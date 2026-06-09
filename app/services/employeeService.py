from datetime import datetime
from app.extensions import db
from app.models.employee import Employee
from app.models.user import User
from app.validations.employeeValidator import validate_employee

class EmployeeService:
    @staticmethod
    def getAll(user_id: int = None)->list[dict]:
        query = Employee.query
        if user_id is not None:
            employees = query.filter_by(user_id=user_id)
        employees = query.order_by(Employee.created_at).all()
        return [e.to_dict() for e in employees]
    
    @staticmethod
    def getById(employee_id: int)->dict | None:
        employee = Employee.query.get(employee_id)
        return employee.to_dict() if employee else None
    
    @staticmethod
    def create(data: dict) -> tuple[dict | None, list[str]]:
        """
        Create a new employee.
        Returns (employee_dict, errors). On success errors=[].
        """
        errors = validate_employee(data, is_update=False)
        if errors:
            return None, errors
 
        # Check user exists
        user = User.query.get(data["user_id"])
        if not user:
            return None, [f"User with id {data['user_id']} does not exist."]
 
        # Check duplicate email
        existing = Employee.query.filter_by(email=data["email"]).first()
        if existing:
            return None, ["An employee with this email already exists."]
 
        # Parse hire_date
        hire_date = _parse_date(data["hire_date"])
 
        employee = Employee(
            first_name=data["first_name"].strip(),
            last_name=data["last_name"].strip(),
            email=data["email"].strip().lower(),
            position=data["position"].strip(),
            salary=float(data["salary"]),
            hire_date=hire_date,
            is_active=data.get("is_active", True),
            user_id=data["user_id"],
        )
        db.session.add(employee)
        db.session.commit()
        return employee.to_dict(), []
    
    @staticmethod
    def update(employee_id: int, data: dict) -> tuple[dict | None, list[str]]:
        """
        Update an existing employee (partial update supported).
        Returns (employee_dict, errors). On success errors=[].
        """
        employee = Employee.query.get(employee_id)
        if not employee:
            return None, [f"Employee with id {employee_id} not found."]

        errors = validate_employee(data, is_update=True)
        if errors:
            return None, errors

        # Check user exists if user_id is being changed
        if "user_id" in data:
            user = User.query.get(data["user_id"])
            if not user:
                return None, [f"User with id {data['user_id']} does not exist."]

        
        # Check duplicate email (exclude self)
        if "email" in data:
            existing = Employee.query.filter(
                Employee.email == data["email"],
                Employee.id != employee_id
            ).first()
            if existing:
                return None, ["Another employee with this email already exists."]

        # Apply updates
        str_fields = ["first_name", "last_name", "email", "position"]
        for field in str_fields:
            if field in data:
                setattr(employee, field, data[field].strip())

        if "salary" in data:
            employee.salary = float(data["salary"])
        if "hire_date" in data:
            employee.hire_date = _parse_date(data["hire_date"])
        if "is_active" in data:
            employee.is_active = data["is_active"]
        if "user_id" in data:
            employee.user_id = data["user_id"]
        if "employer_id" in data:
            employee.employer_id = data["employer_id"]

        db.session.commit()
        return employee.to_dict(), []

    @staticmethod
    def delete(employee_id: int) -> tuple[bool, str]:
        """
        Soft-delete an employee by marking is_active=False.
        Returns (success: bool, message: str).
        """
        employee = Employee.query.get(employee_id)
        if not employee:
            return False, f"Employee with id {employee_id} not found."
        employee.is_active = False
        db.session.commit()
        return True, f"Employee '{employee.first_name} {employee.last_name}' deactivated successfully."

def _parse_date(value):
    from datetime import date
    if isinstance(value, date):
        return value
    return datetime.strptime(str(value), "%Y-%m-%d").date()
from flask import Blueprint, request, jsonify
from app.services.employeeService import EmployeeService

employee_bp = Blueprint("employees", __name__)


@employee_bp.route("/", methods=["GET"])
def get_all_employees():
    """GET /api/employees/ — list all employees (filter by ?user_id= or ?employer_id=)"""
    user_id = request.args.get("user_id", type=int)
    employer_id = request.args.get("employer_id", type=int)
    employees = EmployeeService.getAll(user_id=user_id)
    return jsonify({"data": employees, "count": len(employees)}), 200


@employee_bp.route("/<int:employee_id>", methods=["GET"])
def get_employee(employee_id):
    """GET /api/employees/<id> — get one employee"""
    employee = EmployeeService.getById(employee_id)
    if not employee:
        return jsonify({"error": f"Employee {employee_id} not found."}), 404
    return jsonify({"data": employee}), 200


@employee_bp.route("/", methods=["POST"])
def create_employee():
    """POST /api/employees/ — create an employee"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body must be JSON."}), 400

    employee, errors = EmployeeService.create(data)
    if errors:
        return jsonify({"errors": errors}), 422

    return jsonify({"data": employee, "message": "Employee created successfully."}), 201


@employee_bp.route("/<int:employee_id>", methods=["PUT", "PATCH"])
def update_employee(employee_id):
    """PUT/PATCH /api/employees/<id> — update an employee"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body must be JSON."}), 400

    employee, errors = EmployeeService.update(employee_id, data)
    if errors:
        status = 404 if "not found" in errors[0] else 422
        return jsonify({"errors": errors}), status

    return jsonify({"data": employee, "message": "Employee updated successfully."}), 200


@employee_bp.route("/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):
    """DELETE /api/employees/<id> — soft-delete an employee"""
    success, message = EmployeeService.delete(employee_id)
    if not success:
        return jsonify({"error": message}), 404
    return jsonify({"message": message}), 200
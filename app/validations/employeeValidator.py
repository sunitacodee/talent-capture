import re
from datetime import date, datetime


def validate_employee(data: dict, is_update: bool = False) -> list[str]:
    """
    Validate employee input data.
    Returns a list of error strings (empty = valid).
    """
    errors = []

    # --- first_name ---
    if not is_update or "first_name" in data:
        first = data.get("first_name", "")
        if not first or not first.strip():
            errors.append("first_name is required.")
        elif len(first.strip()) < 2:
            errors.append("first_name must be at least 2 characters.")
        elif len(first.strip()) > 80:
            errors.append("first_name must not exceed 80 characters.")
        elif not re.fullmatch(r"[A-Za-z\s\-']+", first.strip()):
            errors.append("first_name must contain only letters, spaces, hyphens, or apostrophes.")

    # --- last_name ---
    if not is_update or "last_name" in data:
        last = data.get("last_name", "")
        if not last or not last.strip():
            errors.append("last_name is required.")
        elif len(last.strip()) < 2:
            errors.append("last_name must be at least 2 characters.")
        elif len(last.strip()) > 80:
            errors.append("last_name must not exceed 80 characters.")
        elif not re.fullmatch(r"[A-Za-z\s\-']+", last.strip()):
            errors.append("last_name must contain only letters, spaces, hyphens, or apostrophes.")

    # --- email ---
    if not is_update or "email" in data:
        email = data.get("email", "")
        if not email or not email.strip():
            errors.append("email is required.")
        elif not _is_valid_email(email):
            errors.append("email must be a valid email address.")

    # --- position ---
    if not is_update or "position" in data:
        position = data.get("position", "")
        if not position or not position.strip():
            errors.append("position is required.")
        elif len(position.strip()) < 2:
            errors.append("position must be at least 2 characters.")
        elif len(position.strip()) > 100:
            errors.append("position must not exceed 100 characters.")

    # --- salary ---
    if not is_update or "salary" in data:
        salary = data.get("salary")
        if salary is None:
            errors.append("salary is required.")
        elif not isinstance(salary, (int, float)):
            errors.append("salary must be a number.")
        elif salary < 0:
            errors.append("salary must be a non-negative number.")
        elif salary > 10_000_000:
            errors.append("salary must not exceed 10,000,000.")

    # --- hire_date ---
    if not is_update or "hire_date" in data:
        hire_date_raw = data.get("hire_date")
        if not hire_date_raw:
            errors.append("hire_date is required.")
        else:
            parsed = _parse_date(hire_date_raw)
            if parsed is None:
                errors.append("hire_date must be a valid date in YYYY-MM-DD format.")
            elif parsed > date.today():
                errors.append("hire_date cannot be in the future.")

    # --- user_id ---
    if not is_update or "user_id" in data:
        user_id = data.get("user_id")
        if user_id is None:
            errors.append("user_id is required.")
        elif not isinstance(user_id, int) or user_id <= 0:
            errors.append("user_id must be a positive integer.")

   

    return errors


def _is_valid_email(email: str) -> bool:
    pattern = r"^[\w\.\+\-]+@[\w\-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email.strip()))


def _parse_date(value) -> date | None:
    if isinstance(value, date):
        return value
    try:
        return datetime.strptime(str(value), "%Y-%m-%d").date()
    except ValueError:
        return None
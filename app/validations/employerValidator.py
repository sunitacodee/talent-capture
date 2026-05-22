import re

VALID_INDUSTRIES = [
    "Technology", "Healthcare", "Finance", "Education",
    "Manufacturing", "Retail", "Construction", "Transportation",
    "Entertainment", "Agriculture", "Other"
]


def validate_employer(data: dict, is_update: bool = False) -> list[str]:
    """
    Validate employer input data.
    Returns a list of error strings (empty = valid).
    """
    errors = []

    # --- company_name ---
    if not is_update or "company_name" in data:
        name = data.get("company_name", "")
        if not name or not name.strip():
            errors.append("company_name is required.")
        elif len(name.strip()) < 2:
            errors.append("company_name must be at least 2 characters.")
        elif len(name.strip()) > 150:
            errors.append("company_name must not exceed 150 characters.")

    # --- industry ---
    if not is_update or "industry" in data:
        industry = data.get("industry", "")
        if not industry or not industry.strip():
            errors.append("industry is required.")
        elif industry not in VALID_INDUSTRIES:
            errors.append(f"industry must be one of: {', '.join(VALID_INDUSTRIES)}.")

    # --- contact_email ---
    if not is_update or "contact_email" in data:
        email = data.get("contact_email", "")
        if not email or not email.strip():
            errors.append("contact_email is required.")
        elif not _is_valid_email(email):
            errors.append("contact_email must be a valid email address.")

    # --- phone (optional) ---
    if "phone" in data and data["phone"]:
        phone = data["phone"].strip()
        if not re.fullmatch(r"[\d\s\-\+\(\)]{7,20}", phone):
            errors.append("phone must be a valid phone number (7–20 digits/symbols).")

    # --- address (optional) ---
    if "address" in data and data["address"]:
        if len(data["address"].strip()) > 250:
            errors.append("address must not exceed 250 characters.")

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
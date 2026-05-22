from datetime import datetime
from app.extensions import db
from app.models.employer import Employer
from app.models.user import User
from app.validations.employerValidator import validate_employer
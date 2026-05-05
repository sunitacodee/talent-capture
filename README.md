### Clone the Repository
git clone https://github.com/your-username/your-repo.git
cd your-repo

### Create Virtual Environment
## windows
python -m venv .venv
.venv\Scripts\activate

## MAC/linux
python3 -m venv .venv
source .venv/bin/activate

## if activation fails
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
 # then retry
 .venv\Scripts\activate

## Install dependencies
pip install -r requirements.txt

## create .env file and copy
FLASK_APP=run.py
FLASK_ENV=development

DB_USER=root

DB_PASSWORD=yourpassword

DB_HOST=localhost

DB_NAME=new_talent_capture


## create database
CREATE DATABASE new_talent_capture;
## run migration
flask db init        # create migrations folder (only once)

flask db migrate     # generate migration file

flask db upgrade     # apply to DB# talent-capture
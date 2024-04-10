# social-responsibility-project-turkey

To run: (clone the repo, install git, click big green button, click copy, type: git clone <paste here without angled brackets> in a command prompt on windows)

### Install Python 3.

### Install virtualenv.

## On windows, launch a command prompt as admin

### cd social-responsibility-project-turkey

### Run: virtualenv venv

### On windows run: venv/Scripts/activate

### Run: python -m pip install -r requirements.txt 

### cd turkish_questions_project

### python manage.py runserver

# On a browser go to 127.0.0.1:8000

IF you have not created a super user then run python manage.py createsuperuser and follow the prompts.  Then do a python manage.py makemigrations followed by python manage.py migrate.

If you want to load the database with raw data (I already have but it's a sqlite3 db so you can just delete the db file and recreate it by submitting new data) then you can run: python manage.py loaddata rawdata.json and edit rawdata.json before running that command.

If you want as admin, to add/edit user data then you go to 127.0.0.1:8000/admin

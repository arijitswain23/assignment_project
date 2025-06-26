
**Backend Setup (Django + PostgreSQL)**

cd backend/auth_project
python -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt

**Configure PostgreSQL**

- Create a PostgreSQL database and user.
- Update `backend/auth_project/auth_project/settings.py`:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',   # Use the db name
        'USER': 'your_db_user',   # Use the username
        'PASSWORD': 'your_db_password',  # Use the password
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

 **Apply Migrations & Create Superuser**

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

**Run the Backend Server**

python manage.py runserver

 **Frontend Setup (Vue.js)**

cd frontend/auth-frontend
npm install
npm run dev

## Functionality Of the Project

**Registration & Login**

- Users register via the register page.
- After registration, users must wait for admin approval.
- Admins (superusers) can log in immediately in login page.
- Admins log in and are redirected to the admin dashboard.
- Admin dashboard shows all pending user requests.
- Admin can view user details and approve users with a single click.
- After admin Approved users can log in and see their dashboard with their details.

(Just uncomment the DATABASES in `settings.py` we can use sqlite3 database.)

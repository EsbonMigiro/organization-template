# Django-React Web Application

This is a full-stack web application built using **Django** (backend) and **React** (frontend). The React application is contained within the Django project. The project features a landing page with multiple pages, a contact form, sign-in and sign-up forms, and it uses **PostgreSQL** as the database. The Django REST Framework (**DRF**) is used for building APIs for the frontend to interact with the backend.

## Features

- **Landing Page**: The landing page showcases the main features of the web application with links to different pages.
- **Contact Form**: A contact form allowing users to submit inquiries, which are stored in the database.
- **User Authentication**:
  - Sign-up form for new users to create an account.
  - Sign-in form for existing users to log in.
  - Authentication managed by Django and React integration.
- **PostgreSQL Database**: Used to store user information, inquiries, and other data.
- **Django REST Framework (DRF)**: Used to create RESTful APIs to handle communication between the React frontend and the Django backend.

## Technologies Used

- **Frontend**: React, HTML5, CSS3, JavaScript
- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL
- **Deployment**: Gunicorn and Nginx (for production), Docker (optional)

## Setup Instructions

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- Node.js and npm
- PostgreSQL
- Django (installed via `pip`)
- React (handled via `npm`)

### Backend Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/EsbonMigiro/organization-template.git
   cd organization-template/backend
   ```

2. **Install Python dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up PostgreSQL**:

   - Create a PostgreSQL database for the project.
   - Update the database credentials in `backend/settings.py`:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'your_db_name',
           'USER': 'your_db_user',
           'PASSWORD': 'your_db_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

4. **Apply migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Run the Django server**:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup

1. **Navigate to the frontend directory**:

   ```bash
   cd ../frontend
   ```

2. **Install frontend dependencies**:

   ```bash
   npm install
   ```

3. **Start the React development server**:
   ```bash
   npm start
   ```

### Run the Project

Once both the Django and React servers are running:

- Access the backend at `http://localhost:8000/`
- Access the frontend at `http://localhost:3000/`

## API Endpoints

Here are some of the API endpoints provided by the Django REST Framework:

- **User Authentication**: `/api/auth/`
  - `POST /api/auth/login/`: Log in users.
  - `POST /api/auth/signup/`: Register new users.
- **Contact Form**: `/api/contact/`
  - `POST /api/contact/submit/`: Submit contact inquiries.
- **Other APIs**: Customize the endpoints based on your needs.

## Deployment

For deployment, you can use **Gunicorn** as the application server and **Nginx** as the reverse proxy. Docker can also be used for containerization.

1. **Gunicorn setup**:

   ```bash
   gunicorn backend.wsgi:application --bind 0.0.0.0:8000
   ```

2. **Nginx configuration**:
   Configure Nginx to serve the static files and proxy requests to Gunicorn.

3. **Docker setup** _(optional)_: A `Dockerfile` and `docker-compose.yml` can be used to containerize the application.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the open-source community for their contributions to Django, React, and PostgreSQL.

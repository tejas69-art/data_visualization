
# Dashboard Project

This is a Django-based dashboard project designed to provide insights and visualizations for energy data. The project includes a RESTful API built with Django REST Framework, PostgreSQL for data storage, and CORS support for cross-origin requests.

## Features

- **RESTful API**: Exposes energy insights data via a REST API.
- **PostgreSQL Database**: Stores energy-related data efficiently.
- **CORS Support**: Allows cross-origin requests for frontend integration.
- **Django REST Framework**: Provides powerful tools for building APIs.
- **Django Filters**: Enables filtering of API data.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.8 or higher
- PostgreSQL
- pip (Python package manager)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/dashboard-project.git
   cd dashboard-project
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the PostgreSQL database**:
   - Create a database named `dashboard_db` in PostgreSQL.
   - Update the `DATABASES` configuration in `settings.py` with your PostgreSQL credentials:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'dashboard_db',
             'USER': 'your-username',
             'PASSWORD': 'your-password',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```

5. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional)**:
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

8. **Access the API**:
   - The API will be available at [http://127.0.0.1:8000/api/energy-insights/](http://127.0.0.1:8000/api/energy-insights/).
   - Access the Django admin panel at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

## API Endpoints

- **GET** `/api/energy-insights/`: Retrieve a list of energy insights.
- **POST** `/api/energy-insights/`: Create a new energy insight.
- **GET** `/api/energy-insights/{id}/`: Retrieve a specific energy insight by ID.
- **PUT** `/api/energy-insights/{id}/`: Update a specific energy insight by ID.
- **DELETE** `/api/energy-insights/{id}/`: Delete a specific energy insight by ID.

## Environment Variables

For production, ensure the following environment variables are set:

- `SECRET_KEY`: Django secret key for security.
- `DEBUG`: Set to `False` in production.
- `ALLOWED_HOSTS`: List of allowed hosts for the application.
- `DATABASE_URL`: PostgreSQL database URL (if using environment variables for database configuration).

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add some feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/YourFeatureName
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Happy Coding! 🚀



Access Control Log API

Author: Tanvir Ahmed Joy
Email: [tanvir14ahmed@gmail.com](mailto:tanvir14ahmed@gmail.com)
GitHub: [https://github.com/tanvir14ahmed/access_control_log_api](https://github.com/tanvir14ahmed/access_control_log_api)

Table of Contents

* Project Overview
* Features
* Tech Stack
* Project Setup
* API Endpoints
* Signal Logging
* Postman Testing
* Git Workflow

Project Overview
This project is a Django-based REST API that simulates a simple access control logging system. It records door access events, including card ID, door name, access status, and timestamp.
The system also automatically logs creation and deletion events to an external log file (system_events.log) using Django Signals and Python's subprocess module.
This project demonstrates:

* Django REST Framework (DRF) APIs
* Database modeling with SQLite
* Signal handling for system logging
* Proper Git workflow with branching and remote management

Features

* CRUD API for Access Logs: Create, Read, Update, Delete access logs
* Automated Event Logging: On creation: logs event with timestamp and access status; On deletion: logs event with timestamp and card ID
* Clean project structure with .gitignore for virtual environments and sensitive files
* Fully tested with Postman

Tech Stack

* Backend Framework: Django 4.x
* REST API: Django REST Framework (DRF)
* Database: SQLite3 (local, default)
* Python Version: 3.11+
* Version Control: Git & GitHub

Project Setup

1. Clone Repository
   git clone [https://github.com/tanvir14ahmed/access_control_log_api.git](https://github.com/tanvir14ahmed/access_control_log_api.git)
   cd access_control_log_api

2. Create Virtual Environment
   python -m venv .venv

Activate:

* Windows (PowerShell): .venv\Scripts\Activate.ps1
* Windows (CMD): .venv\Scripts\activate.bat

3. Install Dependencies
   pip install -r requirements.txt
   (Requirements include Django>=4.2, djangorestframework>=3.14)

4. Apply Migrations
   python manage.py migrate

5. Run the Development Server
   python manage.py runserver
   API will be available at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

API Endpoints

| Method | Endpoint        | Description                        |
| ------ | --------------- | ---------------------------------- |
| POST   | /api/logs/      | Create a new AccessLog entry       |
| GET    | /api/logs/      | Retrieve all AccessLog entries     |
| GET    | /api/logs/<id>/ | Retrieve a single AccessLog entry  |
| PUT    | /api/logs/<id>/ | Update an existing AccessLog entry |
| DELETE | /api/logs/<id>/ | Delete an AccessLog entry          |

Example POST Request (JSON)
{
"card_id": "C1001",
"door_name": "Main Entrance",
"access_granted": true
}

Signal Logging
All create and delete events are logged automatically to system_events.log in the project root.

* Create example: [2026-01-07 15:55:01] - CREATE: Access log created for card C1001. Status: GRANTED.
* Delete example: [2026-01-07 16:01:12] - DELETE: Access log (ID: 3) for card C1001 was deleted.
  This ensures all access log events are auditable in real-time.

Postman Testing

1. Open Postman
2. Import collection (if available) or test endpoints manually
3. Use the following methods:

   * GET /api/logs/ → List all logs
   * POST /api/logs/ → Create log
   * PUT /api/logs/<id>/ → Update log
   * DELETE /api/logs/<id>/ → Delete log
     (Remember to add trailing slashes / in Django URLs.)

Git Workflow

* Development branch: development
* Merged into main for submission
* .venv/ and .env/ are ignored via .gitignore
* Branching history preserved in GitHub

License
This project is for educational and professional submission purposes.

Contact,

Tanvir Ahmed Joy
* Phone: +8801823555505
* Email: [tanvir14ahmed@gmail.com](mailto:tanvir14ahmed@gmail.com)
* GitHub: [https://github.com/tanvir14ahmed](https://github.com/tanvir14ahmed)

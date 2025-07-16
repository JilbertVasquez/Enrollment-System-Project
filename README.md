# Enrollment System Project

## Project Description
Enrollment System Project is a Python desktop application for managing student enrollment at Allison International School. It provides secure login, registration, and a dashboard for students, along with features for viewing academic details, tuition, and club participation. The application uses a modern UI and connects to a MySQL database for persistent data storage.

## Tech Stack
- ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) Python 3
- ![Tkinter](https://img.shields.io/badge/Tkinter-FFCA28?style=fora-the-badge&logo=python&logoColor=black) Tkinter
- ![Pillow](https://img.shields.io/badge/Pillow-1E90FF?style=for-the-badge&logo=python&logoColor=white) Pillow
- ![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white) MySQL
- ![PyMySQL](https://img.shields.io/badge/PyMySQL-0DB7ED?style=for-the-badge&logo=mysql&logoColor=white) PyMySQL

## Features
- User registration with validation
- Secure login authentication
- Dashboard with student details and tuition calculation
- Certificate of Registration (COR) with subjects, codes, and units
- Club participation info
- Liabilities overview
- Modern, image-rich UI

## Setup Instructions
1. Ensure you have Python 3 installed.
2. Install required packages:
   ```pwsh
   pip install pymysql pillow
   ```
3. Ensure MySQL is running locally.
4. The application will auto-create the `portal` database and `register` table if not present.
5. Update MySQL credentials in `portal.py` if needed (default: `user='root'`, `password='root'`).
6. Run the application:
   ```pwsh
   python portal.py
   ```

## Usage
- Register as a new user or log in with existing credentials.
- View your dashboard, tuition, and academic details.
- Access your Certificate of Registration (COR).
- Explore club participation and liabilities.

## Database
- MySQL database named `portal`.
- Table: `register` (created automatically if missing).

## Author
- Developed by Jilbert Vasquez.

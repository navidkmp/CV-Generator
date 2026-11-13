# CV Generator

A web-based CV Generator built with **Python and Django** that allows users to create, manage, edit, and download professional resumes in PDF format.

## 🚀 Overview

CV Generator is a Django-based web application designed to make resume creation simple and convenient. Users can enter their personal information, educational background, work experience, skills, and professional summary to generate a structured CV.

The application also provides resume management features, allowing users to view, edit, delete, and download their CVs as PDF files.

## ✨ Features

- **Create CV:** Generate a resume by submitting personal and professional information.
- **View CV:** Preview your generated resume.
- **Edit CV:** Update existing resume information whenever needed.
- **Delete CV:** Remove unwanted resumes.
- **PDF Export:** Download resumes as PDF files.
- **Dashboard:** View and manage all created resumes.

## 🛠️ Technologies Used

- **Python** – Backend programming language
- **Django** – Web framework
- **HTML5** – Page structure
- **Tailwind CSS** – Styling and responsive design
- **SQLite / Django Database** – Data storage
- **xhtml2pdf** – PDF generation

## 📋 Requirements

- Python 3.10+
- pip
- Git

## ⚙️ Installation & Setup

**1. Clone the repository**

```bash
git clone https://github.com/navidkmp/CV-Generator.git
```

**2. Navigate to the project directory**

```bash
cd CV-Generator
```

**3. Create a virtual environment**

```bash
python -m venv venv
```

**4. Activate the virtual environment**

Windows:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

**5. Install dependencies**

```bash
pip install -r requirements.txt
```

**6. Apply database migrations**

```bash
python manage.py migrate
```

**7. Run the development server**

```bash
python manage.py runserver
```

**8. Open the application**

Visit:

```text
http://127.0.0.1:8000/
```

## 🎯 Project Goals

The main goal of this project is to practice and demonstrate Django development skills, including:

- Django Models and Database Operations
- CRUD Functionality
- URL Routing and Views
- Django Template Engine
- Form Handling and CSRF Protection
- PDF Generation and File Export

## 👨‍💻 Author

**NdevX (navidkmp)**

GitHub: [navidkmp](https://github.com/navidkmp)

---

⭐ If you find this project useful, consider giving it a star!

**Built with Python & Django.**
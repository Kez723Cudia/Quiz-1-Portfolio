# Quiz-1-Portfolio
A personal portfolio project requirement for Quiz 1, built with Django and Bootstrap.

## Features
- Responsive design with the help of Bootstrap.
- Django Framework for the Backend Logic.
- Portfolio pages (Home/Hero, About, Projects, Skills, Contact)

## Setup Instructions (Procedure)
1. Clone the repository:
```bash
    git clone https://github.com/<Ky723Cudia>/Quiz-1-Portfolio.git
    cd Quiz-1-Portfolio
```
2. Create and activate a virtual environment:
```bash
    python -m venv venv
    source venv/bin/activate   # for Mac/Linux
    venv\Scripts\activate      # for Windows
```
3. Install dependencies:
```bash
    pip install -r requirements.txt
```
4. Verify Django installation:
```bash
    python -m django --version
```
## Project Initialization
This repository has been initialized with Django.

Then:
```bash
    django-admin startproject portfolio .
```
### Project Structure
```bash
    Quiz-1-Portfolio/
    ├── manage.py
    ├── portfolio/
    │   ├── init.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    ├── venv/
    │   ├── Include/
    │   ├── Lib/
    │   ├── Scripts/
    │   └── pyvenv.cfg
    ├── .gitignore
    ├── README.md
    └── requirements.txt
```

- `manage.py` is the command-line utility for project management.  
- `portfolio/` is the Django project folder with settings, URLs, WSGI, and ASGI entry points.  
- `venv/` means Virtual environment (not tracked in GitHub if `.gitignore` is set correctly)
- `.gitignore` is to specify files/folders to exclude from version control.  
- `requirements.txt` lists Python dependencies.  
- `README.md` is the documentation file.  

### Notes

- `db.sqlite3` is created automatically after migrations.
- It is excluded from version control via `.gitignore` to keep the repository clean.

### Progress

- Django project initialized and verified.
- Home app created and registered in `INSTALLED_APPS`.
- Basic Hero page view added and tested at root URL (`/`).
- Server runs successfully with no issues (`python manage.py check` passed).
- Bootstrap integrated via CDN and verified with placeholder page.
- Bootstrap Navbar added and verified locally.
- Bootstrap Hero section created with heading, tagline, and CTA button.
- Hero page redesigned with split layout:
  - Dark left side (3/5 width) with name, surname, tagline, and CTA button.
  - Professional font applied to names, larger font sizes, and repositioned higher.
  - Tagline font size and thickness increased proportionally.
  - CTA button styled with navy border and matching metallic blue background.
  - Right side (2/5 width) updated to darker metallic blue, consistent with button color.
- Hero page improved with professional font, larger text, optimized layout, CTA button styling, and Primary Stack section.

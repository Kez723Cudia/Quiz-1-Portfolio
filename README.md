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
- Hero page refined with Helvetica font, vertically stretched names, optimized tagline spacing, and larger right-side containers.
- Hero page finalized with upper stats (23+ Clients Worldwide), middle Primary Stack section, and lower Status section (Available for opportunities, open for full-time roles & consulting).
- Added Hero page with "See more ➔" navigation
- Implemented About page with bio, timeline, passions, and cohesive design
- Implemented Skills page with categorized competencies (Technical, Professional, Soft).
- Implemented Projects page with placeholders for Arduino builds and future cloud/web projects.
- Implemented Contact page with “Build With Me” heading, Drop me a mes
- Added hover animations for Previous/See more links across all pages.
- Added hover animations for tracker navbar links.
- Fixed tracker navbar active state indicator (underline only active page).
- Hero page “Work with Me” button now routes directly to Contact page.

# Quiz 2

Welcome! This is a continuation of Quiz 1. The same repository, files, and folders are used.  
Quiz 2 introduces backend and database functionality, with strict workflow rules.

## Instructions
To run this project locally and verify its functionality:

1. **Clone the repository**
```bash
    git clone https://github.com/<Ky723Cudia>/Quiz-1-Portfolio.git
    cd Quiz-1-Portfolio
```

2. **Create and activate a virtual environment**
```bash
    python -m venv venv
    source venv/bin/activate   # for Mac/Linux
    venv\Scripts\activate      # for Windows
```

3. **Install dependencies**
```bash
    pip install -r requirements.txt
```

4. **Apply migrations to set up the database**
```bash
    python manage.py makemigrations
    python manage.py migrate
```

5. **Create a superuser account**
```bash
    python manage.py createsuperuser
```
- This allows any user to log in with their own credentials.
- Once logged in at http://127.0.0.1:8000/admin/, they can view and manage Projects and Personal Information.

6. **Run the development server**
```bash
    python manage.py runserver
```

7. **Access the site in a browser**
- For the Portfolio pages, open http://127.0.0.1:8000/ (this link is displayed in the terminal after starting the server).
- For the admin dashboard, open: http://127.0.0.1:8000/admin/ Just add 'admin/' to the URL of the portfolio pages.
    - Then login with the superuser account created earlier.

### Progress in Quiz 2

- Added `Project` and `PersonalInformation` models with appropriate fields for project details and personal data.

- Registered both models in Django Admin for management and verification.

- Created function-based views in `projects/views.py`:
  - `list_view` — displays all projects dynamically from the database.
  - `detail_view` — shows details for a single project by ID.
  - `personal_info_view` — displays personal information records.

- Updated `projects/urls.py` to include routes for list, detail, and personal info views.

- Built new templates in `home/templates/projects/`:
  - `list.html` — renders all projects with clickable links to detail pages.
  - `detail.html` — renders full details of a single project.
  - `personal_info.html` — renders personal information records.

- Verified routing and template rendering:
  - `/projects/list/` shows all projects.
  - `/projects/1/` shows details for project ID 1.
  - `/projects/personal-info/` shows personal information.

- Tested with sample data in Django Admin:
  - Added a project named **Portfolio** with description, tech stack, and GitHub link.
  - Added a personal information record with full name, contact number, email, and address.

- Confirmed templates now render dynamic data from the database instead of hardcoded HTML.

- Deleted the old static `projects.html` file and replaced it with a dynamic `list.html`.
  - **Decision:** This ensured the Projects page now pulls data directly from the database instead of hardcoded HTML.
  - **Rationale:** Moving away from static content makes the portfolio scalable and easier to maintain.

- Integrated the UI design from the deleted static `projects.html` into the new function-based templates:
  - `list.html` — displays all projects dynamically with the same polished UI as before.
  - `detail.html` — shows full project details with styling consistent with the original static design.
  - **Debugging Decision:** Carefully merged the old UI elements into Django’s template system so the look remained intact while functionality became dynamic.

- Created a new `personalinfo` app dedicated to handling personal information. Then moved the `PersonalInformation` model and related functionality into a new `personalinfo` app.
  - **Decision:** Separated concerns by moving `PersonalInformation` out of `projects` to avoid duplication and confusion.
  - **Debugging Decision:** Fixed the “No personal information available” issue by re-entering data under the new app’s model instead of the old one.

- Created a new folder `home/templates/personal-info/` to store the `personal_info.html` template.
  - **Decision:** This folder structure matches the render path (`"personal-info/personal_info.html"`) and ensures Django can locate the template correctly.
  - **Debugging Decision:** Solved `TemplateDoesNotExist` errors by aligning the template path with the view’s render call.

- Added the Personal Info page to the navbar and ensured consistent navigation across all templates.
  - **Rationale:** This makes personal information easily accessible and keeps the portfolio cohesive.

- Fixed routing issues in multiple places:
  - Corrected navbar links so each page points to the right view.
  - Adjusted the `Previous` and `See more >` buttons:
    - **Decision:** Aligned “< Previous” on the left and “See more >” on the right for a professional layout.
    - **Debugging Decision:** Fixed placement errors by restructuring the HTML and CSS.

- Verified functionality:
  - `/projects/list/` shows all projects dynamically.
  - `/personal-info/` shows personal information records with the updated summary text.
  - **Decision:** Removed the literal “Summary:” label from the template to keep the output clean and professional.

- Final polish:
  - Confirmed templates now render dynamic data from the database.
  - Ensuring the portfolio is both functional and styled.
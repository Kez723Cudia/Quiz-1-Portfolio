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


# Quiz 3

Welcome! This is a continuation of Quiz 1. The same repository, files, and folders are used.  
Quiz 2 introduces new models, forms, and views for **Projects, Contact (Inquiries), and Testimonies**.

## Instructions

To run and check Quiz 3 locally:

1. **Clone the repository**
```bash
git clone https://github.com/<Ky723Cudia>/Quiz-1-Portfolio.git
cd Quiz-1-Portfolio
```
2. **Create and activate a virtual environment**
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```
3. **Install dependencies**
```bash
pip install -r requirements.txt
```
4. **Apply migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```
5. **Run the development server**
```bash
python manage.py runserver
```
6. **Navigate the portfolio via buttons**
- Use the navbar to move between Hero, About, Skills, Projects, Contact, Personal Info, and Testimonies.
- Verify navigation flow with Previous and See more buttons across pages.
- On the Projects list page, click any project title to view its detail.
- Use the Add Project button to access the create view and add a new project.
- On the Testimonies list page, click any testimony to view its detail.
- Use the Share Your Testimony button to access the create view and submit a testimony.
7. **Check placeholders/test data**
- Disclaimer: Some placeholders served as testers (specifically, in projects and testimonies) were intentionally left in the database and templates during testing. These serve as evidence of correctness: you can see them listed, click into their detail views, and confirm that create forms work properly.
8. **Backend verification (optional)**
- Access the Django Admin at http://127.0.0.1:8000/admin/ with a superuser account.
- From there, you can view and confirm entries for Projects, Inquiries, and Testimonies directly in the database.

## Procedures
1. Created a new branch named quiz3 and switched to it locally, then pushed it to the remote repository.
2. Created a new app for testimonies, then added it to the project folder’s (portfolio) settings.py.
3. Added models: in contact/models.py created a model (class) for Inquiry; and in testimonies/models.py created a model (class) for Testimony.
4. Ran migrations to generate the database tables for Inquiry and Testimony.
5. Committed changes.
6. Registered models in Admin: added and viewed the Inquiry and Testimony models in the Django Admin panel.
 - Changes made in:
          contact/admin.py
          testimonies/admin.py
- Saved changes and ran the server. Verified that “Inquirys” appeared under Contact and “Testimonys” under Testimonies.
7. Created a new file named forms.py inside the Contact app folder. Added a class InquiryForm which connects directly to the Inquiry model, enabling form rendering in HTML templates and saving submissions into the database.
8. Wired the form into the Contact page through a view. When a user submits, Django saves the data into the Inquiry model.
 - Changes made in:
          contact/views.py
          contact/urls.py
          home/templates/contact.html (custom field rendering)
9. Added Bootstrap styling to make inputs consistent with the design. Updated the InquiryForm in contact/forms.py. Tested and confirmed functionality.
10. Committed changes.
11. Created a new forms.py file in the Testimonies app folder. Added a class TestimonyForm in testimonies/forms.py.
12. Added views:
 - Function-Based Create View in testimonies/views.py
 - Class-Based List View in testimonies/views.py
13. Created a new urls.py in the Testimonies app folder and wired the paths.
14. Included Testimonies URLs in the project folder’s (portfolio) urls.py.
15. Created a new subfolder testimonies in home/templates.
16. Added create.html and list.html in home/templates/testimonies and coded their contents.
17. Updated the navbar: added the Testimonies link across all existing pages.
- Changes made in:
 - home/templates/about/about.html
 - home/templates/contact/contact.html
 - home/templates/home/home.html
 - home/templates/personal-info/personal_info.html
 - home/templates/projects/detail.html
 - home/templates/projects/list.html
 - home/templates/skills/skills.html
 - home/templates/testimonies/create.html
 - home/templates/testimonies/list.html
18. Improved styling in testimonies/list.html for a polished and consistent look.
19. Improved styling in testimonies/create.html to harmonize with the portfolio design.
20. Wired in the Previous / See more links to complete page-to-page flow.
21. Committed changes.
22. Added a function testimony_detail in testimonies/views.py.
23. Wired the URL in testimonies/urls.py.
24. Created detail.html in home/templates/testimonies/ and coded its content.
25. Added sample testimonies to test the functionality of list, create, and detail views.
26. Updated testimony_create_view in views.py to redirect to the list view after saving.
27. Improved detail.html styling for consistency with the portfolio.
28. Committed changes.
29. Updated testimony_create_view in views.py to reload the create view after saving (same page refresh).
30. Created a new forms.py in the Projects app folder and coded its contents.
31. Added the create view in projects/views.py.
32. Wired the URL in projects/urls.py.
33. Created the template create.html in home/templates/projects/ and coded its content.
34. Updated the Projects create view to render each field manually with .form-control for consistent styling. 

## Progress
1. The Inquiry model is fully functional and connected to the existing Contact page (originally created in Quiz 1). 
- Visitors can submit inquiries through the Contact form, and their submissions are saved into the database via the Inquiry model. 
- The form is styled with Bootstrap for consistency. 
- The Contact page also displays my personal contact details, and navigation is verified through buttons (navbar, Previous, See more).
2. The Testimonies feature was newly added in Quiz 3. 
- It includes a create page where visitors can submit feedback using a Django Form and a Function-Based Create View. Submitted testimonies are saved into the database and displayed on the list page, which uses a Class-Based List View. 
- Each testimony name is clickable and routes to a detail page, which uses a Function-Based Detail View to show the full content. Placeholders and test testimonies were left in the database to demonstrate correctness and allow verification of the create → list → detail flow. 
- Navigation is verified through buttons (Share Your Testimony, Previous, Back to list, navbar links).
3. The Projects feature now includes a detail view. 
- Each project listed is clickable and routes to its detail page, which displays the project’s name, description, tech stack, and external link. 
- The detail page is styled consistently with the portfolio and includes navigation back to the Projects list. 
- Test projects were left in the database to demonstrate correctness and allow verification of the create → list → detail flow.
5. Backend accessible via Django Admin for direct database checks.


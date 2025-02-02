# FAQ Project

This is a Django-based FAQ management system that supports multilingual content, WYSIWYG editor for answers, and caching using Redis.

## Features
- **Multilingual support**: Store and manage FAQs in multiple languages (English, Hindi, Bengali, etc.).
- **WYSIWYG Editor**: Rich text editor for better formatting of answers using `django-ckeditor`.
- **API for FAQs**: Create a REST API for managing FAQs.
- **Redis Caching**: Improved performance by caching translations using Redis.
- **Admin Interface**: Manage FAQs through Django’s admin panel.

## Installation

### 1. Clone the repository:
```bash
git clone https://github.com/prasadreddykarri/faq_project.git
cd faq_project


### 2. Set up a virtual environment:
```bash
python -m venv venv


###3. Activate the virtual environment:
#On Windows (PowerShell):
bash
.\venv\Scripts\Activate.ps1

###4. Install the dependencies:
pip install -r requirements.txt

###5. Apply migrations:
python manage.py migrate

###7. Run the server:
python manage.py runserver
The server will start at http://127.0.0.1:8000/

#API Usage
###1. Fetch FAQs in English:
curl http://localhost:8000/api/faqs/

###2. Fetch FAQs in Hindi:
curl http://localhost:8000/api/faqs/?lang=hi






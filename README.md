# Django Backend Product Import

## Overview
Django app that accepts CSV/Excel file from user, parse the file, stores in SQLite and allows for viewing from admin interface by filtering, searching.

## Tech Stack
<ul style="list-style-type:square">
  <li>Python 3.13.0</li>
<li>Django 5.2.6</li>
<li>SQLite 3.43.2</li>
<li>Pandas 2.3.2</li>
</ul>

## Setup(Run on your computer)
1. Clone repo.<br>
   On your computer open terminal where the repo needs to be clone and type
   ```bash
   git clone https://github.com/Pragyanadhikari/File-Upload.git
   ```
2. Create a virtual environment and install required packages.
   ```bash
   python -m venv venv
   source venv/bin/activate #On mac
   venv/Scripts/activate #On windows
   pip install -r requirements.txt
   ```
3. Do migration as:
   ```bash
   python manage.py migrate
   ```
4. Create Superuser
   ```bash
   python manage.py createsuperuser
   ```
5. Run server
   ```bash
   python manage.py runserver
   ```
6. Upload and go to admin through:<br>
   Upload: http://127.0.0.1:8000/<br>
   Admin:  http://127.0.0.1:8000/admin/

## Usage
<ol type="1">
<li> Upload a CSV or Excel file with fields ('sku','name','category','price','stock_qty','status').</li>
<li> The import uses sku as unique key; rows will update_or_create to avoid duplication.</li>
</ol>

## Assumptions
<ul>
  <li>SKU is unique and required.</li>
  <li>Only the file with the colums above are allowed and only file with extension of .csv, .xlsx, .xls are allowed.</li>
</ul>

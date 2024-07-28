1. Clone repository
```git clone https://github.com/RuslanHale/rent_car.git```
2. Go to directory rent_project
```cd rent_project```
3. Create virtual environment
```python -m venv venv```
4. Activate virtual environment
```venv/Scripts/activate```
5. Install dependencies
```pip -install requirements.txt```
6. Load PostgreSQL to your computer https://www.postgresql.org/download/
Create password and remember that. Change database password in rent_project/settings.py to your own. 
8. Install PostgreSQL to Django
```pip install psycopg2```
9. Find pgAdmin and log in there
10. In pgAdmin create database and name it "rent_database"
11. Make migrations
```py manage.py makemigrations```
```py manage.py migrate```
12. Create super user
```py manage.py superuser```
13. Launch your server
```py manage.py runserver```

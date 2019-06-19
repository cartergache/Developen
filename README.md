# Developen

Follow these instructions to setup Developen on your local machine. These instructions are a work in progress so please add to it if you feel it is necessary.

# Setup
These set up instructions are meant for Mac OS.

## Virtual Environment

After cloning the repository to your local machine, you will need to setup a virtual environment. Navigate to your root project directory and do the following.

1. Run `python3 -m virtualenv venv` to create a new virtual environment.
2. Run `source venv/bin/activate` to activate it.
3. Run `pip install -r requirements.txt` in order to install the required dependencies

## Database 

1. Download PostgreSQL.
2. When prompted to do so, create a new PostgreSQL user with username `postgres` and password `postgres`.
3. Launch pgAdmin 4.
4. Create a new server with a descriptive title.
5. Create a new database called `developen` and give the `postgres` user access.
6. From project root directory run `python manage.py migrate` to create the database tables.

## Admin Account

* Run `python manage.py createsuperuser` and enter a username and password when prompted.

## Run Application

1. From project root run `python manage.py runserver`.
2. Go to `http://localhost:8000/projects/` in your browser to view the Developen application.
3. The administrator interface is viewable at `http://localhost:8000/admin/`.

## Development Practices

1. Always make sure your virtual environment is running before you start developing or run your application.
2. You should be committing your migration files whenever they are created by the `python manage.py migrate` command.

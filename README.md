# django-bot-server

To get this running, simply run the  the following 

## Step 1: Install requirements.txt

`pip install -r requirements.txt`

## Step 2: Create databases

Create the databases and the initial migrations with the following command:
`python manage.py migrate`

## Step 3: Create superuser
create superuser with the following command:
`python manage.py createsuperuser`


## Step 4: Run server

And start the server with 

`python manage.py runserver`

You should now be able to go to localhost:8000/chat/ login and chat with the bot

## Step 5: create users

goto django admin page create as many users you want login and see the button counter stats
localhost:8000/chart/



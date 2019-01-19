# Network Monitoring Center

![NMC](static/img/Screenshot.png?raw=true "NMC")

##### CONTEXT: Along with "Tickets" and "GABC", this app was designed as a "concept app" to streamline various processes in the DoD. Whereas "Tickets" deals with streamlining customer IT support, "Network Monitoring Center was designed to give better situational awareness to deployed COMMS personnel.

##### REASONING: Often time it is difficult to troubleshoot network outages in deployed locations.  Is the problem a result of a bad internal config? Or is it being caused by an "upstream" or "downstream" dependency?

##### This app would provide real-time outage reports from your dependent organizations, as well as provide other COMMS personnel with an up-to-date picture of your current COMSTAT.

##### HOW  TO CONTRIBUTE:

###### Contributions are always welcome!  Whether you are new to Django or web development in general (like me), you are more than welcome to contribute!

STEP 1: Clone the project (in the terminal): ```git clone https://github.com/tjdolan121/nmc.git```

STEP 2: Create a new virtual environment: ```virtualenv env```

STEP 3: Activate the virtual environment: ```source env/bin/activate```

STEP 4: Navigate to the project directory (should contain "manage.py" file) and install requirements: ```pip install -r requirements.txt```

STEP 5: Obtain a SECRET_KEY: https://www.miniwebtool.com/django-secret-key-generator/

STEP 5: Create a .env file in the project directory

STEP 6: Add a secret key environment variable (in .env): ```SECRET_KEY=(paste key here)```

STEP 7: Run migrations (while in project directory): ```python manage.py migrate```

STEP 8: Create a superuser account: ```python manage.py createsuperuser```

STEP 9: Run server: ```python manage.py runserver```

STEP 10: Navigate to http://127.0.0.1:8000/admin in browser, log in with your super user account, and create some data.

### Please feel free to message me if you have any questions!

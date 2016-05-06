# Trenary Workflow Project

This is a program intended for use at Western Michigan University by Dr. Robert Trenary. This webapp works in conjunction with a gitolite server with which students are given accounts to. 
Students pull assignments and push their work. Their work is then be pulled by a test package, tested, and reviewed for a final grade. Grades are submitted in a PDF sheet within the students repository. 

The webapp is here to ease the process of viewing the state of the repositories, creating new assignments, and archiving semesters worth of work to "restart" for another semester.

## How to

From DigitalOcean's [tutorial](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps)...

To run the server we will create a virtual environment for the flask application.

We will use pip to install virtualenv and Flask. If pip is not installed, install it on Ubuntu through `apt-get`.

`sudo apt-get install python-pip`

If virtualenv is not installed, use pip to install it using following command:

`sudo pip install virtualenv`

Give the following command (where venv is the name you would like to give your temporary environment):

`sudo virtualenv venv`
Now, install Flask in that environment by activating the virtual environment with the following command:

`source venv/bin/activate`

Give this command to install Flask inside:

`sudo pip install Flask`

Next, run the following command to test if the installation is successful and the app is running:

`sudo python run.py`

It should display “Running on http://localhost:5000/” or "Running on http://127.0.0.1:5000/". If you see this message, you have successfully configured the app.

To deactivate the environment, give the following command:

`deactivate`

This runs the server on port `5000`.
To add a user account edit the `config.py` with a new user entry.


## TODO:
- [x] Simple auth for sensitive data.
- [x] List active repositories.
- [ ] List archived courses.
- [ ] Download a students' work for a course.
- [ ] Archive a course.
- [ ] Begin a course.
- [ ] Display an assignment as graded if a file matching \Graded*.pdf\ exists in the repo.
- [ ] Check the environment to ensure that repositories, bakups, etc. are in their expected directories.
- [ ] OAuth


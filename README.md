CliGo
=====

NB:
Please Read this

** Before you push into our repository
** Remember to pull what is currently there
** Note pull it right before you push
** 
** This is not the pull you do when you want to 
** make changes but after you finished with the
** changes.
**
** Therefore you do two pushes!!!!
** 1. Pull
** 2. Make changes
** 3. Pull again
** 4. Push

** please tell us the changes you made on each
** particular day in this README file
** with you name
** eg is the one below
Team CliGo

************************************************
** By Philip on Tue July 24, 2012 11:59:3 AM: **
** Created the django project cligo ************
************************************************

************************************************
** By Philip on Tue July 25, 2012 11:59:3 AM: **
** Register users into cligo with validation****
** Sent reply back after validateion************
************************************************

************************************************
** By Philip on Tue July 26, 2012 11:59:3 AM: **
** Setup system which sends specific messages **
** to specific users this code is at the *******
** development stage ***************************
************************************************

************************************************
** By Philip on Tue July 27, 2012 11:59:3 AM: **
** Finished 85% work of previous day work i.e.**
** Updated the week period successfully  *******
** without making any changes to the current ***
** subscriber week table and without creating***
** any new tables.
** 2. Created a JSON for initial database ******
**    entry for the Hospitals(30) and change****
**    some fields.******************************
** 3. Made serious changes to the main.py file**
**	  in cron. I Hope this doesn't give any ****
**    problem now. *****************************
**     so you install that file for your cron **
**	   is 99.99% bug free! *********************
** 4. Added Afiday app to project access it by**
**		localhost:8000/afiday ******************
************************************************
NB: How to get the above working on local

1. After cloning from the repository

2. get into your django_cron folder

3. do python setup.py install

4. do a syncdb to synchronize and populate your
	database.

5. create a device and add the key value to the
	device.

6. Start server

7. get into the python client folder and run
	sudo python main.py terminal django
	
8. It Should be working..... Woohoo

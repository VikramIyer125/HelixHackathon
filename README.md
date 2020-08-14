# HelixHackathon

This is the project that my team and I used to win 'Most technologically advanced' creation in the 2020 HelixHacks Hackathon. 

We wanted to go beyond a typical information website and make it interactive through utilizing different forms of user engagement. 
We also wanted to provide a place where users can come for accurate and reliable info, rather than reading misinformation about COVID on other sites with political agendas.

Our project was an all in one full COVID-19 Guide. 

We built a web app that had the following features: 

1. A Local Testing Site Page where users can see the different testing sites for each state and get information such as phone number, hours, facility, address, city, and website.
2. A Machine Learning Lung Scan model which informs the patients whether they have COVID-19 based on a lung scan that they upload.
3. An FAQ bot which uses voice recognition to analyze and output answers to the user's questions about COVID.
4. A page which shows the live stats of COVID-19 such as number of affected and number of deaths.
5. A page which allows user to register for a test by redirecting them to a registration page.

We used mostly html,css,javascript as well as Flask and python for the back end development.

We used teachable machine to train our model on images of COVID CT lung scans. 
We used the javascript web speech api to quickly process the user's voice and give an answer to the user's question. 

Running the program: 

Download the repo and enter the HelixHacks directory. Install the required python libraries in the requirements.txt with pip3 install -r requirements.txt

Once that is done, simply running the flask app with python3 flask_app.py should get the web app up and running. 

Note - the download path for the ct scan upload is a path on my computer. Changing the path in the flask_app.py to the path of the upload folder on your computer will allow you to run the model on your computer. 

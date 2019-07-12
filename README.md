# Custom Flask API

Description: Your objective for this challenge will be to produce a tool that will query the ‘status’ page on 1000 servers and produce a report based on data within the status page.  Each server has a ‘status’ endpoint that returns json data.  The details of that json data will be provided below.

Special Notes: I wrote a Flask API called flaskapi.py and the file that will run the code for my tool is called querytool.py. You'll also need the servers.txt file to pull in the list of servers in the API and querytool.py

Instructions:
1. Download the folder 'TwitterFlaskAPI' and unzip it to your Desktop on a Mac/Linux
2. Open up a terminal window and CD into your directory: cd Desktop/TwitterFlaskAPI
3. Make sure you have Python 3.x or higher installed on your computer
4. Create a virtual environment by doing the following:
	A. In your terminal within the same directory (Desktop/TwitterFlaskAPI) run: 	$ python3 -m venv vena
	B. Activate the virtual environment: $ . venv/bin/activate
	C. Install Flask in virtual environment by running: $ pip install Flask
5. Now run the Flask API by executing the following command:
	A. $ export FLASK_APP=flaskapi.py
	B. $ flask run
6. Check if the API is up and running by testing out id=1. Go to: http://localhost:5000/status/1
You should see a JSON response with id=1
7. Open up a second terminal but leave the first one open
8. Navigate to the correct folder: $ cd Desktop/TwitterFlaskAPI
9. Run the querytool.py file with the following command: $ python3 querytool.py
You'll see several things:
	- an api_data.json file will be created in your TwitterFlaskAPI folder
	- the output will print to the console
	- a file called file_output.txt will output to your TwitterFlaskAPI folder
	- open the file to see the output

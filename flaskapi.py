'''
This is a REST API written in Flask.
It generates random data and populates
the endpoints for each server in the
servers.txt file.
'''

from flask import Flask, request
import json
import random
import pathlib

app = Flask(__name__)

# change the configuration for server name
app.config['SERVER_NAME'] = 'localhost:5000'


# Read server names from file
server_file = pathlib.Path("servers.txt")
server_list = server_file.read_text().split()

# create empty dictionary to hold json data
json_data = dict()

# create application names
application_name = ('Cache2',
                    'Webapp1',
                    'Webapp0',
                    'Cache1',
                    'Database1',
                    'Database2',
                    'Database0')

# create version numbers
version_number = ('1.0.0',
                  '0.0.2',
                  '1.1.0',
                  '1.2.2',
                  '0.2.2',
                  '1.2.1',
                  '0.1.1',
                  '1.1.1')

# loop through each server in list and get the index and server name
for i, server in enumerate(server_list, start=1):
    # populate the dictionary with the keys and values
    json_data[i] = {
                    'id':i,
                    'Server': server,
                    'Application':random.choice(application_name),
                    'Version':random.choice(version_number),
                    'Uptime':random.randrange(10**9, 10**10),
                    'Request_Count':random.randrange(10**9, 10**10),
                    'Error_Count':random.randrange(10**9, 10**10),
                    'Success_Count':random.randrange(10**9, 10**10)
                    }
# create an endpoint: /status/1
@app.route("/status/<int:status_id>", methods=['GET'])
def get_status(status_id):
    # open a file in write mode
    with open("api_data.json", "w") as json_file:
        # dump the json_data dictionary into a string
        data = json.dump(json_data, json_file, indent=4)
    # initialize an empty dictionary
    dict = {}
    # set name to None
    name = None
    # for every entry in the jdon_data's values
    for entry in json_data.values():
        # if the entry id is the same as the status id
        if entry['id'] == int(status_id):
            # then assign the dictionary values to variables
            id = entry['id']
            server = entry['Server']
            application = entry['Application']
            version = entry['Version']
            uptime = entry['Uptime']
            request_count = entry['Request_Count']
            error_count = entry['Error_Count']
            success_count = entry['Success_Count']
            break
    # if the application is not empty
    if application is not None:
        dict['id'] = id
        dict['Server'] = server
        dict['Application'] = application
        dict['Version'] = version
        dict['Uptime'] = uptime
        dict['Request_Count'] = request_count
        dict['Error_Count'] = error_count
        dict['Success_Count'] = success_count

        data_dump = json.dumps(dict)
        return data_dump
        #print('The name for status_id {} is {}'.format(status_id,name))
        #return name, 200
    else:
        #print('Can not find a name for status id {}'.format(status_id))
        return "Not Found in Dictionary", 404

if __name__ == '__main__':
    app.run(debug=True)

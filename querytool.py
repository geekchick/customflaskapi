import requests
import json

# This is a method to query the REST Api endpoints 
def query_file(server_file):
    # create an empty server's list to hold a dictionary of servers from our response
    server_list = []

    # open the server file
    with open('servers.txt', 'r') as file:
        # read in the file and split each server on a new line
        file_list = file.read().split()
    
    # loop through each server in the list and get the index
    for id, server in enumerate(file_list, start=1):
        # get the id
        server_id = id
        # create a constant url that will change with the server id
        url = f"http://localhost:5000/status/{server_id}"
        # do a get request for each of the server id's and store in a response
        response = requests.get(url)   
        # if the response is ('OK') or 200
        if response.status_code == 200:
            # turn text into a Python dictionary
            dict = json.loads(response.text)
            
            # append the dictionary to the server_list
            server_list.append(dict)

    # open a text file to write and append the output data
    with open("file_output.txt", "a") as writer:
        '''
        This nested for loop below is a little confusing 
        but will try to explain as clearly as possible
        '''

        # Start by getting each item of the server list and compare it to the rows beneath it
        for i in range(0, len(server_list)):
            # provide names for the dictionary values
            app = server_list[i]['Application']
            ver = server_list[i]['Version']
            success = server_list[i]['Success_Count']
            error = server_list[i]['Error_Count']
            # loop through each item in the list starting with the row below the one being compared
            for j in range(i + 1, len(server_list)):
                # if the Application and Version are the same
                if app == server_list[j]['Application'] and ver == server_list[j]['Version']:
                    # then aggregate the data; get new total for the success and errors
                    success += server_list[j]['Success_Count']
                    error += server_list[j]['Error_Count']
            # calculate the success rate
            success_rate = success/(success + error)
            # reset the success and error values to 0
            success = 0
            error = 0
            # write the output to a file
            writer.write(f"Your application {app} with version {ver} has a success rate of {success_rate:.2f}\n")
            # print the output to the console
            print(f"Your application {app} with version {ver} has a success rate of {success_rate:.2f}")


query_file('servers.txt')
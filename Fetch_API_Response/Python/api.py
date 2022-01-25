# importing request to get the api
# 'pip install requests' command has to be used in the terminal or cmd
import requests

response = requests.get('https://gorest.co.in/public/v1/users')

# printing the status code of the response
print(response.status_code)

# printing the json response in the terminal
# command for printing the response in the terminal type 'python api.py'
print(response.json())
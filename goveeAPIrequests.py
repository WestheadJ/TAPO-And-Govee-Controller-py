# imports

# import requests module
import requests
# import 'configs.py' file for configuration variables
import configs
# import json module
import json

# setting API request headers, with the API key and the content type being json
request_headers = {'Govee-API-Key':configs.apiKey(),"Content-Type" : "application/json" }

# function for getting the device information
def getDevices():
    # sending a GET request to the API end-point to get the device information with the headers
    response = requests.get('https://developer-api.govee.com/v1/devices',headers=request_headers)
    print(response.content)

# function to turning the device on
def turnOn():
    # creating the request body
    body = {
        # device MAC address found in the device info under device
        "device": configs.deviceMac(),
        # the model number found in the device info under model
        "model":configs.modelNum(),
        # the command that you want the request to do
        "cmd":{
            # name of the command, commands, these values are explained in the documentation
            "name":"turn"
            # the value of the command, these values are explained in the documentation
            ,"value": "on"}
    }
    # sending a PUT request to the API end-point to control the device, adding the body and the headers
    response = requests.put("https://developer-api.govee.com/v1/devices/control", data=json.dumps(body),headers=request_headers)
    print(response.text)

# function to turning the device off
def turnOff():
    # creating the request body
    body = {
        # device MAC address found in the device info under device
        "device": configs.deviceMac(),
        # the model number found in the device info under model
        "model": configs.modelNum(),
        # the command that you want the request to do
        "cmd": {
            # name of the command, commands, these values are explained in the documentation
            "name": "turn",
            # the value of the command, these values are explained in the documentation
            "value": "off"}
    }
    # sending a PUT request to the API end-point to control the device, adding the body and the headers
    response = requests.put(" https://developer-api.govee.com/v1/devices/control", headers=request_headers, data=json.dumps(body))
    print(response.text)
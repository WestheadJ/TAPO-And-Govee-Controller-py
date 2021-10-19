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

def change_colour(colour):

        # getting the rgb value of the hex value
        rgb = hex_to_rgb(colour)

        #laying out easy to follow vairables for the RGB values
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]

        print(r, g, b)

        # creating the request body
        body = {
            # device MAC address found in the device info under device
            "device": configs.deviceMac(),
            # the model number found in the device info under model
            "model": configs.modelNum(),
            # the command that you want the request to do
            "cmd": {
                # name of the command, commands, these values are explained in the documentation
                "name": "color",
                # the value of the command, these values are explained in the documentation
                "value": {"r": r, "g": g, "b": b}}

        }
        # sending a PUT request to the API end-point to control the device, adding the body and the headers
        response = requests.put(" https://developer-api.govee.com/v1/devices/control", headers=request_headers,
                                data=json.dumps(body))

# returns (red, green, blue) for the color given as #rrggbb
def hex_to_rgb(value):
    # strips the first letter
    value = value.lstrip('#')
    # gets the length of the new value
    lv = len(value)
    # returns a tuple converting each hexadecimal number in the hex colour into a decimal number
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
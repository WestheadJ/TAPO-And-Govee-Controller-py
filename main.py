# imports

# import tapo python module
from PyP100 import PyP100
# import flask,template rendering and redirects
from flask import Flask,render_template,redirect
# import the file 'goveeAPIrequests.py' to interact with the govee API
import goveeAPIrequests as api

# initiate the flask
app = Flask(__name__)

# tapo Login
bulb = PyP100.P100("IP","example@email.com","password")

# create a handshake with the bulb for interaction
bulb.handshake()
# use the credentials for login
bulb.login()

#creates a URL route of 'http://localhost:9000/'
@app.route("/")
# when this URL is requested from the browser it calls this function
def index():
    # gets the device information for device status returns a dictioanry
    info = bulb.getDeviceInfo()
    print(info)
    # gets the brightness out of the returns a dictionary
    brightness=info['result']['brightness']
    # gets if the device is overheated returns as an integer
    overheated = info["result"]["overheated"]
    # gets the device state it returns as a boolean
    device_state = info["result"]["device_on"]

    # for data representation if the light is off return the brightness as 0, as it's not outputting light
    # compares the boolean if it is false brightness is returned as 0
    if device_state == False:
        brightness = 0
    # compares the boolean if it is true set the brightness as the devices current brightness
    if device_state == True:
        brightness = brightness

    # returns the HTML file 'index.html', parameters that are used in the HTML
    return render_template("index.html",heated=overheated,deviceState=device_state,brightness=brightness)

# creates a URL route of 'http://localhost:9000/on_tapo'
@app.route("/on_tapo")
# when this URL is requested from the browser it calls this function
def on_tapo():
    # gets the device information for device status returns a dictionary
    # this is for seeing if the bulb is off so there is no error
    info = bulb.getDeviceInfo()
    # gets the device state it returns as a boolean
    device_state = info["result"]["device_on"]
    # compares the boolean if it is True and returns nothing
    if device_state == True:
        pass
    # if it's not true then then it turns the device on using the modules function
    else:
        bulb.turnOn()
    # redirects the user to the URL of 'http://localhost:9000/'
    return redirect("/")

# creates a URL route of 'http://localhost:9000/off_tapo'
@app.route("/off_tapo")
# when this URL is requested from the browser it calls this function
def off_tapo():
    # gets the device information for device status returns a dictionary
    # this is for seeing if the bulb is off so there is no error
    info = bulb.getDeviceInfo()
    # gets the device state, returned as a boolean
    device_state = info["result"]["device_on"]
    # compares the boolean if it is False and returns nothing
    if device_state == False:
        pass
    # if it's not true then then it turns the device off using the modules function
    else:
        bulb.turnOff()
    # redirects the user to the URL of 'http://localhost:9000/'
    return redirect("/")

# creates a URL route of 'http://localhost:9000/up_tapo'
@app.route("/up_tapo")
# when this URL is requested from the browser it calls this function
def up_tapo():
    # gets the device information for device status returns a dictionary
    # this is for seeing if the devices brightness
    info = bulb.getDeviceInfo()
    # gets the devices brightness, returned as an integer
    brightness=info['result']['brightness']
    # compares the brightness if the bulb is already at 100 then return nothing
    if brightness >= 100:
        pass
    # if the brightness isn't greater than 100, add 10 to the brightness and set it as the brightness using the modules function
    else:
        brightness += 10
        bulb.setBrightness(brightness)
    # redirects the user to the URL of 'http://localhost:9000/'
    return redirect("/")

# creates a URL route of 'http://localhost:9000/off_tapo'
@app.route("/down_tapo")
# when this URL is requested from the browser it calls this function
def down_tapo():
    # gets the device information for device status returns a dictionary
    # this is for seeing if the devices brightness
    info = bulb.getDeviceInfo()
    # gets the devices brightness, returned as an integer
    brightness=info['result']['brightness']
    # compares the brightness if the bulb is already at 0 then return nothing
    if brightness <= 10:
        pass
    else:
        # if the brightness isn't greater than 0, subtract 10 to the brightness and set it as the brightness using the modules function
        brightness -= 10
        bulb.setBrightness(brightness)
    # redirects the user to the URL of 'http://localhost:9000/'
    return redirect("/")

# creates a URL route of 'http://localhost:9000/on_govee'
@app.route("/on_govee")
# when this URL is requested from the browser it calls this function
def on_govee():
    # turns the device on with the api function
    api.turnOn()
    # redirects the user to the URL of 'http://localhost:9000/'
    return redirect("/")

# creates a URL route of 'http://localhost:9000/off_govee'
@app.route("/off_govee")
# when this URL is requested from the browser it calls this function
def off_govee():
    # turns the device on with the api function
    api.turnOff()
    # redirects the user to the URL of 'http://localhost:9000/'
    return redirect("/")

# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application on the network on port 9000
    app.run(host="0.0.0.0",port=9000)

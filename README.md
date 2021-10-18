# TAPO-And-Govee-Controller
I made this so I can control my Tapo L510 light bulb and Govee H6159 light strip using 
the PyP100 module and the Govee public API

# How it works
A flask server is set up, the flask sever runs locally on the network on port ```9000```,
your device is found by it's IP which you will need to find out what this is through 
the [Tapo App](https://apps.apple.com/gb/app/tp-link-tapo/id1472718009) then it creates a
handshake between the device and the server, then the server tries to create a login
to the device and the devices to allow communication. Then on the main url ```/```
the index.html file is rendered where a user can access buttons to carry out the functions.
For example the turn on tapo light bulb button goes to url end point ```/on_tapo``` it will
the function attached to the endpoint ```def on_tapo()```

# How to set up to use your devices
Check [PyP100](https://pypi.org/project/PyP100/) compatability and the Govee API compatiblity
when getting you govee API
1. Clone repository 
2. Get IP address of tapo device and login information and swap it out in the ```main.py```
file under ```bulb =``` 
3. Get an API key from Govee, you can do this by getting the 
[Govee App](https://www.govee.com/govee-home)
My Profile -> Settings -> About Us -> Apply for API Key
4. Apply this in ```configs.py``` under ```def apiKey()```
5. Create a virtual environment by having ```vitualenv``` installed and run 
```source venv/bin/activate``` in the main directory
6. run ```python3 main.py``` or ```python main.py```

# Debugging
If when cloning the repositry and can't actiavte the virtual environment create a new one by
running ```virtualenve <directory_name>``` and install the necessary modules:

```requests``` 

```PyP100```

2. If devices have no power provided to them for example a bulb is turned off at the light
switch the seerver will not power up, I cannot add a ```try``` and ```except``` statement as the
```PyP100``` module throws an exception when it can't connect and the server does not start.

# Errors not stated
Create an issue on the repository and I will try to fix it

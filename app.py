from flask import Flask, jsonify, request
from datetime import datetime
import os
import paho.mqtt.client as mqtt


app = Flask(__name__)

# Get port from environment variable or choose 9099 as local default
port = int(os.getenv("PORT", 9099))

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("light")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


 




#Main App Route (First function run when site is accessed)
@app.route('/')

def main():
    name = request.args.get("command")
    action = request.args.get("info")

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message



    client.connect("broker.mqttdashboard.com") 

    
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
    client.loop_forever()
    

   





if __name__ == '__main__':
    # Run the app, listening on all IPs with our chosen port number
    app.run(host='0.0.0.0', port=port)





from flask import Flask, jsonify, request
from datetime import datetime
import os
import paho.mqtt.client as mqtt

app = Flask(__name__)

# Get port from environment variable or choose 9099 as local default
port = int(os.getenv("PORT", 9099))

client = None
message = None
action = None
name = None


def connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe('light')

def inmessage(client,userdata,msg):
    print(msg.topic+" "+str(msg.payload))
    message = str(msg.payload)
        

def networking_init():

    global client
    client = mqtt.Client('homeTest')
    client.on_connect = connect
    client.on_message = inmessage

    client.connect('broker.mqttdashboard.com')
    

    

@app.route('/')
def main():

    networking_init()
    global name, action
    name = request.args.get("name")
    action = request.args.get("action")


    print(name)
    if(action != ""):
        client.publish('light',name)
        client.loop()
        return 'command done'
    else:
        return message



if __name__ == '__main__':
    # Run the app, listening on all IPs with our chosen port number
    app.run(host='0.0.0.0', port=port)




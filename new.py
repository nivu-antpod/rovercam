import paho.mqtt.client as mqtt
import csv
import json
from datetime import datetime



now = datetime.now()
dt_string = now.strftime("%d-%m-%Y-%H-%M-%S")


data_file = open('data_file' + str(dt_string) + '.csv', 'w')
csv_writer = csv.writer(data_file)
count = 0

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    data = json.loads(str(msg.payload))
    sen_data = data['d']
    global count
    if count == 0:
        header = sen_data.keys()
        csv_writer.writerow(header)
        count +=1
    csv_writer.writerow(sen_data.values())

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.43.125", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()

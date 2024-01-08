from flask import Flask, render_template, request,make_response
from flask_restful import Api, Resource
import paho.mqtt.client as mqtt

broker_address = "192.168.65.130"
port = 1883
id = "test3"
topic = f"mst/{id}"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topic)

def on_message(client, userdata, msg):
    data = str(msg.payload)
    print(msg.topic + " " + data)
    # Process received message as needed

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, port, 60)

client.loop_start()  # Start a background thread to handle MQTT events    

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return make_response(render_template("index.html"))
    
class pub(Resource):
    def post(self):
        message = request.form['message']
        client.publish(topic, message)
        return 'Published: ' + message

api.add_resource(HelloWorld, '/')
api.add_resource(pub, '/publish')

if __name__ == '__main__':
    app.run(debug=True,port=5000,host="0.0.0.0",threaded=True)

from flask import Flask, render_template, request,make_response
from flask_restful import Api, Resource
import paho.mqtt.client as mqtt  
from handleMQTT import MQTT
from os import system


system("clear")

broker_address = "192.168.32.130"
port = 1883

t1 = MQTT(broker_address,port)

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return make_response(render_template("index.html"))
    
class pub(Resource):
    def post(self):
        message = request.form['message']
        led = request.form['led']
        if message == "1":
            if led == "1":
                return t1.publish("mst/test1","1")
            elif led =="2":
                return t1.publish("mst/test2","1")
            elif led =="3":
                return t1.publish("mst/test3","1")
        elif message == "0":
            if led == "1":
                return t1.publish("mst/test1","0")
            elif led =="2":
                return t1.publish("mst/test2","0")
            elif led =="3":
                return t1.publish("mst/test3","0")


        return 'Published: ' + message + " "+ led 

api.add_resource(HelloWorld, '/')
api.add_resource(pub, '/publish')

if __name__ == '__main__':
    app.run(debug=True,port=5000,host="0.0.0.0",threaded=True)

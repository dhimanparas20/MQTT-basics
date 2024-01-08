import paho.mqtt.client as mqtt

class MQTT:
    def __init__(self, broker_address, port=1883):
        # self.topic = topic
        self.client = mqtt.Client()
        # self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(broker_address, port, 60)
        self.client.loop_start()  # Start a background thread to handle MQTT events

    def publish(self,topic, message):
        self.client.publish(topic, message)
        self.subscribe(topic)
        return True

    def subscribe(self,topic):
        print(f"Subscriber to {topic}")
        self.client.subscribe(topic)

    def on_message(self, client, userdata, msg):
        data = str(msg.payload)
        print(f"Received message: [{msg.topic}] : {data}")
        # Do something with the received message

    # def on_connect(self, client, userdata, flags, rc):
    #     print(f"Connected with result code {rc}")
    #     self.client.subscribe(self.topic)    



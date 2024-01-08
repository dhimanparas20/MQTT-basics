import paho.mqtt.client as mqtt

class MQTT:  #Class to handle MQTT events
    def __init__(self, BROKER_ADDRESS, port):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        if USE_CREDS == "true":
          self.client.username_pw_set(MQTT_USER, MQTT_PASS)
        self.client.connect(BROKER_ADDRESS, port, 60)
        self.client.loop_start()  # Start a background thread to handle MQTT events

    def on_connect(self, client, userdata, flags, rc):
        if rc==0:
            return True
            # print("connected OK Returned code=",rc)
        else:
            return False
            # print("Bad connection Returned code=",rc)    

    def publish(self,topic, message):   # Publish Topics
        self.client.publish(topic, message)
        self.subscribe(topic)
        return True

    def subscribe(self,topic):  # Subscribe to Topics
        # print(f"Subscribed to: {topic}")
        self.client.subscribe(topic)
        return True

    def unsubscribe(self, topic):
        self.client.unsubscribe(topic)
        return True    



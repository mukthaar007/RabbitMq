import pika

class RabbitMQReceiver:
    def __init__(self, host, queue):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        self.channel = self.connection.channel()
        self.queue = queue

    def call(self, ch, method, properties, body):
        print("with class and objects:", body)

    def subscribing(self):
        self.channel.queue_declare(queue=self.queue)
        self.channel.basic_consume(queue=self.queue, on_message_callback=self.call, auto_ack=True)
        self.channel.start_consuming()

    def close(self):
        self.connection.close()

if __name__ == '__main__':
    rec_obj = RabbitMQReceiver(host='localhost',queue='Telengana')
    rec_obj.subscribing()
    rec_obj.close()


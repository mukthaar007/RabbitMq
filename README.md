import pika

class rabbitmq_sender():
    def __init__(self,exchange,keys,Q1,Q2 ):

        self.connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel=self.connection.channel()

        self.exchange=exchange

        self.keys=keys

        self.Q1=Q1
        self.Q2=Q2

        self.channel.exchange_declare(exchange=exchange,exchange_type='direct')

        self.channel.queue_declare(queue=Q1)
        self.channel.queue_declare(queue=Q2)

        self.channel.queue_bind(exchange=self.exchange,queue=self.Q1,routing_key=self.keys[0])
        self.channel.queue_bind(exchange=self.exchange, queue=self.Q1, routing_key=self.keys[1])

    def publisher(self):
        self.channel.basic_publish(exchange=self.exchange,routing_key=self.keys[1],body='Welcome to the world of AI')

    def close(self):
        self.connection.close()

obj =rabbitmq_sender(exchange='Artificial Intelligence',keys=['m1','m2'],Q1='Telengana',Q2='Kerala')
obj.publisher()
obj.close()
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


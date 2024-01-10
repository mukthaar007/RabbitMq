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

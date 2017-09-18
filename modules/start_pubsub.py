import pika
import threading

def start_pubsub(name, *key, tx, rx):
    def consumeCallBack(ch, method, properties, body):
        print "In ConsumeCallBack"

    # TODO
    credentials = pika.PlainCredentials('guest', 'guest')
    parameters = pika.ConnectionParameters('127.0.0.1', 5672, 'node0', credentials)

    connection = pika.BlockingConnection(parameters)

    print connection

    channel = connection.channel()

    print channel

    channel.exchange_declare('cita', 'topic', 'true')
    channel.queue_declare('consensus', 'true', 'false', 'false', None)

    #TODO, not only one key
    channel.queue_bind('consensus', 'cita', "request")
    channel.queue_bind('consensus', 'cita', "response")

    channel.basic_consume(consumeCallBack, queue='consensus')

    print "[*] Waiting for messages. To exit press CTRL+C"

    #Subscrible Thread
    def subscribeThreadFun():
        print "In Subscribe Tread"
        channel.start_consuming()

    subscribeThread = threading.Thread(target=subscribeThreadFun, args="")
    subscribeThread.start()

    channel.exchange_declare('cita', 'topic', 'true')
    channel.queue_declare('consensus', 'true', 'false', 'false', None)

    def publishThreadFun():
        while True:
            channel.basic_publish(exchange='cita',
                    routing_key='hello2',
                    body='Hello World!',
                    properties=pika.BasicProperties(
                        delivery_mode=2,  # make message persistent
                        )
                    )

    publishThread = threading.Thread(target=publishThreadFun, args="")
    publishThread.start()

    print "it's OK"

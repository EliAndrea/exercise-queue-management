"""
update this file to implement the following already declared methods:
- enqueue: Should add a member to the list
- dequeue: Should remove and return an element from the top or the bottom of the list (depending on the list mode: FIFO or LIFO)
- get_all: should return the entire list as it is
- size: Should return the total size of the list
"""
from twilio.rest import Client

class Queue:

    def __init__(self, mode='FIFO'):
        self._queue = []
        # depending on the _mode, the queue has to behave like a FIFO or LIFO
        self._mode = mode

    def test_message(self, message):
        return print(message)

    def enqueue(self, item):
        if self._mode == 'FIFO':
            self._queue.append(item)
        else:
            self._queue.insert(0, item)
        pass

    def dequeue(self):
        user = self._queue.pop(0)
        return user

    def get_all(self):
        return self._queue

    def size(self):
        return len(self._queue)

    def send_message(self, phone, sms):
        account_sid = 'ACbecb5dc9bd4fd5e960a810f64e1ff3eb'
        auth_token = 'ae002bc14e3dc7dc867edfea4dea548a'
        client = Client(account_sid, auth_token)
        message = client.messages \
                        .create(
                            body= sms,
                            from_='+12063508511',
                            to= phone
                            )
        print("mensaje enviado")

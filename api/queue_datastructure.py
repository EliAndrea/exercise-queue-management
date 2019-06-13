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

#add account_sid, auth token, and trial number of Twillio Account

    def send_message(self, phone, sms):
        account_sid = ''
        auth_token = ''
        client = Client(account_sid, auth_token)
        message = client.messages \
                        .create(
                            body= sms,
                            from_='', #trial number of Twillio
                            to= phone
                            )
        print("mensaje enviado")

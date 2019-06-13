from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from api.queue_datastructure import Queue
import json

queue = Queue(mode='FIFO')


class QueueView(APIView):
    def get(self, request):
        if queue.size() > 0:
            user = queue.dequeue()
            name = user["name"]
            result = "Se está atendiendo a " + name
            sms = "Es tú turno"
            queue.test_message(sms)
            queue.send_message(user["phone"], sms)
        else:
            result = "La cola está vacia"
        return Response(result, status=status.HTTP_200_OK)

    def post(self, request):
        new_user = json.loads(request.body)
        queue.enqueue(new_user)
        result = "Nuevo usuario agregado"
        size_queue = str(queue.size()-1)
        if size_queue == 1:
            sms = "Hay " + size_queue + " persona antes que tú"
        else:
            sms = "Hay " + size_queue + " personas antes que tú"
        queue.test_message(sms)
        queue.send_message(new_user["phone"], sms)
        return Response(result, status=status.HTTP_200_OK)

class QueueAllView(APIView):
    def get(self, request):
        # respond a json with all the queue items
        all_queue = queue.get_all()
        result = json.dumps(all_queue)
        return Response(result, status=status.HTTP_200_OK)
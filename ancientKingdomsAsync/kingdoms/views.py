from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import json
import time
import random
import requests

from concurrent import futures

CALLBACK_URL = "http://0.0.0.0:8000/async/application"

executor = futures.ThreadPoolExecutor(max_workers=1)

def get_random_check():  
  num = random.randrange(1, 11)
  if 1 <= num <= 4:
    return True
  elif 5 <= num <= 8:
    return False
  
  return 'skip'


def get_random_status(pk):
  time.sleep(5)
  return {
    "Id": pk,
    "Check": get_random_check(),
  }


def status_callback(task):
  try:
    result = task.result()
  except futures._base.CancelledError:
    return
  
  id = int(result["Id"])
  check = result["Check"]

  print(id, check)

  if check == 'skip':
    return
  
  nurl = str(CALLBACK_URL)
  headers = {
    'AsyncKey': 'secret',
    'Content-Type': 'application/json',
  }
  answer = {
    "Id": id,
    "Check": check,
  }

  requests.put(nurl, data=json.dumps(answer), headers=headers, timeout=10)


@api_view(['POST'])
def set_status(request):

  if "Id" in request.data.keys():   
    id = request.data["Id"]

    task = executor.submit(get_random_status, id)
    task.add_done_callback(status_callback)        
    return Response(status=status.HTTP_200_OK)
  
  return Response(status=status.HTTP_400_BAD_REQUEST)
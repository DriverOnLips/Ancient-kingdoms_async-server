from django.http import JsonResponse, HttpResponse
# from kingdoms.asyncProcessing.task import get_random_number

def generate_random_number(request):
   return HttpResponse("Hello world!!!")
    # # Получите параметры min_value и max_value из запроса
    # min_value = int(request.GET.get('min_value', 0))
    # max_value = int(request.GET.get('max_value', 100))

    # # Запустите задачу Celery для получения случайного числа
    # task = get_random_number.delay(min_value, max_value)
    # return JsonResponse({'task_id': task.id})

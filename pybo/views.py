from django.http import HttpResponse


def index(request):
    return HttpResponse("곽진선은 몽총이다.")
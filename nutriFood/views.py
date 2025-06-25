from django.http import HttpResponse


def index(request):
    return HttpResponse("Hey ! tu es sur l'index de l'application search du projet NutriFood.")
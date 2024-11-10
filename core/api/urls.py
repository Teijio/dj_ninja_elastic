from django.http import HttpRequest
from django.urls import path

from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/ping")
def ping(request: HttpRequest):
    return {"result": True}


urlpatterns = [path("api/", api.urls)]

from django.contrib import admin
from django.http import HttpResponse
from django.urls import path,include

def home(request):
    return HttpResponse("Home Page")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("base.urls"))
]

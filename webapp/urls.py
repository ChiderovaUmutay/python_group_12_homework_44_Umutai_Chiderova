from django.urls import path

from views.main import handle

urlpatterns = [
    path('', handle),
    path('post/', handle),
]
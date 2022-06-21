from django.urls import path

from webapp.views.main import handle

urlpatterns = [
    path('', handle),
    path('post/', handle),
]
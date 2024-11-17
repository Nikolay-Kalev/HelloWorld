from django.urls import path

from test_project.greetings import views

urlpatterns = [
    path('', views.hello)
]
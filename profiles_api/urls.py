from profiles_api import views
from django.urls import path, include

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]
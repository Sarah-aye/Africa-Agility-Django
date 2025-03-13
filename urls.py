from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('', views.todos, name="todos"),
]

# those lines were created by me
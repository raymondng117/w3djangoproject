# This urls.py only set routes for /members/<..>

from django.urls import path
from . import views

urlpatterns = [
    # Index page is "", not "/"
    path("", views.main, name="main"),

    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
]
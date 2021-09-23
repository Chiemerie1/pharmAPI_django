from django.urls import path, include
from . import views
from .views import StringView





urlpatterns = [
    path("", StringView.as_view(), name="test"),
]

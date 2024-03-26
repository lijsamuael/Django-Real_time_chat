from django.urls import path
from .views import SignInView

urlpatterns = [
    path('signin/', SignInView.as_view())
]

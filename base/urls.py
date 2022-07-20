# from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path
from . import views

urlpatterns = [
    # Login
    path('login', views.MyTokenObtainPairView.as_view()),
    # Register
    path('reg', views.registration),
    # Add book
    path('addbook', views.addBook),
    # User's only books
    path('ubooks', views.userbooks)
]

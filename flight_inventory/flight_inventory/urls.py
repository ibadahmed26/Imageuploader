from django.contrib import admin
from django.urls import path
from flight import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/signup/', views.Signup.as_view(), name='signup'),
]

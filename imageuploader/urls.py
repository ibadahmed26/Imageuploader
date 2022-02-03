from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from imageapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', views.home, name='dashboard'),
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.userlogin, name='login'),
    path('logout/', views.userlogout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


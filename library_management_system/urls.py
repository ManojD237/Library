from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from students import urls
from books import urls
from library import urls
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    path('books/', include('books.urls')),
    path('library/', include('library.urls')),
    path('set_session/', views.set_session, name='set_session'),
    path('get_session/', views.get_session, name='get_session'),
    path('check_session/', views.check_session, name='check_session'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

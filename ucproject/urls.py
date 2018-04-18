
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import Jobs.views
import Salwar.views 	


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Jobs.views.home, name='home'),
    path('salwar/',Salwar.views.salwar, name='salwar'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

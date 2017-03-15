from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^app/', include('app.urls')),
    url(r'^admin/', admin.site.urls),

] + static(settings.STATIC_URL, document_root=settings.STATIC_DIR)

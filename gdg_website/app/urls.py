from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^team/(?P<id>[0-9]+)$',views.team,name='team'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




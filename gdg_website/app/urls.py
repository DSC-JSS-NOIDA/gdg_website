from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^team/$', views.team, name='team'),
    url(r'^event/$', views.event, name='event'),
	url(r'^event_detail/(?P<id>[0-9]+)$',views.event_detail,name='event_detail'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from menu.views import dynamic_view

urlpatterns = [
    re_path(r'^(?P<menu_name>[^/]+)/(?P<path>.*)$', dynamic_view, name='dynamic_view'),
    re_path(r'^(?P<menu_name>[^/]+)/$', dynamic_view, name='dynamic_view_root'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

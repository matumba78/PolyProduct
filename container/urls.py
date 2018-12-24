from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
    # Examples:
    # url(r'^$', 'container.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^extra/',include('extra.urls')),
    url('register/', include('django.contrib.auth.urls')),
    url('', TemplateView.as_view(template_name='home.html'), name='home'),
]

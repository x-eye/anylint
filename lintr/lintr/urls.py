from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
# import apps

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lintr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^repos/', include('apps.repos.urls')),

    url(r'^$', 'lintr.views.index', name='index')
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

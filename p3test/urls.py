from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'p3test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'baaaad.views.hello_from_python_3', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)

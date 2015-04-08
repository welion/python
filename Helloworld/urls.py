from django.conf.urls import patterns, include, url
from django.contrib import admin
from Helloworld.views import Hello

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Helloworld.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$',Hello),
)

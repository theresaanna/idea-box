from django.conf.urls import patterns, include, url
from django.contrib import admin
from ideabox import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ideabox.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

if 'idea' in settings.INSTALLED_APPS and \
        'django.contrib.comments' in settings.INSTALLED_APPS:
    urlpatterns.append(url(r'^comments/',
        include('django.contrib.comments.urls')))
    urlpatterns.append(url(r'^idea/', include('idea.urls', namespace='idea')))


from django.contrib import admin
from django.urls import path , include
from. import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from articles import views as article_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',views.aboutpage),
    path('articles/',include('articles.urls')),
    path('accounts/',include('accounts.urls')),
    path('',article_views.article_list,name="home"),
    path('movies/',views.movie,name='movie'),
    path('articleapi/',views.articleapi,name="articlesapi")
]

urlpatterns+= staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

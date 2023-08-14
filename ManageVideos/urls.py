
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home,name="home"),
    path('Documentation',views.Docs,name="Docs"),
    path('uploadvideo',views.UploadVideo,name="UploadVideo"),
    path('edit/<slug:slug>',views.EditSubs,name="EditSubs"),
     path('register/',views.register,name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

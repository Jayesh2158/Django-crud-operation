from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
#from django.conf.urls.defaults import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('delete/<list_id>',views.delete,name='delete'),
    path('cross_off/<list_id>',views.cross_off,name='cross_off'),
    path('uncross/<list_id>',views.uncross,name='uncross'),
    path('edit/<list_id>',views.edit,name='edit'),
    path('additem/',views.addItem,name='additem'),
    #path('sign_up/',views.adduser,name='adduser'),
    path('reset/<tokenId>',views.reset,name='reset'),
    path('forgot/',views.forgot,name='forgot'),
    path('error404/',views.error404,name='error404'),
    path('',views.Login,name='login'),
    path('success/',views.Sucess,name='success'),
    path('profile/',views.profile,name='profile'),
    path("register/", views.register_request, name="register"),
    path("profile/", views.profileView, name="profile")
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('home/', views.home),
    path('about/', views.about),
    path('doctors/', views.doctors),
    path('blog/', views.blog),
    path('contact/', views.contact),
    path('login/', views.login),
    path('logout/', views.logout),
    path('logincode/', views.logincode),
    path('registercode/', views.registercode),
    path('user/', views.user),
    path('admin1/', views.admin1),
    path('addblood/', views.addblood),
    path('addbloodcode/', views.addbloodcode),
    path('showblood/', views.showblood),
    path('deleteblood/<int:pk>/', views.deleteblood, name="deleteblood"),
    path('addcamp/', views.addcamp),
    path('addcampcode/', views.addcampcode),
    path('showcamp/', views.showcamp),
    path('deletecamp/<int:pk>/', views.deletecamp, name="deletecamp"),
    path('showuser/', views.showuser),
    path('u_showblood/', views.u_showblood),
    path('bloodrequest/', views.bloodrequest),
    path('myrequest/', views.myrequest),
    path('deletemyrequest/<int:pk>/', views.deletemyrequest, name="deletemyrequest"),
    path('u_showcamp/', views.u_showcamp),
    path('changepwd/', views.changepwd),
    path('mypassword/', views.mypassword),
    path('showrequest/', views.showrequest),
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

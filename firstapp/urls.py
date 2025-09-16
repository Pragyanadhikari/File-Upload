from django.contrib import admin
from django.urls import path
from firstapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.upload_file_view,name='upload_file'),
    
]


from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns=[
    path('admin/',admin.site.urls),
    path('POWER/',views.power, name="POWER"),
    path('',views.power,name="POWERROOT")
]

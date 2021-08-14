from django.contrib import admin
from django.urls import path
from .views import home , product_detil

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('<str:name_categorey>/',home,name="name_categorey"),

    path('<int:product_choice>',product_detil,name="product_choice"),
]

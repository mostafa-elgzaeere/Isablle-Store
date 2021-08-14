from django.contrib import admin
from .models import Categorie, Comment ,Product
# Register your models here.


admin.site.register(Categorie)
admin.site.register(Product)
admin.site.register(Comment)
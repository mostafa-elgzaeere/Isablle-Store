from django.db.models import *
from autoslug import AutoSlugField
from django.contrib.auth.models import User

# Create your models here.


class Categorie(Model):
    name=CharField(max_length=70)
    slug = AutoSlugField(populate_from='name' ,default=" ")


    def __str__(self):
        return self.name




class Product(Model):
    title=CharField(max_length=100)
    description=CharField(max_length=300)
    active=BooleanField(default=True)
    price=DecimalField(max_digits=5,decimal_places=2)
    image = ImageField(upload_to="static\img", height_field=None, width_field=None, max_length=None)    

    categorey=ForeignKey(Categorie,on_delete=CASCADE,related_name="products")

    

    def __str__(self):
        return self.title


    




class Comment(Model):
    writer     = ForeignKey(User, on_delete=CASCADE , related_name="comments")
    title      = CharField(max_length=50,null=True,default="")
    content    = TextField(max_length=400)
    product    = ForeignKey(Product,on_delete=CASCADE , related_name="comments")

    def __str__(self):
        return f" {self.writer} is commented at {self.product} "



    




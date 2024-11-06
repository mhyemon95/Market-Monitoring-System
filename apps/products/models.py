from django.db import models
from apps.Users.models import User
import uuid
from django_resized import ResizedImageField

# Create your models here.

class product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length = 225 )
    image = ResizedImageField(upload_to="blog/cover/", default="blog/cover/default.jpg")
    price = models.IntegerField(null=True, blank=True)
    product_description = models.TextField(blank=True, max_length=500)
    location = models.CharField(max_length=225)
    seller = models.CharField(max_length= 100, blank=True,max_length=225)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now = True)
    published_at = models.DateTimeField(default = False)
    catagory = models.CharField(max_length = 225)
    
    def __str__(self) -> str:
        return super().__str__()
    


# from django.db import models
# from apps.manage_user.models import User
# import uuid

# class BlogPost(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     title = models.CharField(max_length=255)
#     content = CKEditor5Field(config_name="extends")
#     image = ResizedImageField(upload_to="blog/cover/", default="blog/cover/default.jpg")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     published_at = models.DateTimeField(null=True, blank=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     is_published = models.BooleanField(default=False)

#     def _str_(self):
#         return self.title
from django.contrib import admin
#blog/models.pyからPostをimportした
from .models import Post

# Register your models here.
admin.site.register(Post)
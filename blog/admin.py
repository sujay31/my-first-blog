#new code written after deletion of the previous
#lines starting with 'from' or 'import' are used to copy a portion from other files
from django.contrib import admin
from .models import Post

admin.site.register(Post) #to make the model visible on the admin page it is registered at admin.site.register(Post)'
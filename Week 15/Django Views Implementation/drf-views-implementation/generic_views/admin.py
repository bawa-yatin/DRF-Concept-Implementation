from django.contrib import admin
from .models import GenericArticle, GenericAuthor

# Register your models here.
admin.site.register(GenericArticle)
admin.site.register(GenericAuthor)


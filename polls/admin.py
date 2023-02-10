from django.contrib import admin
from .models import Question

# Register your models here.
admin.site.site_header = "后台登录界面"
admin.site.register(Question)

from django.contrib import admin

# Register your models here.
from .models import User, Organisation

# Register your models here.
admin.site.register(User)
admin.site.register(Organisation)

from django.contrib import admin

from ads.models import User, Category, Ad
from users.models import Location

# Register your models here.
admin.site.register(Location)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Ad)
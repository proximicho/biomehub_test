from django.contrib import admin

# Register your models here.


from .models import post, about, contact

admin.site.register(post)
admin.site.register(about)
admin.site.register(contact)

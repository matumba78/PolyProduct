from django.contrib import admin
from .models import User,CT,CTInstance,ExtraField,Extrafield_values,Relationship
# Register your models here.
admin.site.register(CT)
admin.site.register(User)
admin.site.register(ExtraField)
admin.site.register(Extrafield_values)
admin.site.register(CTInstance)
admin.site.register(Relationship)


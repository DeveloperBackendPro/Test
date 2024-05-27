from django.contrib import admin
from home.models import *

class TestAdmin(admin.ModelAdmin):
    list_display = ['questions', 'category', 'status',]
    search_fields = ('questions',)
    list_editable = ('status',)

admin.site.register(Test, TestAdmin)
admin.site.register(Category)
admin.site.register(Student)

from django.contrib import admin
from .models import article


class admin_post(admin.ModelAdmin):
    list_display = (
        'Name', 'Company', 'Website', 'Linkedin', 'Email', 'Photo', 'Text', 'Created_on', 'Update_on', 'Status',
        'Author')
    list_filter = ("Status", "Author")
    search_fields = ['Name', 'Company']
    prepopulated_fields = {'Company':('Name',)}


admin.site.register(article, admin_post)

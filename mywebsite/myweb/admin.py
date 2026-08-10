from django.contrib import admin
from myweb.models import login


#this is the admin panel for the login model created in models.py file. It will show the username, email, college_id and phone number of the user in the admin panel.
class LoginAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'college_id', 'phone')

admin.site.register(login, LoginAdmin)
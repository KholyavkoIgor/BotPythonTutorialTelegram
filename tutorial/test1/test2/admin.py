from django.contrib import admin

# Register your models here.
from .forms import ProfileForm
from .models import Profile
from .models import Message

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'external_id', 'name')
    form = ProfileForm

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'text', 'textrus','texteng','lecturename' ,'created_at')

    #def get_queryset(self, request):
      #  return

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

# For both new forms we are setting the model to our CustomUser and
# using the default fields via Meta.fields which includes '''all''' default fields.
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        # the default setting for fields on UserCreationForm is just
        '''username, email, and password '''
        # even though there are many more fields available
        fields = UserCreationForm.Meta.fields + ('age',)
        # To add custom age field we simply tack it on at the end
        # and it will display automatically on our future sign up page

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

# only other step we need is to update our admin.py file since Admin is
# tightly coupled to the default User model.

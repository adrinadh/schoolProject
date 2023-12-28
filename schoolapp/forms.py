from django import forms
from .models import UserInfo


class UserInfoForm(forms.ModelForm):
    dob = forms.DateField(input_formats=['%d-%m-%Y'])

    class Meta:
        model = UserInfo
        fields = '__all__'

        # widgets = {
        #     'address': forms.TextInput(),  # Use TextInput for a single-line input
        # }

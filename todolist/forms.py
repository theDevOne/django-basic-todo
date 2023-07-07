from django import forms
from .models import TodoItem
from django.contrib.auth import get_user_model

User = get_user_model()

class TodoItemForm(forms.ModelForm):

    class Meta:
        model = TodoItem
        fields = ['name', 'description', 'completed']


class UserRegisterForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Enter Password",
            }
        )
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"})
    )

    class Meta:
        model = User
        fields = [ "username", "first_name", "last_name", "email"]

        def clean(self):
            cleaned_data = super(UserRegisterForm, self).clean()
            password = cleaned_data.get("password")
            confirm_password = cleaned_data.get("confirm_password")

            if password != confirm_password:
                raise forms.ValidationError("Password does not match!")

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs["placeholder"] = "Enter First Name"
        self.fields["last_name"].widget.attrs["placeholder"] = "Enter last Name"
        self.fields["username"].widget.attrs["placeholder"] = "Enter username"
        self.fields["email"].widget.attrs["placeholder"] = "Enter email"

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
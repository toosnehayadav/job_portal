from django import forms
from .models import UserProfile
import re
from .models import UserProfile as User

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'email', 'phone_number', 'age', 'address', 'profile_image','password']
        
    # Custom validation for phone_number
    def clean_phone_number(self):
        phone = self.cleaned_data['phone_number']
        if len(phone) < 10:
            raise forms.ValidationError('Phone number must be at least 10 digits.')
        if not phone.isdigit():
            raise forms.ValidationError('Phone number must contain only digits.')
        return phone
    
    # Custom validation for email
    def clean_email(self):
        email = self.cleaned_data['email']
        # You can add more specific checks, for example, checking if the email already exists in the database
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise forms.ValidationError('Enter a valid email address.')
        return email
    
    # Custom validation for age (should be greater than 18)
    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise forms.ValidationError('Age must be greater than or equal to 18.')
        return age
    
    # Custom validation for address (optional, for example, check for non-empty address)
    def clean_address(self):
        address = self.cleaned_data['address']
        if len(address.strip()) == 0:
            raise forms.ValidationError('Address cannot be empty.')
        return address
    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 5:
            raise forms.ValidationError('Password must be at least 6 characters long.')
        return password


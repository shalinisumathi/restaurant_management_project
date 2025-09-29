from rest_framework.response import Response 
from rest_framework.decorators import api_view
from utils.validation_utils import is_valid_email
from django import forms


@api_view(['POST'])
def register_user(request):
    email = request.data.get('email')

    if not is_valid_email(email):
        return Response({"error": "Invalid email address"}, status=400)

    return Response({"message": "User registered successfully"})

class ContactForm(forms.Form):
    email = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)

    def clean_email(self):
        email = self.cleaned_data['email']
        if not is_valid_email(email):
            raise forms.ValidationError("Please enter a valid email address.")
        return email
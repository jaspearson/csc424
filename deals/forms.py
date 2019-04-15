# Used to the functioning Contact Us Page
# -ZT
from django import forms

class ContactForm(forms.Form):

    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea(attrs={"rows":20, "cols":30}))
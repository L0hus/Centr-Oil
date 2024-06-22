from django import forms
from Main.models import Feedback

class FeedBackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'formControl', 'id': 'Name', 'name': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'formControl', 'id': 'Email', 'name': 'Email'}),
            'phone': forms.NumberInput(attrs={'class': 'formControl', 'id': 'Phone', 'name': 'Phone'}),
            'message': forms.Textarea(attrs={'class': 'formControl', 'id': 'Message', 'name': 'Message', 'rows': 5}),
        }
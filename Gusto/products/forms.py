from .models import Reviews
from django import forms

# display specified review fields in a view
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['rating', 'body']
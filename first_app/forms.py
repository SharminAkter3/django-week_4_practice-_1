from django import forms

# Create your forms here.


class ExampleForm(forms.Form):
    name = forms.CharField()

from django import forms
from django.forms.fields import validators



class HeartRateForm(forms.Form):
    systolic = forms.IntegerField(validators=[
        validators.MinValueValidator(0, message="Value might be greater then 0 and less then 240"),
        validators.MaxValueValidator(240, message="Value might be greater then 0 and less then 240")
    ])
    diastolic = forms.IntegerField(validators=[
        validators.MinValueValidator(0, message="Value might be greater then 0 and less then 240"),
        validators.MaxValueValidator(240, message="Value might be greater then 0 and less then 240")
    ])
    pulse = forms.IntegerField(validators=[
        validators.MinValueValidator(0, message="Value might be greater then 0 and less then 240"),
        validators.MaxValueValidator(240, message="Value might be greater then 0 and less then 240")
    ])

    class Meta:
        widgets = {
            'systolic': forms.TextInput(),
            'diastolic': forms.TextInput(),
            'pulse': forms.TextInput()
        }

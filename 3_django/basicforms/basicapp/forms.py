from django import forms
from django.core import validators

#example of custom validator, you would pass it to a field with validators=[chech_for_z]
def check_for_z(value:str):
    if value.lower() != 'z':
        raise forms.ValidationError("Name needs to start with Z")

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='enter email again')
    text = forms.CharField(widget=forms.Textarea())
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput(), validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']
        if email != vemail: raise forms.ValidationError("Emails don't match")

    '''
    This is what the validator in botcatcher is doing now

    def clean_botcatcher(self):
    botcatcher = self.cleaned_data['botcatcher']
    if(len(botcatcher)):
        raise forms.ValidationError("Bot alert")
    '''

    
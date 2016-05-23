from django import forms
from django.forms import ModelForm, Textarea, TextInput, NumberInput
from django.forms.extras import SelectDateWidget
from .models import Project

class ProjectForm(ModelForm):
    name = forms.CharField(widget=Textarea(attrs={'rows':2, 'cols':50}))
    description = forms.CharField(widget=Textarea(attrs={'rows':2, 'cols':45}))
    expiration_date = forms.DateField(widget=SelectDateWidget())
    number_of_users_required = forms.IntegerField(min_value=0, max_value=999, widget=NumberInput(attrs={'style':'text-align:right'}))
    url = forms.CharField(widget=TextInput(attrs={'size':54}))
    class Meta:
        model = Project
        exclude = ('slug','users','skills',)

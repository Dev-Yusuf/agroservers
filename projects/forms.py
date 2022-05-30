from xml.parsers.expat import model
from django.db import models
from django.forms import ModelForm, fields
from django import forms
from .models import Project, Review

class projectForm(ModelForm):
    class Meta:
        model = Project
        fields =['title', 'featured_image', 'description', 'demo_link', 'source_link', 'tags']

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(projectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})



class ReviewForm(ModelForm):
    class Meta: 
        model = Review
        fields = ['value', 'body']

        labels = {
            'value': 'leave a vote',
            'body': 'leave a comment'
        }

#whenever you see this block of code, what it does is that it loops through all the fields and add the style of the class from css

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
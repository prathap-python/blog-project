from django import forms
from blog.models import Comment
class emailsendform(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    to=forms.CharField()
    comments=forms.CharField(required=False,widget=forms.Textarea)
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','email','body')


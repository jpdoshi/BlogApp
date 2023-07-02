from django import forms

class BlogForm(forms.Form):
	title = forms.CharField()
	cover = forms.ImageField()
	body = forms.CharField(widget=forms.Textarea)
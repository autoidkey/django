from django import forms
from .models import Post,My_post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class My_postform(forms.ModelForm):

	class Meta:
		model = My_post
		fields = ('title','text')
'''
class My_trendform(forms.ModelForm):

	class Meta:
		model = My_trend
		fields = ('topic')
'''
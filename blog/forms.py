from django import forms
from .models import *

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class My_postform(forms.ModelForm):

	class Meta:
		model = My_post
		fields = ('title','text')

class My_trendform(forms.ModelForm):

	class Meta:
		model = My_trend
		fields = ('topic',) #謎 なぜか,が必要
		widgets = {
			'topic': forms.TextInput(attrs={'size':6}),
		}

class My_taskform(forms.ModelForm):

	class Meta:
		model = My_task
		fields = ('topic',) #謎 なぜか,が必要
		widgets = {
			'topic': forms.TextInput(attrs={'size':6}),
		}

class My_interestform(forms.ModelForm):

	class Meta:
		model = My_interest
		fields = ('topic',) #謎 なぜか,が必要
		widgets = {
			'topic': forms.TextInput(attrs={'size':6}),
		}
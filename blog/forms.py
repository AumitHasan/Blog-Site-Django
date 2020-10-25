from django import forms
from blog.models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author', 'title', 'text')
    
        # widgets a dictionary attribute inside Meta class to edit default field style
        widgets = {
            'title': forms.TextInput(attrs={'class':'textinputclass'}) ,# attrs is atribute
            'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}) # css classes
            # classes are from Medium Javascript CSS library
            # textinputclass & postcontent are my own class
        }
    

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author': forms.TextInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea'}),
        }







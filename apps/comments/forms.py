from django import forms
from apps.comments.models import Comment


class AddCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text', 'topic']
        widgets = {
            'topic': forms.HiddenInput()
        }

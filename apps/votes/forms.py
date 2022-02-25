from django import forms
from apps.votes.models import Vote


class AddVoteForm(forms.ModelForm):

    class Meta:
        model = Vote
        fields = ['comment']
        widgets = {
            'comment': forms.HiddenInput()
        }

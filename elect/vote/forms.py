from django import forms
from vote.models import NewVote

class VoteForm(forms.ModelForm):
    class Meta:
        model = NewVote
        exclude = ['date_entered']

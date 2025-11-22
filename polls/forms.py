from django import forms


class VoteForm(forms.Form):
    choice = forms.IntegerField(required=True)
    
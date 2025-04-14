from django import forms
from .models import Poll, Choice

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question']
        
class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']
        
ChoiceFormSet = forms.inlineformset_factory(
    Poll, Choice, form=ChoiceForm, extra=2, can_delete=False
)
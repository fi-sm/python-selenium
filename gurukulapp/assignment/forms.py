
from .models import Assignment
from django import forms


class CreateMealForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = [‘name’, ‘date’, ‘members’]
    name = forms.CharField()
    date = forms.DateInput()
    members = forms.ModelMultipleChoiceField(
        queryset=Member.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
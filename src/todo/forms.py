from django import forms


class ToDo(forms.Form):
    line = forms.CharField(max_length=255)

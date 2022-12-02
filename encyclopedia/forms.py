from django import forms


class SearchForm(forms.Form):
    q = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'search',
                                                                      'placeholder': 'Search Encyclopedia',
                                                                      }))


class NewPage(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={"rows": 10, 'class': 'form-control'}))



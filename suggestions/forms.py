from django import forms

from .models import Suggestion


class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ['name', 'address', 'why_wheelchair_friendly', 'additional_information']

    def __init__(self, *args, **kwargs):
        super(SuggestionForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = "Navn"
        self.fields['name'].widget.attrs['autocomplete'] = "off"
        self.fields['address'].widget.attrs['placeholder'] = "Adresse"
        self.fields['address'].widget.attrs['autocomplete'] = "off"
        self.fields['why_wheelchair_friendly'].widget.attrs[
            'placeholder'] = 'Eksempel “Tilpasset trening inkludert med resten av medlemmene uavhengig av mobilitet.”'
        self.fields['additional_information'].widget.attrs[
            'placeholder'] = 'Eksempel “Resepsjonen ikke er i samme etasje som resten av senteret”.'
from django import forms

class SelectForm(forms.Form):
    select_source_one = forms.ChoiceField(label='Select Source', choices=[('tbt_news', 'The Bangladesh Today'), ('tds_news', 'The Daily Star'), ('tna_news', "The New Age")])
    select_source_two = forms.ChoiceField(label='Select Source', choices=[('tbt_news', 'The Bangladesh Today'), ('tds_news', 'The Daily Star'), ('tna_news', "The New Age")])
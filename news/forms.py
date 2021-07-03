from django import forms


class SelectForm(forms.Form):
    select_source_one = forms.ChoiceField(label='Select Source', 
                        widget=forms.Select(attrs={'class': 'form-control', 'name': 'select_0'}),  
                        choices=[('0', '--------select--------'), ('tbt_news', 'The Bangladesh Today'), ('tds_news', 'The Daily Star'), ('tna_news', "The New Age"), ('bd_news', 'BDNews24')],
                        initial=0)
    select_source_two = forms.ChoiceField(label='Select Source', 
                        widget=forms.Select(attrs={'class': 'form-control'}), 
                        choices=[('0', '--------select--------'), ('tbt_news', 'The Bangladesh Today'), ('tds_news', 'The Daily Star'), ('tna_news', "The New Age"), ('bd_news', 'BDNews24')],
                        initial=0)

    
    
    # def __init__(self, *args, **kwargs):
    #     super(SelectForm, self).__init__(*args, **kwargs)
    #     self.fields['select_source_one'].widget.attrs['class'] = 'form-control'
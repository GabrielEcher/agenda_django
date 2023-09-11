from . import models
from django import forms
from django.core.exceptions import ValidationError

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Aqui veio do init',
            }
        ),
        label='Primeiro Nome',
        help_text='Texto de ajuda para seu usuário',
    )
    
    class Meta:
       model = models.Contact
       fields = ('first_name', 'last_name', 'phone',)
       
    #    widgets = {
    #        'first_name': forms.TextInput(
    #            attrs={
    #                'class': 'c',
    #                'placeholder': 'Escreva aqui',
    #            }
    #         )
    #     }
    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            error_msg = ValidationError(
                'Primeiro nome não pode ser igual ao segundo',
                code='invalid'
            )
            
            self.add_error('first_name', error_msg)
            self.add_error('last_name', error_msg)
        
        return super().clean()
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        
        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'NÃO DIGITE ABC NESTE CAMPO',
                    code='invalid'
                )
            )
        return first_name
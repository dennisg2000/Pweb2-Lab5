from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            'nombres',
            'apellidos',
            'edad',
            'donador',
        ]
    def clean_nombres(self,*arg,**kwargs):
        print('paso a la limpieza del campo de nombres')   
        name=self.cleaned_data.get('nombres')
        if name.istitle():
            return name
        else: 
            raise forms.ValidationError('la primara letra en mayuscula')

class RawPersonaForm(forms.Form):
    nombres=forms.CharField(
        widget = forms.Textarea(
            attrs={
                'placeholder' : 'solo ingresa tu nombre',
                'id' : 'nombreID',
                'class' : 'special',
                'cols' : '20',
                'rows' : '5'
            }
        )
    )
    apellidos=forms.CharField()
    edad=forms.IntegerField(initial=20)
    donador=forms.BooleanField()
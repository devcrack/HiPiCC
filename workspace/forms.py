from django import forms
from django.core.exceptions import ValidationError

from .models import DynamicModule, Potential

class PotentialForm(forms.ModelForm):
    # Validaciones del Campo Fracción de Volumen
    def clean_phi(self):
        aux = self.cleaned_data['phi']

        if not(0 < aux < 0.75):
            raise ValidationError('La Fracción de Volumen debe estar entre un valor 0 y 0.75.')
        return aux
    #Validaciones de Campo Temperatura
    def clean_temp(self):
        aux = self.cleaned_data['temp']

        if not(0 < aux <= 1):
            raise ValidationError('La Temperatura debe de estar entre un valor de 0 y 1')
        return aux

    class Meta:
        model = Potential
        fields = ('phi','temp',)
        # widgets = {'temp': forms.HiddenInput()}
        # help_texts = {'phi': 'La Fracción de Volumen debe estar entre un valor 0 y 0.75.'}


class HardSpherePotentialForm(forms.ModelForm):

    def clean_phi(self):
        aux = self.cleaned_data['phi']

        if not(0 < aux < 0.75):
            raise ValidationError('La Fracción de Volumen debe estar entre un valor 0 y 0.75.')
        return aux

    class Meta:
        model = Potential
        fields = ('phi',)

class DynamicModuleForm(forms.ModelForm):

    def clean_phi(self):
        aux = self.cleaned_data['phi']

        if not(0 < aux < 0.75):
            raise ValidationError('La Fracción de Volumen debe estar entre un valor 0 y 0.75.')
        return aux

    class Meta:
        model = DynamicModule
        fields = ('phi',)
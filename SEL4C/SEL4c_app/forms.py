from django import forms
from .models import Modulos
from ckeditor.widgets import CKEditorWidget

class ModulesForm(forms.ModelForm):
    class Meta:
        model = Modulos
        fields = ['titulo_mod', 'instrucciones', 'imagen_mod', 'tipo_multimedia']
        widgets = {
            # importar widget de ckeditor
            'instrucciones': CKEditorWidget(config_name='webEditor'),
        }
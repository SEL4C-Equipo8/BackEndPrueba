from django import forms
from .models import Modulos
from ckeditor.widgets import CKEditorWidget

class ModulesForm(forms.ModelForm):
    class Meta:
        model = Modulos
        fields = ['titulo_mod', 'instrucciones', 'imagen_mod', 'tipo_multimedia']
        #Labels para output de datos
        labels = {
            'titulo_mod': 'Título del módulo',
            'instrucciones': 'Instrucciones',
            'imagen_mod': 'Imagen',
            'tipo_multimedia': 'Tipo de multimedia'
        }
        widgets = {
            # Importar CKEditor
            'instrucciones': CKEditorWidget(config_name='webEditor'),
        }
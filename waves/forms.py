from django.forms import ModelForm

from .models import Wave


class AddWaveForm(ModelForm):
    class Meta:
        model = Wave
        fields = ('content',)


class EditWaveForm(ModelForm):
    class Meta:
        model = Wave
        fields = ('content',)

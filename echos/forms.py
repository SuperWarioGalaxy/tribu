from django.forms import ModelForm

from .models import Echo


class AddEchoForm(ModelForm):
    class Meta:
        model = Echo
        fields = ('content',)


class EditEchoForm(ModelForm):
    class Meta:
        model = Echo
        fields = ('content',)

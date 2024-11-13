from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, render

from echos.models import Echo

from .forms import AddWaveForm, EditWaveForm
from .models import Wave


# Create your views here.
@login_required
def add_wave(request, pk: int):
    if request.method == 'POST':
        if (form := AddWaveForm(request.POST)).is_valid():
            echo = Echo.objects.get(pk=pk)
            wave = form.save(commit=False)
            wave.user = request.user
            wave.echo = echo
            wave.save()
            return redirect(echo)
    else:
        form = AddWaveForm()
    return render(request, 'add_wave.html', dict(form=form, pk=pk))


@login_required
def wave_edit(request, wave_pk: int, echo_pk: int):
    wave = Wave.objects.get(pk=wave_pk)
    if wave.user != request.user:
        raise PermissionDenied
    else:
        if request.method == 'POST':
            if (form := EditWaveForm(request.POST, instance=wave)).is_valid():
                echo = Echo.objects.get(pk=echo_pk)
                wave = form.save(commit=False)
                wave.save()
                return redirect(echo)
        else:
            form = EditWaveForm(instance=wave)
        return render(request, 'edit_wave.html', dict(wave=wave, echo=echo, form=form))


@login_required
def wave_delete(request, pk: int):
    echo = Echo.objects.get(pk=pk)
    if echo.user != request.user:
        raise PermissionDenied
    else:
        Echo.objects.filter(pk=pk).delete()
        echos = Echo.objects.all()
        return render(
            request,
            'list.html',
            {
                'echos': echos,
            },
        )

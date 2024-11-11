from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .forms import AddEchoForm, EditEchoForm
from .models import Echo


# Create your views here.
@login_required
def echos_list(request: HttpRequest) -> HttpResponse:
    echos = Echo.objects.all()
    return render(
        request,
        'list.html',
        {
            'echos': echos,
        },
    )


@login_required
def echo_detail(request: HttpRequest, pk: int) -> HttpResponse:
    echo = Echo.objects.get(pk=pk)
    # waves = echo.waves.all()
    waves = echo.waves.all().order_by('-created_at')[:5]
    more = True
    return render(request, 'detail.html', dict(echo=echo, waves=waves, more=more))


@login_required
def echo_waves(request: HttpRequest, pk: int) -> HttpResponse:
    echo = Echo.objects.get(pk=pk)
    waves = echo.waves.all()
    more = False
    return render(request, 'detail.html', dict(echo=echo, waves=waves, more=more))


@login_required
def add_echo(request):
    if request.method == 'POST':
        if (form := AddEchoForm(request.POST)).is_valid():
            echo = form.save(commit=False)
            echo.user = request.user
            echo.save()
            return redirect('echos:echos-list')
    else:
        form = AddEchoForm()
    return render(request, 'add_echo.html', dict(form=form))


def echo_edit(request, pk: int):
    echo = Echo.objects.get(pk=pk)
    if echo.user != request.user:
        raise PermissionDenied
    else:
        if request.method == 'POST':
            if (form := EditEchoForm(request.POST, instance=echo)).is_valid():
                echo = form.save(commit=False)
                # echo.slug = slugify(task.name)
                echo.save()
                return redirect('echos:echos-list')
        else:
            form = EditEchoForm(instance=echo)
        return render(request, 'edit.html', dict(echo=echo, form=form))


def echo_delete():
    pass

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .forms import AddEchoForm
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
def echos_detail(request: HttpRequest, pk: int) -> HttpResponse:
    echo = Echo.objects.get(pk=pk)
    waves = echo.waves.all()
    return render(request, 'detail.html', dict(echo=echo, waves=waves))


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


def echo_edit():
    pass


def echo_delete():
    pass

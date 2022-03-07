from django.shortcuts import render, redirect
from .models import Madlib
from .forms import MadlibFormA, MadlibFormB, MadlibFormE, MadlibFormF, MadlibFormG, MadlibFormH, MadlibFormI,\
    MadlibFormJ, MadlibFormK, MadlibFormL, MadlibFormO, MadlibFormM, MadlibFormN, MadlibFormC, MadlibFormD


# Create your views here.
def index(request):
    return render(request, 'Madlibs/index.html')


def madlib_a(request, id):
    madlib = Madlib.objects.get(id=id)
    form = MadlibFormA(request.POST or None, instance=madlib)

    if form.is_valid():
        form.save()
        return redirect('Madlibs:a')

    return render(request, 'Madlibs/madlib-form.html', {'form': form, 'madlib': madlib})


def madlib_b(request, id):
    madlib = Madlib.objects.get(id=id)
    form = MadlibFormB(request.POST or None, instance=madlib)

    if form.is_valid():
        form.save()
        return redirect('Madlibs:b')

    return render(request, 'Madlibs/madlib-form.html', {'form': form, 'madlib': madlib})


def madlib_c(request, id):
    madlib = Madlib.objects.get(id=id)
    form = MadlibFormC(request.POST or None, instance=madlib)

    if form.is_valid():
        form.save()
        return redirect('Madlibs:c')

    return render(request, 'Madlibs/madlib-form.html', {'form': form, 'madlib': madlib})


def madlib_d(request, id):
    madlib = Madlib.objects.get(id=id)
    form = MadlibFormD(request.POST or None, instance=madlib)

    if form.is_valid():
        form.save()
        return redirect('Madlibs:d')

    return render(request, 'Madlibs/madlib-form.html', {'form': form, 'madlib': madlib})


def madlib_e(request, id):
    madlib = Madlib.objects.get(id=id)
    form = MadlibFormE(request.POST or None, instance=madlib)

    if form.is_valid():
        form.save()
        return redirect('Madlibs:e')

    return render(request, 'Madlibs/madlib-form.html', {'form': form, 'madlib': madlib})


def madlib_f(request, id):
    madlib = Madlib.objects.get(id=id)
    form = MadlibFormF(request.POST or None, instance=madlib)

    if form.is_valid():
        form.save()
        return redirect('Madlibs:f')

    return render(request, 'Madlibs/madlib-form.html', {'form': form, 'madlib': madlib})


def madlib_g(request, id):
    madlib = Madlib.objects.get(id=id)
    form = MadlibFormG(request.POST or None, instance=madlib)

    if form.is_valid():
        form.save()
        return redirect('Madlibs:g')

    return render(request, 'Madlibs/madlib-form.html', {'form': form, 'madlib': madlib})


def madlib_h(request, id):
    madlib = Madlib.objects.get(id=id)
    form = MadlibFormH(request.POST or None, instance=madlib)

    if form.is_valid():
        form.save()
        return redirect('Madlibs:h')

    return render(request, 'Madlibs/madlib-form.html', {'form': form, 'madlib': madlib})


def madlib_i(request, id):
    madlib = Madlib.objects.get(id=id)
    form = MadlibFormI(request.POST or None, instance=madlib)

    if form.is_valid():
        form.save()
        return redirect('Madlibs:i')

    return render(request, 'Madlibs/madlib-form.html', {'form': form, 'madlib': madlib})


def madlib_j(request, id):
    madlib = Madlib.objects.get(id=id)
    form = MadlibFormJ(request.POST or None, instance=madlib)

    if form.is_valid():
        form.save()
        return redirect('Madlibs:j')

    return render(request, 'Madlibs/madlib-form.html', {'form': form, 'madlib': madlib})


def madlib_k(request, id):
    madlib = Madlib.objects.get(id=id)
    form = MadlibFormK(request.POST or None, instance=madlib)

    if form.is_valid():
        form.save()
        return redirect('Madlibs:k')

    return render(request, 'Madlibs/madlib-form.html', {'form': form, 'madlib': madlib})


def madlib_l(request, id):
    madlib = Madlib.objects.get(id=id)
    form = MadlibFormL(request.POST or None, instance=madlib)

    if form.is_valid():
        form.save()
        return redirect('Madlibs:l')

    return render(request, 'Madlibs/madlib-form.html', {'form': form, 'madlib': madlib})


def madlib_m(request, id):
    madlib = Madlib.objects.get(id=id)
    form = MadlibFormM(request.POST or None, instance=madlib)

    if form.is_valid():
        form.save()
        return redirect('Madlibs:m')

    return render(request, 'Madlibs/madlib-form.html', {'form': form, 'madlib': madlib})


def madlib_n(request, id):
    madlib = Madlib.objects.get(id=id)
    form = MadlibFormN(request.POST or None, instance=madlib)

    if form.is_valid():
        form.save()
        return redirect('Madlibs:n')

    return render(request, 'Madlibs/madlib-form.html', {'form': form, 'madlib': madlib})


def madlib_o(request, id):
    madlib = Madlib.objects.get(id=id)
    form = MadlibFormO(request.POST or None, instance=madlib)

    if form.is_valid():
        form.save()
        return redirect('Madlibs:o')

    return render(request, 'Madlibs/madlib-form.html', {'form': form, 'madlib': madlib})

def madlib(request):
    return render(request, 'Madlibs/madlibs.html')

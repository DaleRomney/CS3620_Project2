from django.shortcuts import render, redirect
from .models import Madlib
from .forms import MadlibFormA, MadlibFormB, MadlibFormE, MadlibFormF, MadlibFormG, MadlibFormH, MadlibFormI,\
    MadlibFormJ, MadlibFormK, MadlibFormL, MadlibFormO, MadlibFormM, MadlibFormN, MadlibFormC, MadlibFormD


# Create your views here.
def index(request):
    return render(request, 'Madlibs/index.html')


def madlib_a(request):
    madlib = Madlib.objects.get(id=1)
    form = MadlibFormA(request.POST or None, instance=madlib)

    if form.is_valid():
        form.save()
        return redirect('Madlibs:a')

    return render(request, 'Madlibs/madlib-form.html', {'form': form, 'madlib': madlib})


def a(request):
    madlib = Madlib.objects.get(id=1)
    context = {
        'madlib': madlib,
    }
    return render(request, 'Madlibs/a.html', context)


def madlib_b(request):
    madlib = Madlib.objects.get(id=2)
    form = MadlibFormB(request.POST or None, instance=madlib)

    if form.is_valid():
        form.save()
        return redirect('Madlibs:b')

    return render(request, 'Madlibs/madlib-form.html', {'form': form, 'madlib': madlib})


def b(request):
    madlib = Madlib.objects.get(id=2)
    context = {
        'madlib': madlib,
    }
    return render(request, 'Madlibs/b.html', context)


def madlib_c(request):
    madlib = Madlib.objects.get(id=3)
    form = MadlibFormC(request.POST or None, instance=madlib)

    if form.is_valid():
        form.save()
        return redirect('Madlibs:c')

    return render(request, 'Madlibs/madlib-form.html', {'form': form, 'madlib': madlib})


def c(request):
    madlib = Madlib.objects.get(id=3)
    context = {
        'madlib': madlib,
    }
    return render(request, 'Madlibs/c.html', context)


def madlib_d(request):
    madlib = Madlib.objects.get(id=4)
    form = MadlibFormD(request.POST or None, instance=madlib)

    if form.is_valid():
        form.save()
        return redirect('Madlibs:d')

    return render(request, 'Madlibs/madlib-form.html', {'form': form, 'madlib': madlib})


def d(request):
    madlib = Madlib.objects.get(id=4)
    context = {
        'madlib': madlib,
    }
    return render(request, 'Madlibs/d.html', context)


def madlib_e(request):
    madlib = Madlib.objects.get(id=5)
    form = MadlibFormE(request.POST or None, instance=madlib)

    if form.is_valid():
        form.save()
        return redirect('Madlibs:e')

    return render(request, 'Madlibs/madlib-form.html', {'form': form, 'madlib': madlib})


def e(request):
    madlib = Madlib.objects.get(id=5)
    context = {
        'madlib': madlib,
    }
    return render(request, 'Madlibs/e.html', context)


def madlib_f(request):
    madlib = Madlib.objects.get(id=6)
    form = MadlibFormF(request.POST or None, instance=madlib)

    if form.is_valid():
        form.save()
        return redirect('Madlibs:f')

    return render(request, 'Madlibs/madlib-form.html', {'form': form, 'madlib': madlib})


def f(request):
    madlib = Madlib.objects.get(id=6)
    context = {
        'madlib': madlib,
    }
    return render(request, 'Madlibs/f.html', context)


def madlib_g(request):
    madlib = Madlib.objects.get(id=7)
    form = MadlibFormG(request.POST or None, instance=madlib)

    if form.is_valid():
        form.save()
        return redirect('Madlibs:g')

    return render(request, 'Madlibs/madlib-form.html', {'form': form, 'madlib': madlib})



def g(request):
    madlib = Madlib.objects.get(id=7)
    context = {
        'madlib': madlib,
    }
    return render(request, 'Madlibs/g.html', context)


def madlib_h(request):
    madlib = Madlib.objects.get(id=8)
    form = MadlibFormH(request.POST or None, instance=madlib)

    if form.is_valid():
        form.save()
        return redirect('Madlibs:h')

    return render(request, 'Madlibs/madlib-form.html', {'form': form, 'madlib': madlib})


def h(request):
    madlib = Madlib.objects.get(id=8)
    context = {
        'madlib': madlib,
    }
    return render(request, 'Madlibs/h.html', context)


def madlib_i(request):
    madlib = Madlib.objects.get(id=9)
    form = MadlibFormI(request.POST or None, instance=madlib)

    if form.is_valid():
        form.save()
        return redirect('Madlibs:i')

    return render(request, 'Madlibs/madlib-form.html', {'form': form, 'madlib': madlib})


def i(request):
    madlib = Madlib.objects.get(id=9)
    context = {
        'madlib': madlib,
    }
    return render(request, 'Madlibs/i.html', context)


def madlib_j(request):
    madlib = Madlib.objects.get(id=10)
    form = MadlibFormJ(request.POST or None, instance=madlib)

    if form.is_valid():
        form.save()
        return redirect('Madlibs:j')

    return render(request, 'Madlibs/madlib-form.html', {'form': form, 'madlib': madlib})


def j(request):
    madlib = Madlib.objects.get(id=10)
    context = {
        'madlib': madlib,
    }
    return render(request, 'Madlibs/j.html', context)


def madlib_k(request):
    madlib = Madlib.objects.get(id=11)
    form = MadlibFormK(request.POST or None, instance=madlib)

    if form.is_valid():
        form.save()
        return redirect('Madlibs:k')

    return render(request, 'Madlibs/madlib-form.html', {'form': form, 'madlib': madlib})


def k(request):
    madlib = Madlib.objects.get(id=11)
    context = {
        'madlib': madlib,
    }
    return render(request, 'Madlibs/k.html', context)


def madlib_l(request):
    madlib = Madlib.objects.get(id=12)
    form = MadlibFormL(request.POST or None, instance=madlib)

    if form.is_valid():
        form.save()
        return redirect('Madlibs:l')

    return render(request, 'Madlibs/madlib-form.html', {'form': form, 'madlib': madlib})


def l(request):
    madlib = Madlib.objects.get(id=12)
    context = {
        'madlib': madlib,
    }
    return render(request, 'Madlibs/l.html', context)


def madlib_m(request):
    madlib = Madlib.objects.get(id=13)
    form = MadlibFormM(request.POST or None, instance=madlib)

    if form.is_valid():
        form.save()
        return redirect('Madlibs:m')

    return render(request, 'Madlibs/madlib-form.html', {'form': form, 'madlib': madlib})


def m(request):
    madlib = Madlib.objects.get(id=13)
    context = {
        'madlib': madlib,
    }
    return render(request, 'Madlibs/m.html', context)


def madlib_n(request):
    madlib = Madlib.objects.get(id=14)
    form = MadlibFormN(request.POST or None, instance=madlib)

    if form.is_valid():
        form.save()
        return redirect('Madlibs:n')

    return render(request, 'Madlibs/madlib-form.html', {'form': form, 'madlib': madlib})


def n(request):
    madlib = Madlib.objects.get(id=14)
    context = {
        'madlib': madlib,
    }
    return render(request, 'Madlibs/n.html', context)


def madlib_o(request):
    madlib = Madlib.objects.get(id=15)
    form = MadlibFormO(request.POST or None, instance=madlib)

    if form.is_valid():
        form.save()
        return redirect('Madlibs:o')

    return render(request, 'Madlibs/madlib-form.html', {'form': form, 'madlib': madlib})


def o(request):
    madlib = Madlib.objects.get(id=15)
    context = {
        'madlib': madlib,
    }
    return render(request, 'Madlibs/o.html', context)


def madlib(request):
    return render(request, 'Madlibs/madlibs.html')

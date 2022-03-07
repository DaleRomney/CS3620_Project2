from . import views
from django.urls import path

app_name = 'Madlibs'
urlpatterns = [
    path('', views.index, name="index"),
    path('madlib/', views.madlib, name="madlib"),
    path('a/<int:id>', views.madlib_a, name="a"),
    path('b/<int:id>', views.madlib_b, name="b"),
    path('c/<int:id>', views.madlib_c, name="c"),
    path('d/<int:id>', views.madlib_d, name="d"),
    path('e/<int:id>', views.madlib_e, name="e"),
    path('f/<int:id>', views.madlib_f, name="f"),
    path('g/<int:id>', views.madlib_g, name="g"),
    path('h/<int:id>', views.madlib_h, name="h"),
    path('i/<int:id>', views.madlib_i, name="i"),
    path('j/<int:id>', views.madlib_j, name="j"),
    path('k/<int:id>', views.madlib_k, name="k"),
    path('l/<int:id>', views.madlib_l, name="l"),
    path('m/<int:id>', views.madlib_m, name="m"),
    path('n/<int:id>', views.madlib_n, name="n"),
    path('o/<int:id>', views.madlib_o, name="o"),
]
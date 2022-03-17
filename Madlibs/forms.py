from django import forms
from .models import Madlib


class MadlibFormA(forms.ModelForm):
    class Meta:
        model = Madlib
        fields = ['relative', 'adjective', 'person', 'verb_end_ed', 'body_part', 'verb_end_ing', 'noun_plural', 'noun'
                  , 'adverb', 'verb']


class MadlibFormB(forms.ModelForm):
    class Meta:
        model = Madlib
        fields = ['person', 'noun', 'superlative_ending_est', 'body_part', 'verb_end_ing', 'verb', 'event', 'day_of_week',
                  'place', 'time_span', 'adverb',]


class MadlibFormC(forms.ModelForm):
    class Meta:
        model = Madlib
        fields = ['number', 'occupation', 'place', 'person', 'body_part', 'adjective', 'noun', 'celebrity', 'verb_end_ing',
                  'adverb', 'verb_end_s']


class MadlibFormD(forms.ModelForm):
    class Meta:
        model = Madlib
        fields = ['silly_word', 'last_name', 'illness', 'noun_plural', 'adjective', 'place', 'number']


class MadlibFormE(forms.ModelForm):
    class Meta:
        model = Madlib
        fields = ['place', 'amount_of_time', 'adjective', 'noun', 'noun_plural', 'verb', 'occupation']


class MadlibFormF(forms.ModelForm):
    class Meta:
        model = Madlib
        fields = ['month', 'number', 'holiday', 'noun_plural', 'verb_end_ed', 'verb', 'noun', 'occupation']


class MadlibFormG(forms.ModelForm):
    class Meta:
        model = Madlib
        fields = ['company', 'noun', 'adjective', 'noun_plural', 'noun_end_ers']


class MadlibFormH(forms.ModelForm):
    class Meta:
        model = Madlib
        fields = ['girl_name', 'noun', 'boy_name', 'verb_end_s', 'noun_plural', 'animal_plural', 'verb', 'adjective']


class MadlibFormI(forms.ModelForm):
    class Meta:
        model = Madlib
        fields = ['adjective', 'occupation', 'animal_plural', 'animal', 'noun', 'noun_plural', 'kitchen_appliance',
                  'verb', 'silly_word']


class MadlibFormJ(forms.ModelForm):
    class Meta:
        model = Madlib
        fields = ['person', 'adjective', 'noun', 'food_plural', 'noun_plural', 'verb_end_ed', 'liquid']


class MadlibFormK(forms.ModelForm):
    class Meta:
        model = Madlib
        fields = ['verb', 'noun', 'adjective', 'government_position', 'holiday', 'occupation', 'crime', 'verb_end_ed',
                  'verb_end_s', 'silly_word', 'noun_end_ers', 'noun_plural']


class MadlibFormL(forms.ModelForm):
    class Meta:
        model = Madlib
        fields = ['fruit', 'noun_plural', 'noun', 'silly_word', 'noun_end_ers', 'animal_plural', 'crime', ]


class MadlibFormM(forms.ModelForm):
    class Meta:
        model = Madlib
        fields = ['number', 'adjective', 'person', 'girl_name', 'animal_plural', 'noun_plural', 'verb_end_ing', 'noun',
                  'location', 'fruit', 'crime', 'animal', 'illness', 'kitchen_appliance', 'food_plural']


class MadlibFormN(forms.ModelForm):
    class Meta:
        model = Madlib
        fields = ['boy_name', 'noun', 'occupation', 'measurement', 'adjective', 'game', 'noun_plural', 'verb_end_ing',
                  'noun_end_ers', 'silly_word', 'kitchen_appliance', ]


class MadlibFormO(forms.ModelForm):
    class Meta:
        model = Madlib
        fields = ['verb', 'adverb', 'adjective', 'noun_plural', 'verb_end_ing', 'noun', 'weapon_plural', 'silly_word',
                  'verb_end_s', 'occupation']

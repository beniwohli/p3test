from django.shortcuts import render
from django.conf import settings

from .markov import gen_word


def hello_from_python_3(request):
    raise AssertionError()


def random_exception(request):
    word = gen_word().title()
    Ex = type(word + 'Exception', (Exception,), {})
    raise Ex(gen_word())

from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt
from django.template.context_processors import csrf


def index(request):
    filen = "polls/index.html"
    t = loader.get_template(filen)   
    c = Context({})
    resp = HttpResponse(t.render(c))
    return resp

def lfile(request):
    filen = "polls/mh4.html"
    t = loader.get_template(filen)   
    c = Context({})
    resp = HttpResponse(t.render(c))
    return resp

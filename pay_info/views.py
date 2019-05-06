from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def testutl(request):
    return HttpResponse('Hello')


def step1url(request):
    return render(request, 'step1.html', locals())


def step2url(request):
    return render(request, 'step2.html', locals())


def step3url(request):
    return render(request, 'step3.html', locals())


def step4url(request):
    return render(request, 'step3.html', locals())

from django.shortcuts import render

from django.http import HttpResponse, Http404

def example_view(request):
	if request.COOKIES:
		return HttpResponse(f' <h1> Hi! </h1>')
	else:
		return HttpResponse(f' <h1> no </h1>')


'''
from django.shortcuts import render
from django.http import HttpResponse, Http404


def example_view(request):
	return HttpResponse(f' <h1> Hi! </h1>')

'''
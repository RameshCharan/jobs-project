from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Hydjobsinfo(request):
    s='<h1> Hyderabad Jobs information</h1>'
    return HttpResponse(s)
def Bangjobsinfo(request):
    s='<h1> Bangalore Jobs information</h1>'
    return HttpResponse(s)
def Mumbaijobsinfo(request):
    s='<h1> Mumbai Jobs information</h1>'
    return HttpResponse(s)
def Chennaijobsinfo(request):
    s='<h1> Chennai Jobs information</h1>'
    return HttpResponse(s)



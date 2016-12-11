from django.shortcuts import render
from django.template import RequestContext

def reg(request):
  data = login.objects.all()
  return render(request, 'reg.html')

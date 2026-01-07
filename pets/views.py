from django.shortcuts import render
from .models import Pet

def lista_pets(request):
    pets = Pet.objects.all()
    return render(request= request,
                  template_name='lista_pets.html',
                  context={'pets': pets})
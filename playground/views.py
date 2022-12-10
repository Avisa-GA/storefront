from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Collection

# Create your views here.
def say_hello(request) :
    try:
     collection = Collection.objects.filter(pk=1).exists();
    except ObjectDoesNotExist:
     pass;
    
    return render(request, 'hello.html', {'name': 'Mosh'})
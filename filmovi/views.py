from django.shortcuts import render
from .models import Filmovi


# Create your views here.
def filmovi_lista(request):

    queryset = Filmovi.objects.all()

    context = {
        'queryset': queryset
    }
    return render(request, 'filmovi.html', context)

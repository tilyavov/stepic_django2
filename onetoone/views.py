from django.shortcuts import render
from onetoone.models import Worker

def index(request):
    people = Worker.objects.order_by('id')
    return render(request, 'index.html', {'people': people})

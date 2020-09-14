from django.shortcuts import redirect, render
from django.views.generic import CreateView
from .models import Email

from rest_framework.viewsets import ModelViewSet
from .serializers import EmailSerializer
from .models import Email


class EmailViewSet(ModelViewSet):
    queryset = Email.objects.order_by('-creation_time')
    serializer_class = EmailSerializer


def ru_index(request):
    context = dict()
    if request.method == 'POST':
        email = request.POST['email']
        Email.objects.create(email=email)
        context['is_send'] = True
        print(context)
    else:
        context['is_send'] = False

    return render(request, 'ru_index.html', context)


def en_index(request):
    context = dict()
    if request.method == 'POST':
        email = request.POST['email']
        Email.objects.create(email=email)
        context['is_send'] = True
        print(context)
    else:
        context['is_send'] = False

    return render(request, 'en_index.html', context)
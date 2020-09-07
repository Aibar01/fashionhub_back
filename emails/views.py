from rest_framework.viewsets import ModelViewSet
from .serializers import EmailSerializer
from .models import Email


class EmailViewSet(ModelViewSet):
    queryset = Email.objects.order_by('-creation_time')
    serializer_class = EmailSerializer

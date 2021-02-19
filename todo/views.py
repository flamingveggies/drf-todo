from rest_framework import viewsets, permissions

from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.order_by('-created')
    serializer_class = TodoSerializer
    permission_classes = [permissions.AllowAny]
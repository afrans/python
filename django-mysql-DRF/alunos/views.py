from rest_framework import viewsets
from .models import Aluno
from .serializers import AlunoSerializer


class AlunoViewSet(viewsets.ModelViewSet):
    """
    ViewSet completo: list, retrieve, create, update, partial_update, destroy
    """

    queryset = Aluno.objects.all().order_by("id")
    serializer_class = AlunoSerializer

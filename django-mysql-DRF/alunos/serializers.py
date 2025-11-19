from rest_framework import serializers
from .models import Aluno


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ["id", "nome", "idade", "curso", "criado_em"]
        read_only_fields = ["id", "criado_em"]

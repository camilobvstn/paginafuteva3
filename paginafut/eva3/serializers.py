from rest_framework import serializers
from eva3.models import Partido, Comentario

class PartidoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Partido
        fields = '__all__'


class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model= Comentario
        fields = '__all__'
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as http_status
from administracao.services import servico_service
from ..serializers import servico_serializer


class Servico(APIView):
    def get(self, request, format=None):
        servicos = servico_service.listar_servicos()
        serializer_servico = servico_serializer.ServicoSerializer(servicos, many=True)
        return Response(serializer_servico.data, status=http_status.HTTP_200_OK)

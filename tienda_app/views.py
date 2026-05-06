from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def comprar(request):
    data = {
        "mensaje": "Compra procesada correctamente",
        "producto": "Libro de Arquitectura de Software",
        "cantidad": 1,
        "total": 85000,
        "estado": "API funcionando correctamente"
    }

    return Response(data)
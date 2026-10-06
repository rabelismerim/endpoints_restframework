from django.db.models.deletion import ProtectedError
from rest_framework.response import Response
from rest_framework.views import exception_handler as drf_exception_handler


def exception_handler(exc, context):
    if isinstance(exc, ProtectedError):
        return Response({"detail": "Este registro possui vínculos e não pode ser excluído."}, status=409)
    return drf_exception_handler(exc, context)

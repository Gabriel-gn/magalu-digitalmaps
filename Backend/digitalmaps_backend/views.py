from django.http import JsonResponse
from rest_framework import generics


class Filament_REST(generics.ListCreateAPIView):
    authentication_classes = []
    queryset = None

    def get(self, request, *args, **kwargs):
        return JsonResponse({'aaaa': 'aaaa'})

    def post(self, request, *args, **kwargs):
        return JsonResponse({})
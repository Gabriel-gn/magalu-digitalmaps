from django.http import JsonResponse
from rest_framework import generics


class LocaisRoot(generics.ListCreateAPIView):
    authentication_classes = []
    queryset = None

    def get(self, request, *args, **kwargs):
        return JsonResponse({'Hello': 'World',
                             'Olá': 'Galera do labs'})

    def post(self, request, *args, **kwargs):
        return JsonResponse({})
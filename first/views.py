from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response


class First(APIView):
    def get(self, request):
        return Response('Method GET')

    def post(self, request):
        return Response('Method post')

    def put(self, request):
        return Response('Method put')

    def patch(self, request):
        return Response('Method patch')

    def delete(self, request):
        return Response('Method delete')


class Second(APIView):
    def get(self, *args, **kwargs):
        params = self.request.query_params.dict()
        print(params)
        return Response(params)

    def post(self,*args,**kwargs):
        data = self.request.data
        print(data)
        return Response(data)


class Thrid(APIView):
    def get(self, *args, **kwargs):
        print(kwargs)
        return Response(kwargs)

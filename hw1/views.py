from django.shortcuts import render

import json

from rest_framework.views import APIView
from rest_framework.response import Response


class Hw1View(APIView):
    def get(self, *args, **kwargs):
        try:
            with open('users.json') as file:
                data = json.load(file)
                return Response(data)
        except Exception as err:
            print(err)

    def post(self, *args, **kwargs):
        try:
            newUser = self.request.data
            with open('users.json') as readFile:
                users: list = json.load(readFile)
                users.append(newUser)
                with open('users.json', 'w') as writeFile:
                    json.dump(users, writeFile)
                    return Response(users)
        except Exception as err:
            print(err)

    def delete(self, *args, **kwargs):
        try:
            with open('users.json') as readFile:
                users: list = json.load(readFile)
                users.pop()
                with open('users.json', 'w') as writeFile:
                    json.dump(users, writeFile)
                    return Response(users)
        except Exception as err:
            print(err)

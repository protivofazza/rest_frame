from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView, Response
from .serializers import UsersSerializer, TariffsSerializer, StatesSerializer
from .models import Users as UsersModel, Tariffs as TariffsModel, States as StatesModel


class Users(APIView):
    def get(self, request):
        user = UsersModel.objects.filter(agg_id='005602173').first()
        serializer = UsersSerializer(user).data
        response = {
            'data': serializer
        }
        return Response(response)

    # class Tariffs(APIView):
    #     tariff = TariffsModel.objects.filter(agg_id='005602173').first()
    #     serializer = UsersSerializer(tariff).data
    #     response = {
    #         'data': serializer
    #     }
    #     return Response(response)
    #     # queryset = TariffsModel.objects.all()
    #     # serializer_class = TariffsSerializer
    #     # permission_classes = [permissions.IsAuthenticated]
    #
    #
    # class States(APIView):
    #     """
    #     API endpoint that allows groups to be viewed or edited.
    #     """

    #     queryset = StatesModel.objects.all()
    #     serializer_class = StatesSerializer
    #     permission_classes = [permissions.IsAuthenticated]

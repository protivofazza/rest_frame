from rest_framework import serializers
from .models import Users, Tariffs, States


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('info_id', 'agg_id', 'family_name', 'first_name', 'account', 'state', 'type')


class TariffsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariffs
        fields = ('info_id', 'type_name')


class StatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = States
        fields = ('info_id', 'state')



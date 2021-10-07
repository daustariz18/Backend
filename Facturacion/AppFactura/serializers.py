from .models import Clients, Product, Bills
from rest_framework import serializers


class ClientsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clients
        fields = ('id', 'first_name', 'last_name', 'email')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'precio', 'descripcion']


class BillsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bills
        fields = ['client_id', 'company_name', 'nit']

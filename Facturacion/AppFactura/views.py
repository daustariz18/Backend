from AppFactura.models import Clients, Product, Bills
from AppFactura.serializers import ClientsSerializer
from AppFactura.serializers import ProductSerializer
from AppFactura.serializers import BillsSerializer
from rest_framework import generics


class ClientsList(generics.ListAPIView):

    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer


class ClientsCreate(generics.CreateAPIView):

    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer


class ClientUpdate(generics.UpdateAPIView):

    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer


class ClientDelete(generics.DestroyAPIView):

    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer


class ProductList(generics.ListAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreate(generics.CreateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdate(generics.UpdateAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDelete(generics.DestroyAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class BillsList(generics.ListAPIView):

    queryset = Bills.objects.all()
    serializer_class = BillsSerializer


class BillsCreate(generics.CreateAPIView):

    queryset = Bills.objects.all()
    serializer_class = BillsSerializer


class BillsUpdate(generics.UpdateAPIView):

    queryset = Bills.objects.all()
    serializer_class = BillsSerializer


class BillsDelete(generics.DestroyAPIView):

    queryset = Bills.objects.all()
    serializer_class = BillsSerializer

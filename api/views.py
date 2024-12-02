from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CustomerSerializer, OrderSerializer
from record.models import Customer


@api_view(['GET'])
def getData(request):
    customer = Customer.objects.all()
    serializer = CustomerSerializer(customer, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addCustomer(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def addOrder(request):
    serializer = OrderSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

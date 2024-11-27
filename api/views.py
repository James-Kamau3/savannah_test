from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CustomerSerializer
from record.models import Customer


@api_view(['GET'])
def getData(request):
    customer = Customer.objects.all()
    serializer = CustomerSerializer(customer, many=True)
    return Response(serializer.data)


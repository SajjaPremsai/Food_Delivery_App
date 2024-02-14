from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view , parser_classes

from .models import Item , Organization , Pricing
from .serializers import ItemSerializer ,OrganizationSerializer , PricingSerializer , PricingRequestSerializer
from rest_framework.parsers import JSONParser
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView


class DeliveryCharge(GenericAPIView):
    serializer_class = PricingRequestSerializer
    @swagger_auto_schema(operation_description="This API calculates the Delivery price for the given information")
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            obj = Pricing.objects.filter(item__type=data['item_type'],zone=data['zone'],organization_id=data['organization_id']).values_list('organization_id', flat=True).distinct()
            if len(obj) > 0:
                price = obj.values("km_price")[0]["km_price"]
                distance = obj.values("base_distance_in_km")[0]["base_distance_in_km"]
                if data["total_distance"] > distance:
                    total_price = obj.values("fix_price")[0]["fix_price"] + ((data["total_distance"] - distance) * price)
                else:
                    total_price = obj.values("fix_price")[0]["fix_price"]
                return Response({"total_price": total_price})
            else:
                return Response({"Message": "No Delivery Option are Found"})
        else:
            return Response(serializer.errors)


class Create_Organizations(GenericAPIView):
    serializer_class = OrganizationSerializer
    
    @swagger_auto_schema(operation_description="This API gets the all the Organizations data")
    def get(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(operation_description="This API creates a new organization")
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def get_queryset(self):
        return Organization.objects.all()


class Create_Items(GenericAPIView):
    serializer_class = ItemSerializer
    
    @swagger_auto_schema(operation_description="This API gets the all the create items")
    def get(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(operation_description="This API creates a new item")
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def get_queryset(self):
        return Item.objects.all()


class Create_Pricing(GenericAPIView):
    serializer_class = PricingSerializer
    
    @swagger_auto_schema(operation_description="This API creates a new item")
    def get(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(operation_description="This API creates a new pricing structure to a organization")
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def get_queryset(self):
        return Pricing.objects.all()

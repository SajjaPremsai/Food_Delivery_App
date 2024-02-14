from rest_framework import serializers
from .models import Item , Organization , Pricing

class ItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Item 
        fields = '__all__'
    

class OrganizationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Organization
        fields = '__all__' 
        
        
class PricingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Pricing 
        fields = '__all__'
        

class PostPricingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Pricing 
        fields = ["zone","base_distance_in_km","fix_price","organization","item"]
    
class PricingRequestSerializer(serializers.Serializer):
    zone = serializers.CharField(max_length=100)
    organization_id = serializers.IntegerField()
    total_distance = serializers.IntegerField()
    item_type = serializers.CharField(max_length=100)

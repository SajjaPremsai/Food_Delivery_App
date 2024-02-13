from django.urls import path
# from django.views.generic import TemplateView

# from django.urls import re_path
# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

from djangoapp.views import Create_Items, Create_Organizations, Create_Pricing, DeliveryCharge

# schema_view = get_schema_view(
#    openapi.Info(
#       title="Food Delivery App",
#       default_version='v1',
#       description="",
#       contact=openapi.Contact(email="sajjapremsai8938@gmail.com"),
#       license=openapi.License(name="BSD License"),
#    ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
# )


urlpatterns = [
   #  path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   #  path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("Organizations", Create_Organizations.as_view()),  
    path("Item", Create_Items.as_view()),  
    path("Pricing", Create_Pricing.as_view()), 
    path("DeliveryPrice", DeliveryCharge.as_view()),  
]

from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.models import Banner
from base.serializers import BannerSerializer

@api_view(['GET'])
def getBanners(request):
    banners = Banner.objects.all()
    serializer = BannerSerializer(banners, many=True)
    return Response(serializer.data)    

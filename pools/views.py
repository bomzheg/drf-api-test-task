from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Poll
from .serialializers import PoolSerializer


def index(request):
    return Response("Hello, World!")


class PoolsView(APIView):
    def get(self, request):
        pools = Poll.objects.all()
        serializer = PoolSerializer(pools, many=True)
        return Response({'pools': serializer.data})

    def post(self, request):
        pool = request.data.get("pool")
        serializer = PoolSerializer(data=pool)
        if serializer.is_valid():
            pool_saved = serializer.save()
            return Response({'success': True, "pool": PoolSerializer(pool_saved).data})
        return Response(status=400)

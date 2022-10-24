from main.models import Sneakers
from main.serializers import MealsSerializer
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import GenericAPIView
# Create your views here.

class AboutSneakers(ListModelMixin, CreateModelMixin, GenericAPIView):
    serializer_class = MealsSerializer

    def get_queryset(self):
        queryset = Sneakers.objects.all()
        return queryset

    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)

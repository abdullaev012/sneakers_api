from rest_framework import serializers


from main.models import Sneakers


class MealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sneakers
        fields = ['id', 'sneakers_name', 'description', 'image', 'price']
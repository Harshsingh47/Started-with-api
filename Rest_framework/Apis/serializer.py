from rest_framework import serializers
from .models import *

class Postserializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = "__all__"

from rest_framework import serializers
from Relations.models import Posts,Creators


# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.CharField(required=False, allow_blank=True,max_length=100)
#     text = serializers.CharField(max_length=100)
#     created = serializers.DateField()
#
#     def create(self, validated_data):
#         return Posts.objects.create(** validated_data)
#
#     def update(self, instance, validated_data):
#         instance.author = validated_data.get('author',instance.author)
#         instance.text = validated_data.get('text',instance.text)
#         instance.created = validated_data.get('created',instance.created)
#         instance.save()
#         return instance


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['id','author','text','created']


class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creators
        fields = ['id','Name','title','language']


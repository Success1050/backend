from rest_framework import serializers
from .models import Comment

class CommentSerializers(serializers.ModelSerializer):
    # image_url= serializers.SerializerMethodField()
    class Meta:
        model= Comment
        fields= ['id', 'name', 'email', 'message']

    # def get_image_url(self, obj):
    #     request= self.context.get('request')
    #     if obj.image and request:
    #         return request.build_absolute_uri(obj.image.url)
    #     return None
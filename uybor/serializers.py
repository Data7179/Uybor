from rest_framework.serializers import ModelSerializer
from .models import Uylar


class UylarSerializer(ModelSerializer):
    class Meta:
        model = Uylar
        fields = "__all__"


    # def to_representation(self, instance):
    #     return {
    #         "yangilik":{
    #             "id": instance.id,
    #             "title": instance.title,
    #             "preview_text": instance.text[:100],
    #         }
    #     }

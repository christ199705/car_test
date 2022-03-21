from rest_framework import serializers
from .models import Brand


class BrandModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        exclude = ("update_time", "create_time")
        extra_kwargs = {"country": {"write_only": True}}

    def validate(self, attrs):
        tuple01 = ("中国", "韩国", "法国", "德国", "美国", "日本")
        if attrs["country"] not in tuple01:
            raise serializers.ValidationError("国家错误")
        elif 1 > len(attrs["name"]) or len(attrs["name"]) > 10:
            raise serializers.ValidationError("品牌名称长度在1-10之间")
        elif 1 > len(attrs["originator"]) or len(attrs["originator"]) > 8:
            raise serializers.ValidationError("品牌创始人名字长度在1-8之间")
        return attrs

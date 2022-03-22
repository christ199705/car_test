from rest_framework import serializers

from brand.models import Brand
from .models import Type
from brand.serializers import BrandModelSerializer


class TypeModelSerializer(serializers.ModelSerializer):
    # B_id = serializers.StringRelatedField(label="所属品牌")
    B_id = serializers.SlugRelatedField(slug_field="name", queryset=Brand.objects.all())

    # queryset = Brand.objects.all()
    class Meta:
        model = Type
        exclude = ("update_time", "create_time")

    def validate(self, attrs):
        if len(attrs["name"]) < 1 or len(attrs["name"]) > 8:
            raise serializers.ValidationError("{'error_code':400,'error_message':'车型名称长度在1-8之间'}")
        elif attrs["year_count"] < 0:
            raise serializers.ValidationError("{'error_code':400,'error_message':'年销量不能小于0'}")
        return attrs


class TypeNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ("id", "name")



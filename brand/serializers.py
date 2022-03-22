from rest_framework import serializers
from .models import Brand
from type.models import Type


class BrandModelSerializer(serializers.ModelSerializer):
    # 第一个固定的序例化类，用于初始的几个接口，还要校验
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


class BrandNameSerializer(serializers.ModelSerializer):
    # 值返回id 和 姓名的序例化器类
    class Meta:
        model = Brand
        fields = ["id", "name"]


class BrandTypeSerializer(serializers.ModelSerializer):
    # 数据库反查序例化器类，只定义
    class Meta:
        model = Type
        fields = ["name","year_count"]


class BrandByTypeSerializer(serializers.ModelSerializer):
    # 调用反查序例化器反查
    type_set = BrandTypeSerializer(read_only=True, many=True)

    class Meta:
        model = Brand
        fields = ["id", "type_set"]
    # 返回内容

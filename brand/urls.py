"""car URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import BrandView
from rest_framework_swagger.views import get_swagger_view

from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
# 自定义路由
from rest_framework import routers


# 1。创建路由对象
router = routers.SimpleRouter()
# 2,注册路由,第一个参数为路由前缀，一般添加为应用名即可，第二个参数为视图类名
router.register("", BrandView)
# dict1 = {"get": "list", "post": "create"}
# dict2 = {"get": "retrieve",
#          "put": "update",
#          "delete": "destroy"}
# dict3 = {"get": "names"}
# dict4 = {"get": "type"}
schema_view = get_swagger_view(title='API 接口文档')
urlpatterns = [
    path("", include(router.urls)),
    path('docs/', schema_view, name='docs'),  # 线上环境，干掉

    # path('', BrandView.as_view(dict1)),
    # path('<int:id>', BrandView.as_view(dict2)),
    # path('names/', BrandView.as_view(dict3)),
    # path('<int:id>/type/', BrandView.as_view(dict4)),
]
# urlpatterns += router.urls
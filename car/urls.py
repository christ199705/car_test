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
from django.urls import path, include, re_path

# coreapi 配置
from rest_framework.documentation import include_docs_urls
# swagger 配置
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


Schema_view = get_schema_view(
    openapi.Info(
        title="汽车品牌接口文档",
        default_version='v1.0',
        description="秦旺django rest_framework 接口文档",
        terms_of_service="http://qinwang.work",
        contact=openapi.Contact(email="qinwang@codemao.cn"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    # permission_classes=(permissions.AllowAny,),  权限类
)

urlpatterns = [
    # 主路由
    path('admin/', admin.site.urls),
    path('brand/', include("brand.urls")),
    path('type/', include("type.urls")),



    #coreapi 配置
    path("docs/", include_docs_urls(title="API文档", description="秦旺的接口文档平台")),

    # swagger 配置
    re_path(r'swagger(?P<format>.json|.yaml)$', Schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
    path('swagger/', Schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', Schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]




"""myshop_back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include,re_path
from django.views.static import serve
from django.conf import settings

# DRF生成接口文档
from rest_framework.documentation import include_docs_urls

# 生成swagger接口文档
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer,OpenAPICodec
schema_view = get_schema_view(title='我的商城swagger接口文档', renderer_classes=[SwaggerUIRenderer, OpenAPICodec])


urlpatterns = [
    path('admin/', admin.site.urls),
    path('basic/',include('apps.basic.urls')),
    path('goods/',include('apps.goods.urls')),
    path('users/',include('apps.users.urls')),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('docs/', include_docs_urls(title='我的商城DRF接口文档')),
    path('docs2/', schema_view, name='docs'),
    # re_path('media/(?P<path>.*)', serve, {"document_root": settings.MEDIA_ROOT}),
    # re_path('static/(?P<p ath>.*)', serve, {"document_root": settings.STATIC_ROOT}),
]

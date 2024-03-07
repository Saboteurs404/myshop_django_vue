from django.contrib import admin
from apps.goods.models import *

# Register your models here.

'''
①在Django中，@admin.register() 是一个装饰器（decorator）
用于注册数据库模型类（Model）到后台管理界面。具体来说，
@admin.register(GoodsCategory) 这行代码的作用是将
GoodsCategory 数据库模型类注册到Django后台管理界面，
从而允许您在后台对该模型进行管理和操作。

一旦通过 @admin.register() 注册了一个数据库模型类，
Django会自动创建一个对应的管理页面，该页面允许您查看、添加、修改和删除模型的实例。
这样，您就可以在后台管理界面轻松地管理您的数据库中的 GoodsCategory 数据。

②在上面的代码中，GoodsCategoryAdmin 类被用作 GoodsCategory 模型的管理类，
它继承自 admin.ModelAdmin。通过在该类中定义不同的属性和方法，
您可以自定义后台管理界面的外观和行为，例如定义要显示的字段、搜索和过滤选项、
排序规则等等。

'''
@admin.register(GoodsCategory)
class GoodsCategoryAdmin(admin.ModelAdmin):
    admin.site.site_title='我的特产商城后台'
    admin.site.site_header='我的特产商城后台'
    admin.site.index_title="商城平台管理"

    # 设置列表中显示的字段
    list_display = ['name','logo', 'sort', 'create_time']
    # 搜索
    search_fields = ['name']
    # 过滤
    list_filter = ['name','parent_id']
    # 设置日期选择器
    date_hierarchy = 'create_time'
    # 设置每页显示的数量
    list_per_page = 10
    # 设置排序
    ordering = ['sort']

@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    # 设置列表中显示的字段
    list_display = ['name', 'market_price', 'price']

@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    #设置列表中显示的字段
    list_display = ['goods_id','sort', 'images']
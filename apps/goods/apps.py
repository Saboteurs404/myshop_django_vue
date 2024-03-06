from django.apps import AppConfig


class GoodsConfig(AppConfig):
    name = 'apps.goods'
    #TODO: 商品管理会显示在admin后台管理系统中的左侧菜单导航栏中
    verbose_name='商品管理'

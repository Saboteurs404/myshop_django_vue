from django.shortcuts import render,redirect
from django.views.generic.base import View
from django.http import HttpResponse,JsonResponse
from apps.goods.models import *
from apps.goods.forms import GoodsCategoryForm
import json

class GoodsCategoryView(View):
    def get(self,request):
        cates=GoodsCategory.objects.all()
        return render(request,"shop/goods/cate_index.html",{"cates":cates})

    def post(self,request):
        pass

class GoodsCategoryAddView(View):
    def __init__(self):
        self.alist={}

    def binddata(self,datas,id,n):
        if id==0:
            datas=datas.filter(parent__isnull = True)
        else:
            datas=datas.filter(parent__isnull =True)
        for data in datas:
            self.alist[data.id]=self.spacelength(n)+data.name
            self.binddata(datas,data.id,n+2)
        return self.alist

    def spacelength(self,i):
        space=''
        for j in range(1,i):
            space+="&nbsp;&nbsp;"
        return space+"|--"

    def get(self,request):
        form_obj=GoodsCategoryForm()
        return render(request,"shop/goods/cate_add.html",{"form_obj":form_obj})

    def post(self,request):
        form_obj=GoodsCategoryForm(request.POST,request.FILES)
        if form_obj.is_valid():
            name=request.POST.get("name",'')
            cates=GoodsCategory.objects.filter(name=name)
            if cates:
                info='分类已经存在'
            else:
                #form_obj.cleaned_data["is_staff"]=1
                #form_obj.cleaned_data["is_superuser"]=0 #非管理员
                #接收页面传递过来的参数，进行新增
                cate=GoodsCategory.objects.create(**form_obj.cleaned_data)
                #成功后，重定向到商品分类列表页面
                #info='注册成功,请登陆'
                return redirect('cate_index')
            return render(request,'shop/goods/cate_index.html',{"form_obj":form_obj,"info":info})
        else:
            errors = form_obj.errors
            print(errors)
            return render(request, "shop/goods/cate_add.html", {'form_obj': form_obj, 'info': errors})

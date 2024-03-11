from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from apps.users import forms
from apps.users.models import MyUser
# Create your views here.


#TODO: 用户注册
def user_reg(request):
    if request.method == 'GET':
        form_obj = forms.UserRegForm()
        return render(request, 'shop/user_reg.html',{'form_obj':form_obj})
    if request.method == 'POST':
        form_obj = forms.UserRegForm(request.POST, request.FILES)
        #? 校验表单中数据是否合法
        if form_obj.is_valid():
            uname = request.POST.get('username','')
            users=MyUser.objects.filter(username=uname)
            if users:
                for user in users:
                    user_img = user.user_img
                info='用户已经存在'
            else:
                #? 获取表单中通过验证的数据
                form_obj.cleaned_data.pop('re_password')
                form_obj.cleaned_data['is_staff']=1 #? 可以登录管理员后台
                form_obj.cleaned_data['is_superuser']=0 # 非超级管理员
                user=MyUser.objects.create_user(**form_obj.cleaned_data)
                user_img = user.user_img
                info = '注册成功，请登录'
            return render(request,'shop/user_reg.html',{'form_obj':form_obj,'info':info,'user_img':user_img})
        else:
            #? 表单中验证错误的信息
            errors = form_obj.errors
            print(errors)
            return render(request,"shop/user_reg.html",{'form_obj':form_obj,'errors':errors})

#TODO: 用户登录
def user_login(request):
    return render(request, 'shop/user_login.html')

#TODO: 使用Ajax对用户登录的提交数据进行处理
def ajax_login_data(request):
    uname = request.POST.get('username','')
    pwd = request.POST.get('password','')
    json_dict = {}
    if uname and pwd: #? 不为空的情况下查询数据库
        if MyUser.objects.filter(username=uname): #? 判断用户是否存在
            #? 如果存在，进行验证
            user = authenticate(username=uname,password=pwd)
            if user:#? 如果通过验证
                if user.is_active: #? 用户状态为激活
                    login(request,user) #? 进行登录操作，完成session操作
                    json_dict['code'] = 1000
                    json_dict['msg'] = "登录成功"
                else:
                    json_dict['code'] = 1001
                    json_dict['msg'] = '用户还未激活'
            else:
                json_dict['code'] = 1002
                json_dict['msg'] = '账号密码不对，请重新输入'
        else:
            json_dict['code'] = 1003
            json_dict['msg'] = '用户账号有误，请查询'
    else:
        json_dict['code'] = 1004
        json_dict['msg'] = '用户名或者密码为空'
    return JsonResponse(json_dict)

#TODO: 用户首页
def index(request):
    if request.method=='GET':
        level=request.GET.get('level')
        truename=request.GET.get('truename','')
        status=request.GET.get('status')

        search_dict = dict()
        if level:
            search_dict['level']=level
        if truename:
            search_dict['truename']=truename
        if status:
            search_dict['status']=status

        datas = MyUser.objects.filter(**search_dict).order_by('-id')

        page_size = 2 # 每页显示行数
        try:
            if not request.GET.get('page'):
                curr_page=1
            curr_page=int(request.GET.get('page'))
        except:
            curr_page=1
        #todo: 每页显示数据的行数 
        paginator=Paginator(datas,page_size)

        try:
            users = paginator.page(curr_page)
        except PageNotAnInteger:
            users=paginator.page(1)
        except EmptyPage:
            users=paginator.page(1)
        context = {
            'level':level,
            'truename':truename,
            'status':status,
            'users':users,
        }
        print(context)
    return render(request, 'shop/users/index.html',context=context)

#TODO：删除用户
def delete(request,id):
    obj=MyUser.objects.get(id=id)
    obj=delete()
    json_dict={}
    json_dict['code']=200
    json_dict['msg']='删除数据成功'
    return JsonResponse(json_dict)

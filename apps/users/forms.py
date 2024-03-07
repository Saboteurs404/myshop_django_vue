from apps.users.models import *
from django import forms
from django.core.exceptions import ValidationError
import re

#TODO: 自定义验证规则

def mobile_validate(value):
    mobile_re = re.compile(
        r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$'
        )
    if not mobile_re.match(value):
        raise ValidationError('手机号格式错误')


class UserRegForm(forms.Form):
    username = forms.CharField(label='用户名', min_length=2,
                    widget=forms.widgets.TextInput(
                        #其中class样式为form-control，这是bootstrap的样式
                        attrs = {'class':'form-control','placeholder':'请输入用户名'}
                    ),
                    error_messages={
                        'required':'用户姓名不能为空',
                        'min_length':'长度至少2位'
                    }
                )

    password = forms.CharField(label='密码',min_length=4,max_length=10,
                    widget=forms.widgets.PasswordInput(
                        #render_value=True，页面校验不通过后，页面上该值还存在
                        attrs = {'class':'form-control','placeholder':'请输入密码'},
                        render_value=True
                    ),
                    error_messages={
                        'max_length':'密码最长10位',
                        'required':'密码不能为空',
                        'min_length':'密码最少4位'
                    }
                )

    re_password = forms.CharField(label='确认密码',min_length=4,max_length=10,
                    widget=forms.widgets.PasswordInput(
                        attrs={'class':'form-control','placeholder':'请再次输入密码'},
                        render_value=True
                    ),
                    error_messages={
                        'max_length':'密码最长10位',
                        'required':'密码不能为空',
                        'min_length':'密码最少4位'
                    }
                )

    nickname = forms.CharField(label="昵称", max_length=20,required=False,
                    widget=forms.widgets.TextInput(
                        # 其中class样式为form-control，这是bootstrap的样式
                        attrs={'class': 'form-control', 'placeholder': "请输入用户昵称"}
                    ),
                    error_messages={
                        'required': '用户昵称不能为空',
                        'max_length': '昵称长度不能超过20位',
                    }
                )

    email = forms.EmailField(label='邮箱',
                    widget=forms.widgets.EmailInput(
                        attrs = {'class':'form-control','placeholder':'请输入邮箱号'}
                    ),
                    error_messages={
                        'required':'邮箱不能为空',
                        'invalid':'邮箱格式不对'
                    }
                )

    mobile = forms.CharField(label='手机号码',validators=[mobile_validate],
                    widget=forms.widgets.TextInput(
                        attrs={
                            'class':'form-control',
                            'placeholder':'请输入手机号码'
                            }
                    ),
                    error_messages={
                        'required':'手机号码不能为空'
                    }
                )

    user_img = forms.ImageField(label='用户头像',required=False,
                    widget=forms.widgets.FileInput(
                        attrs={
                            'class':'from-control'
                        }
                    )
                )

''''
钩子函数：

1、是个函数，在系统消息触发时被系统调用

2、不是用户自己触发的

3、使用时直接编写函数体

钩子函数的名称是确定的，当系统消息触发，自动会调用。

clean() 函数作用是在 Django Form 表单数据进行提交前进行校验，并将校验过后的数据返回。

Django 的 clean() 一般是在 Django Form 中定义。我们首先要在 forms.py
文件中定义一个继承 forms.Form 的类，然后在该类中写入需要校验的字段，并在每
个字段后面定义一个 clean_ 前缀的方法，这个方法应该返回一个经过校验过后的值。
'''
#TODO: 全局钩子函数
def clean(self):
    '''
    在表单验证成功后，可以通过forms.clean()方法或者forms.clean_data属性获取表单提交的数据
    ，此外还可以通过forms.data获取表单原始数据
    '''
    password = self.cleaned_data.get("password")
    re_password = self.cleaned_data.get('re_password')
    print("密码为：{}".format(password))
    if password != re_password:
        #? 使用add_error()方法来处理。让错误信息在指定字段处显示
        self.add_error("re_password",ValidationError("两次密码输入不一致"))
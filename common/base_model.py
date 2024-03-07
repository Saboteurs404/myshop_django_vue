from django.db import models

class BaseModel(models.Model):
    '''
    抽象基类
    auto_now: 无论是你添加还是修改对象，时间为你添加或者修改对象的时间，一般用作更新时间；
    auto_now_add:为添加时的时间，更新对象时不会变动，一般用作创建时间


    '''
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True,verbose_name="更新时间")

    class Meta:
        #TODO: 指定抽象类
        '''
        抽象类（abstract base class,ABC）就是类里定义了纯虚成员函数的类。纯虚函数一般只提供了接口，
        并不会做具体实现（虽然可以），实现由它的派生类去重写。抽象类不能被实例化(不能创建对象)，
        通常是作为基类供子类继承，子类中重写虚函数，实现具体的接口。简言之，ABC描述的是至少使用一个纯虚函数的接口，
        从ABC派生出的类将根据派生类的具体特征，使用常规虚函数来实现这种接口。
        '''
        abstract = True
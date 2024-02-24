# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 09:55:16 2018

@author: 高治国
"""

#继承
#刘备类:父类 -> 被其他类继承的类称之为父类(超类,基类)
class LiuBei:
    #属性
    familyname = '刘'
    firsttime = '备'
    sex = 'man'
    money = '100'
    country = '蜀国'
    wife = ('甘夫人','糜夫人','孙尚香')
    #方法
    def say(self):
        print('险损我一员大将')

    #非绑定类的方法[对象访问]
    def drink(self):
        print(self)
        print('来干了这杯')

    def walk(self):
        print('gogo')

    #绑定类的方法
    def la():
        print('hualala')

#刘禅类:子类 -> 继承其他类的类称之为子类(派生类)
class LiuShan(LiuBei):
    #子类独有的成员
    #属性
    weight = '180斤'

    #方法
    def douququ(self):
        print('此间乐,不思蜀')

    #重载父类方法
    def say(self):
        print('刘备baba')

    #重载父类的drink方法,但是还要将父类中操作拿过来使用
    def drink(self):
        print('举起筷子,夹一口菜')
        #喝酒 通过对象调用的方法的重载(推荐使用super().方法名())
        super().drink() #LiuBei.drink(self)

    #重载父类的la方法,但是还要将父类中操作拿过来使用
    def la():
        print('准备好纸')
        #调用父类的la方法(推荐使用类名.方法名)
        LiuBei.la()

#查看刘禅类
print(LiuShan.__dict__)#继承操作不会将成员直接复制到子类中
print(LiuShan.sex)
LiuShan.walk(1)
#print(LiuShan.wife)
'''
1.所有的类的父类都是object子类
2.子类继承父类则可以访问父类的所有成员.(私有成员除外)
3.子类继承父类并不会将父类的所有成员复制到子类当中去,访问父类成员是间接通过父类来访问的(目的:节省资源)
4.子类可以具有自己独有的属性和方法
5.子类可以重载父类中的方法,只需要设置和父类指定成员相同的名称即可实现重载,重载之后的成员,子类只会访问当前类中的成员,而不会调用父类中同名的成员
6.子类中如果重载父类的方法,并且还想将重载的父类方法借调过来使用,可以在重载的方法中使用如下方法
[父类名.方法()](适合类)  或者  [super().方法()](适合对象)
'''
result = issubclass(type,object)
print(result)

#访问子类独有的成员
LiuShan.douququ(1)
print(LiuShan.weight)

#访问继承来的方法
LiuShan.say(1)

#访问重载并且调用了父类的方法的方法
LiuShan.la()

ls = LiuShan()
ls.drink()



#Python语法中没有受保护的语法,程序员约定一种操作来实现受保护
class Father:
    #属性
    sex = 'man'
    #受保护的
    _money = 1000
    color = 'yellow'
    #私有化
    __wife = 'bingbing'

    #方法
    def eat(self):
        print(Father._money)
        print('吃吃吃')

    def niao(self):
        print('哗哗哗')

class Son(Father):
    #添加一个子类的方法用于测试子类中的访问
    def test():
        #方式访问父类中私有成员
        #print(Father.wife)
        #print(Son.wife)
        #访问父类中公共的成员
        print(Son.color)
        #访问受保护的成员
        print(Son._money)

Son.test()
Father.eat(1)
print(Father._money)
#受保护的定义
'''
私有化:只能在类或者对象的结构中访问
公共的:可以在任何位置访问
受保护:可以在当前类或者对象 和子类或者子类对象中访问

        类内    子类中    类外部
私有化:   √        ×        ×
受保护:   √        √        √(×类外部应该不能访问)
公共的:   √        √        √
'''



#单继承

class Biology:
    #属性
    life = '活的'
    #方法
    def shengzhi(self):
        print('生育后代')

class animal(Biology):
    #属性
    age = 18
    #方法
    def jiao(self):
        print('叫两声听听')

class mammal(animal):
    #属性
    gen = '胎生'
    #方法
    def weinai(self):
        print('干了这杯奶')

class Human(mammal):
    #属性
    name = '囡囡'

    def dapai(self):
        print('王炸')

#实例化对象操作
zb = Human()
zb.dapai()
zb.weinai()
zb.jiao()
zb.shengzhi()



#多继承

class GrandPa:
    def damajiang(self):
        print('大三元')

class GrandMa:
    def doudizhu(self):
        print('飞机')

class LaoLao:
    def dance(self):
        print('弯弯的河水天上来')

class LaoYe:
    def zhajinhua(self):
        print('哗哗哗')

class PaPa:
    def zhuanqian(self):
        print('赚钱')

class MaMa:
    def huaqian(self):
        print('花钱')

class LaoWang:
    def fanqiang(self):
        print('FQ')

class Son(LaoWang,MaMa,PaPa,LaoYe,LaoLao,GrandMa,GrandPa):
    def kengdie(self):
        print('我老子是刘备')

#实例化对象
ls = Son()
ls.kengdie()
ls.fanqiang()
ls.huaqian()
ls.doudizhu()
ls.dance()
ls.damajiang()
ls.zhajinhua()
ls.zhuanqian()



#菱形继承
'''
        动物类

人类              鸟类

        鸟人类
'''

#动物类
class Animal:

    #属性
    pass

    #方法
    def say(self):
        print('Animal张开嘴')
        print('Animal合上嘴')

#人类
class Human(Animal):
    #属性
    pass

    #方法
    def say(self):
        print('人类张开嘴')
        #调用动物类的say方法
        super().say()
        print('人类合上嘴')

#鸟类
class Bird(Animal):
    #属性
    pass

    #方法
    def say(self):
        print('鸟类张开嘴')
        #调用动物类的say方法
        super().say()
        print('鸟类合上嘴')

#鸟人类
class Birdy(Human,Bird):
    #属性
    pass

    #方法
    def say(self):
        print('鸟人类张开嘴')
        #鸟类的say
        Bird.say(self)
        #人类say
        Human.say(self)
        print('鸟人类合上嘴')

#实例化鸟人对象
by = Birdy()
by.say()

#查看继承关系的mro列表
result = Birdy.mro()
print(result)



#mixin设计模式

#水果类
class Fruit:
    pass

#南方水果类
class SouthFruit(Fruit):
    pass

#北方水果类
class NorthFruit(Fruit):
    pass

#北方礼物水果
class NorthGiftFruit(NorthFruit):
    pass
#北方非礼物水果
class NorthNotGiftFruit(NorthFruit):
    pass

#南方礼物水果
class SouthGiftFruit(SouthFruit):
    pass
#南方非礼物水果
class SouthNotGiftFruit(SouthFruit):
    pass

#苹果
class Apple(NorthGiftFruit):
    pass

#梨
class Pear(NorthNotGiftFruit):
    pass

#桔子
class Orange(SouthGiftFruit):
    pass

#香蕉
class Banana(SouthNotGiftFruit):
    pass


#多继承
#mixin设计模式

#水果类
class Fruit:
    pass

#南方类
class South:
    pass

#北方类
class North:
    pass

#礼物类
class Gift:
    pass

#非礼物类
class NotGift:
    pass

#苹果类
class Apple(Fruit,North,Gift):
    pass

#梨
class Pear(Fruit,North,NotGift):
    pass

#桔子
class Orange(Fruit,South,Gift):
    pass

#香蕉
class Banana(Fruit,South,NotGift):
    pass



#描述符相关的魔术方法

#描述符类
class Decription:

    #成员属性  共享值的操作
    def __init__(self):
        self.var = 'zhengyang'
    #定义三个操作
    #获取成员属性
    def __get__(self,obj,cls):#self描述符对象  obj接受描述的成员属性username的对象e  cls描述成员属性username所在的类Email
        #print(obj,cls)
        #隐藏名字中间的一个字符
        result = self.var[0]+'*'+self.var[-1]
        return result

    #设置成员属性
    def __set__(self,obj,value):#self描述符对象  obj接受描述的成员属性username的对象e  value设置的值
        #设置时候,默认添加思密达
        self.var = value + '思密达'

    #删除成员属性
    def __delete__(self,obj):#self描述符对象  obj接受描述的成员属性username的对象e
        #删除self.var就可以删除username的访问操作
        #根据密码是否为空决定是否可以删除用户名
        if obj.password == '':
            del self.var
        else:
            pass

class Email:
    #属性
    #希望对用户名进行管控(不是权限管控,而是内容管控)
    username = Decription()#交接操作 将username的操作管控交给描述符类的一个对象
    password = '123456'
    #方法
    def login(self):
        print('登录')
    def logout(self):
        print('注销')

#实例化对象
e = Email()

#获取成员属性
print(e.username)

#设置成员属性
e.username = '张望'
print(e.username)

#删除成员属性
del e.username
print(e.username)


#描述符2
class Email:
    #属性
    #username = ''
    password = ''
    #方法
    def __init__(self):
        #设置var对象成员为描述符的三个方法工作
        self.var = 'yang'

    def login(self):
        print('登录')

    def logout(self):
        print('注销')

    #获取属性的操作
    def getusername(self):
        result = self.var[0] + '*' +self.var[-1]
        return result

    #设置属性的操作
    def setusername(self,value):
        self.var = value

    #删除属性的操作
    def delusername(self):
        #删除的时候对self.var进行操作
        del self.var

    #将username属性交给property指定的函数管理
    username = property(getusername,setusername,delusername)

#实例化对象
e = Email()

#获取成员属性
print(e.username)

#设置成员属性
e.username = 'yangjun'
print(e.username)

#删除成员属性
#del e.username
#print(e.username)


#描述符3
class Email:
    #属性
    #username = ''
    password = ''
    #方法
    def __init__(self):
        #为描述符添加的用于数据通讯的成员属性
        self.var = '匿名'

    def login(self):
        print('登录')
    def logout(self):
        print('注销')

    #获取操作
    @property
    def username(self):
        result = self.var[0] + '*' + self.var[-1]
        return result
    #设置操作
    @username.setter
    def username(self,value):
        self.var = value
    #删除操作
    @username.deleter
    def username(self):
        del self.var

#实例化对象
e = Email()

#获取用户名
print(e.username)

#修改用户名
e.username = 'sun'
print(e.username)

#删除用户名
#del e.username
#print(e.username)





#与属性相关的魔术方法

class Man:
    #属性
    sex = 'man'
    age = 18
    color ='yellow'
    name = 'shizhipeng'

    #方法
    def __init__(self):
        self.gf = 'cortana'
        self.hobby = 'watchTV'

    def chou(self):
        print('piapia')
    def keng(self):
        print('坑娃的')
    '''
    #__getattr__()
   
    触发时机:访问一个不存在的成员属性的时候触发
    功能:1.防止访问不存在成员报错 2.可以为不存在的成员设置默认值
    参数:一个self接受对象  一个参数接受要访问的不存在的成员名
    返回值:可以有可以没有,如果有则是设置了访问的成员的值
    
    def __getattr__(self,attrname):
        #print(attrname)
        if attrname == 'height':
            return '175cm'
        elif attrname =='weight':
            return '75kg'
        else:
            return '对不起,不存在该属性'
    '''
    '''
    #__getattribute__()
    
    触发时机:访问对象成员时触发(无论是否存在)
    功能:可以限制过滤指定成员的值的访问
    参数:一个self接受当前对象  一个接受要访问的成员名
    返回值:可以有,可以没有  推荐根据程序设定(一般有!)
    
    def __getattribute__(self,attrname):

        if attrname == 'name':
            #不能通过当前对象访问成员(访问时绝对不允许使用[对象,成员名]的格式获取)触发递归!
            return object.__getattribute__(self,attrname)
        elif attrname == 'sex':
            return object.__getattribute__(self,attrname)
        else:
            return'对不起,成员不存在或者不允许访问'
    '''

    #__setattr__
    '''
    触发时机:对成员属性进行设置的时候触发
    功能:限制或者过滤对象成员的修改
    参数:一个self接受当前对象  一个接受修改的成员名  一个要修改的成员值
    返回值:没有返回值!
    '''
    def __setattr__(self,attrname,value):
        #可以在设置成员属性时候进行判断
        if attrname == 'sex' or attrname == 'name':
            pass
        else:
            object.__setattr__(self,attrname,value)

    #__delattr__ 魔术方法
    def __delattr__(self,attrname):
        #根据删除的内容决定是否允许删除
        if attrname == 'hobby':
            pass
        else:
            object.__delattr__(self,attrname)

#实例化对象
szp = Man()

'''
#获取对象的成员属性(getattr魔术方法)
print(szp.height)
print(szp.weight)
print(szp.length)
'''

#获取对象的成员属性(getattribute)
#print(szp.color)

#设置成员属性
#szp.sex = 'no man no woman'
#print(szp.sex)

#szp.name = '失了志'
#print(szp.name)

#szp.color = 'black'
#print(szp.color)

#删除成员属性
print(szp.__dict__)
del szp.gf
print(szp.__dict__)


#dir魔术方法
class Human:

    #属性
    sex = 'man'
    age = 18
    name = 'dog'

    #方法
    def eat(self):
        print('吃饭')
    def drink(self):
        print('喝水')

    #__dir__
    def __dir__(self):
        #获取所有可以访问的成员
        lists = object.__dir__(self)
        #过滤魔术方法  只留下自定义成员
        newlists = []
        for i in lists:
            if i.startswith('__') and i.endswith('__'):
                pass
            else:
                newlists.append(i)

        return newlists
#实例化对象
qw = Human()

#获取当前对象中所有存在的成员
result = dir(qw)
print(result)


#其他魔术方法

#自定义我们自己的整型类
class Myint(int):
    '''
    #__add__加法的魔术方法(int类中本来就有)
    def __add__(self,other):
        #print('add方法被触发')
        #print(self,other)
        return int(self) - int(other)
    '''
    #__radd__反向加法的魔术方法(int类中本来就有)
    def __radd__(self, other):
        #print('radd方法被触发')
        return int(self) * int(other)

#实例化对象
no1 = Myint(50)
#result = no1 + 15
#print(result)

'''
#练习:自定义一个整型,相加时进行的运算为10位数相乘+个位数相减
class Myint(int):
    def __add__(self,other):
        return int((self // 10) * (other // 10)) + int(self % 10 - other % 10)

no1 = Myint(18)

result = no1 + 25
print(result)
'''
#反向加法运算__radd__
result = no1 + 40
print(result)
'''
#练习:自定义一个整型,反向相加运算时获取2个数值的个位数的乘积作为结果
class Myint(int):
    def __radd__(self, other):
        return int(self % 10) * int(other % 10)

no1 = Myint(18)
result = 25 + no1
print(result)
'''


#比较运算
class Myint(int):

    #__eq__ 相等魔术方法
    def __eq__(self,other):
        #print('eq方法被触发')
        #print(self,other)
        #自定义规则:如果2个数都能被6整除 相等 其余都不相等
        if self % 6 == 0 and other % 6 == 0:
            return True
        else:
            return False

    #__gt__ 大于比较魔术方法
    def __gt__(self,other):
        if self % 5 > other % 5:
            return True
        else:
            return False
#实例化对象
no1 = Myint(34)
no2 = Myint(63)

#相等运算
result = no1 == no2
print(result)
'''
#练习:只要个位数相等 就相等 其余都不相等
class Myint(int):
    def __eq__(self,other):
        if (self % 10) == (other % 10):
            return True
        else:
            return False
no1 = Myint(12)
no2 = Myint(22)

result = no1 == no2
print(result)
'''
#大于比较运算
result = no1 > no2
print(result)
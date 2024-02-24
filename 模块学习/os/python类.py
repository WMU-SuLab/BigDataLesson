# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 09:52:54 2018

@author: 高治国
"""

#类和对象 
class Human:
    #属性 -> 成员属性(变量)
    ear = 2
    mouth = 1
    sex = 'man'
    age = 28
    name = 'zhangwang'
    married = False
    color = 'yellow'
    #特征 -> 成员方法(函数)
    def walk(self):
        print('直立行走')

    def eat(self):
        print('吃饭')

    def sleep(self):
        print('睡觉')

    def playgame(self):
        print('打游戏')


#查看类的值
print(Human)

#类的类型
print(type(Human))

#实例化对象操作
wangwang = Human()

#打印对象的值
print(wangwang)

#打印对象的类型
print(type(wangwang))

#检测类的成员(在类中声明的成员都可以看到)
print(Human.__dict__)

#检测对象中的成员
print(wangwang.__dict__)
print(wangwang.sex)



class GF:
    #属性
    sex = '女'
    age = 18
    height = '170'
    weight = '50kg'
    threeWei = ('36E','2.1','108CM')
    #方法
    def guang(self):
        print('guang')
    def eat(self):
        print('chi')
    def cry(self):
        print('wu')
#类的基本操作
#访问
print(GF.sex)#属性
GF.eat(1)#方法
#修改
print(GF.age)
GF.age = 22#属性
print(GF.__dict__)
#定义一个函数
'''
def mycry():
    print('Do not cry')
GF.cry = lambda :print('啊呜')#方法
GF.cry = mycry#方法
GF.cry()
'''
#添加
GF.hobby = 'act'#属性
print(GF.__dict__)
GF.upsky = lambda : print('upsky')#方法
GF.upsky()
#删除
del GF.threeWei
print(GF.__dict__)
del GF.cry
print(GF.__dict__)
#对象的基本操作
bingbing = GF()
print(bingbing.__dict__)
#访问
print(bingbing.sex)#属性
bingbing.eat()#方法
#修改
bingbing.age = 28 #属性  修改属性只会影响当前对象本身
print(bingbing.__dict__)
bingbing.cry = lambda : print('bigcry')
print(bingbing.__dict__)
bingbing.cry()
#添加操作
bingbing.cloth = '一袭长裙'#属性
print(bingbing.__dict__)
bingbing.walk = lambda : print('走红毯')#方法
print(bingbing.__dict__)
bingbing.walk()
#删除
bingbing.water = 'more'
bingbing.action = lambda : print('专业演员')
print(bingbing.__dict__)
del bingbing.water#属性
del bingbing.action#方法
print(bingbing.__dict__)



#关于self
'''
通过类调用的函数: 绑定类的方法
通过对象调用的函数: 非绑定类的方法
'''
class Human:
    #属性
    age = 18
    sex = 'female'
    name = 'sanpao'

    #方法
    def eat(self):
        print(self)#通过类来调用的时候self只是函数的一个普通形参,必须给实参!
        print('吃西瓜')

    def drink(self):
        print(self)#通过对象调用的时候self接受的肯定是当前的对象!此处的self不是关键字 只是一个形参,名字可以修改,但是推荐用self
        print('喝西瓜汁')

    #绑定类的方法(肯定)
    def la():
        print('puchi')

    #绑定类的方法/非绑定类的方法(取决于怎么使用)
    def sa(arg):
        print('hualala')

#通过类调用
Human.eat('nidaye')

#通过对象调用
zw = Human
zw.drink(1)

#类来访问sa方法(绑定类的方法)
Human.sa(1)

#通过对象方法sa方法(非绑定类的方法)
zw.sa(1)



#人类
class Human:
    #属性
    age = 18
    #私有化封装成员属性[只能在当前结构中使用]
    __sex = 'male'
    color = 'yellow'
    hair = 'black'

    #方法
    def say(self):
        print('ayi')

    def walk(self):
        print('sousou')

    #私有化成员方法(只能在当前类或者对象的结构中访问)
    def __niao(self):
        print('xuxu')

    #测试:自己访问自己的私有成员
    def demo(self):
        #访问私有方法niao
        self.__niao()
        print('测试私有成员的访问')

#实例化对象
tbw = Human()

#调用tbw的成员
'''
print(tbw.age)
print(tbw.hair)
print(tbw.color)

tbw.say()
tbw.walk()
'''
#相当于别人叫你的名字 想查看你的性别[私有化成员不可以在类/对象的当前结构外访问]
#print(tbw.sex)

#tbw.niao()

#访问测试方法demo[私有化成员可以在类/对象的当前结构中访问]
#tbw.demo()

#Python对私有成员的封装实际上使用了改名策略(name  mangling)
print(Human.__dict__)
print(tbw._Human__sex)
tbw._Human__niao()

print(Human._Human__sex)
Human._Human__niao(1)


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
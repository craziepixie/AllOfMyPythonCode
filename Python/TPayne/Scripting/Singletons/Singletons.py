'''
class MySingleton(object):
        _instance =  None
        def __new__(self):
                if not self._instance:
                        self._instance = super(MySingleton, self).__new__(self)
                        self.y = 10
                return self._instance

x = MySingleton()
print x.y
x.y = 20
z = MySingleton()
print z.y
print x
print MySingleton
'''
def Singleton(myClass):
        instances = {}
        def getInstance(*args, **kwargs):
                if myClass not in instances:
                        instances[myClass] = myClass(*args, **kwargs)
                return instances[myClass]
        return getInstance

@Singleton
class TestClass(object):
        pass
x = TestClass()















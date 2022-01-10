from typing_extensions import ParamSpecArgs


class prevTest():
    pass


class Test(prevTest):
    def __init__(self, name):
        self.name = name
        Test.count = 'ECHO'
    

        
class Test0(Test):

    def __init__(self, name):
        super().__init__(name)
    
    @classmethod
    def add1(cls):
        cls.count += 1
        

a = Test0('hekp')
print(a.name)
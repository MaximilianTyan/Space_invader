class Test():

    
    def __init__(self, name):
        self.name = name
        Test.count = 'ECHO'
    

        
class Test0(Test):

    def __init__(self, name):
        pass
    
    @classmethod
    def add1(cls):
        cls.count += 1
        

a = Test0('1')
print(a.count)
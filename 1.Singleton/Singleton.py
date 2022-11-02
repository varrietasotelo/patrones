class Singleton(object):
    def __new__(type):
        if not '_the_instance' in type.__dict__:
            type._the_instance = object.__new__(type)
        return type._the_instance

a = Singleton()
b = Singleton()
print (id(a), id(b))  

if id(a)== id(b):
    print("Singleton funciona correctamente, ambas variables contienen la misma instancia")
else:
    print("Singleton fallo, las varuables contienen diferentes instancas")

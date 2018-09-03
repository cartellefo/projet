class EmployeeRe:
    'base class for all employees'
    empCount = 0
    
    def __init__(self, name,salary,age):
        self.name = name
        self.salary = salary
        self.age = age
        EmployeeRe.empCount+= 1
        
    def displaycount(self):
        print("Total EmployeeRe %d" % EmployeeRe.empCount)
        
    def displayEmployeeRe(self):
        print("Name :",self.name, "salary :", self.salary, "age :", self.age)


#if __name__ == '__main__':
print("EmployeeRe.__doc__:", EmployeeRe.__doc__)
print("EmployeeRe.__name__:", EmployeeRe.__name__)
print("EmployeeRe.__module__:", EmployeeRe.__module__)
print("EmployeeRe.__bases__:", EmployeeRe.__bases__)
print("EmployeeRe.__dict__:", EmployeeRe.__dict__)
        
#creating instances objects       
emp1 = EmployeeRe("zara",200,25)
emp2 = EmployeeRe("Sven", 100,37)
emp3 = EmployeeRe("marko",100,38)      
emp4 = EmployeeRe("niklas",75,26)



# Add, Remove or modify attribute of classes
#emp1.age = 30
#emp1.große = 140

#del emp1.age


## fonctions to modify the attributes
# getattr(emp1,'age') # returns values of age
# hasattr(emp1,'age') #returns true if 'age' attribute exists
# setattr(emp2,'age', 20)
#delattr(empl,'große') ####  ###

#Accessing Attributes


emp1.displayEmployeeRe()
emp2.displayEmployeeRe()
emp3.displayEmployeeRe()
emp4.displayEmployeeRe()

print("Total EmployeeRe %d" %EmployeeRe.empCount)

# destroying Objects




# class point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         def __del__(self):
#             class_name = self.__class__.__name__
#             print(class_name, "destroyed")
            
# pt1 = point()
# pt2 = pt1
# pt3 = pt1
# print(id(pt1), id(pt2), id(pt3)) # prints the ids of the obejcts
# del pt1
# del pt2
# del pt3
# #print(class_name, "destroyed")

#  #class Inheritance

# class Parent:        # define parent class
#    parentAttr = 100
#    def __init__(self):
#       print( "Calling parent constructor")

#    def parentMethod(self):
#       print( 'Calling parent method')

#    def setAttr(self, attr):
#       Parent.parentAttr = attr

#    def getAttr(self):
#       print( "Parent attribute :", Parent.parentAttr)

# class Child(Parent): # define child class
#    def __init__(self):
#       print( "Calling child constructor")

#    def childMethod(self):
#       print('Calling child method')

# c = Child()          # instance of child
# c.childMethod()      # child calls its method
# c.parentMethod()     # calls parent's method
# c.setAttr(200)       # again call parent's method
# c.getAttr()          # again call parent's method


# ## overriding Methodes
# class Parent:
#     def myMethode(self):
#         print("calling parent methode")
# class Child(Parent):
#     def myMethode(self):
#         print("calling child method")
# c = Child()
# c.myMethode()
                
 

#   #base Overloading Methods
# # __init__(self[,argument...])
# # __del__(self),
# # __repr__(self), repr(obj)
# # __str__(self) str(obj)
# # __cmp__(self,x) object comparison


# class Vector:
#     def __init__(self, a,b):
#         self.a = a
#         self.b = b
#     def __str__(self):
#         return 'Vector (%d,%d)' %(self.a, self.b)
#     def __add__(self,other):
#         return Vector (self.a + other.a,self.b + other.b)
# v1 = Vector(5,15)
# v2 = Vector(18, -20)
# print(v1 + v2)


# class JustCounter:
#     __secretCount =0
#     def count(self):
#         self.__secretCount +=1
#         print(self.__secretCount)
        
# counter = JustCounter()
# counter.count()
# counter.count
# #print(counter.__secretCount)
# print(counter._JustCounter__secretCount)
        




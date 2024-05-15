""""
1.create a python class called circle with constructor which will take a list as an argument for the task.The list is [10,501,22,37,100,999,87,351]
2. create proper member variables inside the task if required and use them when necessary.For example for this task create a class private variab;e named pi=3.141
3. From the given list create two class methods area and perimeter which will be going to calculate the area and perimeter.
"""

class Circle:
    
    # member variable
    pi=3.141

    # constructor
    def __init__ (self,radius_list):
        self.radius_list=radius_list

    def area_of_circle(self,radius):
        return radius * radius * self.pi  

    def perimeter_of_circle(self,radius):
        return radius * self.pi * 2
    
    def calculate_area(self):
        return list(map(self.area_of_circle,self.radius_list))
    
    def calculate_perimeter(self):
        return list(map(self.perimeter_of_circle,self.radius_list))
    

Data=[10,501,22,37,100,999,87,351]

circle=Circle(Data)

Area=circle.calculate_area()
print("Area of Circle list is : ",Area)

Perimeter=circle.calculate_perimeter()
print("Perimeter of a circle list is :" , Perimeter)




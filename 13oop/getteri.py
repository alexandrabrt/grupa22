# class Dog:
#
#     legs_no = 4
#
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return f"{self.name}"
#
#     def change_name(self, name):
#         self.name = name
#
#     @staticmethod
#     def speak():
#         print("Ham ham")
#
#
# # print(Dog.legs_no)
# my_dog = Dog("Max")
# # print(my_dog)
# # print(my_dog.name)
# # print(my_dog.legs_no)
# my_dog.change_name("Rex")
# # print(my_dog)
# # print(my_dog.name)
# my_dog.speak()
# Dog.speak()

class Dog:

    def __init__(self, value):
        self.__name = value

    @property
    def get_name(self):
        return self.__name

    @get_name.setter
    def get_name(self, value1):
        self.__name = value1

    @get_name.deleter
    def get_name(self):
        del self.__name


my_dog = Dog(value='Rex')
# print(my_dog._Dog__name)
print(my_dog.get_name)
my_dog.get_name = "Max"
print(my_dog.get_name)
del my_dog.get_name
print(my_dog.get_name)

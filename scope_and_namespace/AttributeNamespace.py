class MyClass:
    # Class namespace
    class_attr = "I am a class attribute"

    def __init__(self, value):
        # Instance namespace
        self.instance_attr = value


# Accessing class attribute
print(MyClass.class_attr)  # Output: I am a class attribute

# Creating an instance
obj = MyClass("I am an instance attribute")

# Accessing instance attribute
print(obj.instance_attr)  # Output: I am an instance attribute

# Modifying instance attribute
obj.instance_attr = "Modified instance attribute"
print(obj.instance_attr)  # Output: Modified instance attribute

# Deleting instance attribute
del obj.instance_attr
# print(obj.instance_attr)  # This would raise an AttributeError
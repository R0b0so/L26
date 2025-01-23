class Strs:
    def __init__(self):
        self.str1 = "" 
    def get_str(self):
        self.str1 = input("Enter a String")
    def print_String(self):
        print("Result is ",self.str1.upper())
str1 = Strs()
str1.get_str()
str1.print_String()
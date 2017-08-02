def cube(num):
    return num**3

def mod(num):
    if num<0: return -num
    return num

def sum(num1,num2):
    return num1-num2

# import unittest
# 
# class TestCase(unittest.TestCase):
#     def test_cube(self):
#         self.assertEqual(cube(4), 64, "Cubed 4")
#         self.assertEqual(sum(4,3),4, "Print Message")
#         
# unittest.main()
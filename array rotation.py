# If [1,3,5,7,2,4] is your array rotate it with n times

# if n = 2 , then [2,4,1,3,5,7]

"""
Algorithm:
    1)Get the number of rotations to perform on the array
    2)MOVE the last element to the first element and move all the remaining
    elements next to one place
    3) iterate it over N times as got in the first step
"""
class ArrayRotation:
    def __init__(self,rotate):
        self.rotate = rotate
    def rotate_right(self):
        last = array[len(array)-1]
        for i in range(len(array)-1,0,-1):
            array[i] = array[i-1]
        array[0] = last
        print(array)

    def rotate_left(self):
        first = array[0]
        for i in range(len(array) - 1):
            array[i] = array[i + 1]
        array[i + 1] = first
        print(array)

    def action(self):
        print("Rotating array on right: ")
        for i in range(self.rotate):
            self.rotate_right()
        print(f"The array after rotation {array}\n")
        print("Rotating array on left: ")
        for i in range(self.rotate):
            self.rotate_left()

array = [1,2,3,4,5,6,7]
print(f"The Original array before rotation: {array}")
n = int(input("Enter the N to perform rotation: "))
obj = ArrayRotation(n)
obj.action()
print("At the end it gives the original array"
      " after rotating right and left same number of times")
# array = [1,2,3,4,5,6,7] Change this array to [3,4,5,6,7,1,2] by 2 rotation

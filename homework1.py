#Douglas Chi
#Classify triangles and use automated test platform
#Write test cases to test implementation of classifying triangles
def classify_triangle(a, b, c):
    def what_is_triangle_type():
        triangle_type = "scalene"
        if a == b and b == c:
            triangle_type = "equilateral"
        elif a == b or b == c or a == c:
            triangle_type = "isosceles"
        return triangle_type

    def right_triangle():
        sides = [a, b, c]
        sides.sort()
        if sides[0]**2 + sides[1]**2 == sides[2]**2:
            return True
        else:
            return False

    return what_is_triangle_type(), right_triangle()

def test_classify_triangle():

    assert classify_triangle(5, 12, 13) == ('scalene', True)
    assert classify_triangle(7, 7, 7) == ('equilateral', False)
    assert classify_triangle(11, 11, 11) == ('equilateral', False)
    assert classify_triangle(3, 3, 4) == ('isosceles', False)
    assert classify_triangle(3, 4, 5) == ('scalene', True)
    assert classify_triangle(9, 5, 7) == ('scalene', False)
 
print("classify_triangle(5, 12, 13):", classify_triangle(5, 12, 13))
print("classify_triangle(7, 7, 7)):", classify_triangle(7, 7, 7))
print("classify_triangle(11, 11, 11)):", classify_triangle(11, 11, 11))
print("classify_triangle(3, 3, 4)):", classify_triangle(3, 3, 4))
print("classify_triangle(3, 4, 5)):", classify_triangle(3, 4, 5))
print("classify_triangle(9, 5, 7)):", classify_triangle(9, 5, 7))
  
test_classify_triangle()



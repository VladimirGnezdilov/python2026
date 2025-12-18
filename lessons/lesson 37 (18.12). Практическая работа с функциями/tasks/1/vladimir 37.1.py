def rectangle_info(width, height):
    P=(width+height)*2
    S=height*width
    return S, P
print(rectangle_info(10,12))



def is_adult(age):
    if age>=18:
        return True
    else:
        return False
print(is_adult(20))



def safe_div(a, b):
    if b==0:
        return None
    else:
        return a/b
print(safe_div(20,10))

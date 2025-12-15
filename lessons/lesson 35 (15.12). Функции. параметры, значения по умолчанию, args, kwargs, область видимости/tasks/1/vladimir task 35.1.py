def perimeter_rectangle (length,width):
    return length*2+width*2
print(perimeter_rectangle(12,5))


def area_rectangle (length,width):
    return length*width
print(area_rectangle(10,7))




def compare_sizes (length1,width1,length2,width2):
    s1=length1*width1
    s2=length2*width2
    if s1>s2:
        return "Первый больше"
    if s1<s2:
        return "Второй больше"  
    if s1==s2:
        return "Равны"      
print(compare_sizes(10,10,5,5))


elements = [67, 12, 89, 43, 56, 34, 78, 23, 91, 45, 18, 76, 39, 52, 87, 65, 29, 83, 16, 72, 47, 54, 31, 95, 68, 21, 84, 59, 13, 75]


def insertion_sort(elements):
    for i in range(len(elements)):
        j = i
        while j > 0 and elements[j] < elements[j-1]:
            elements[j], elements[j-1] = elements[j-1], elements[j]
            j -= 1
            
    return elements


  
print(insertion_sort(elements))


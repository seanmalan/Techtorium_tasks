

elements = [67, 12, 89, 43, 56, 34, 78, 23, 91, 45, 18, 76, 39, 52, 87, 65, 29, 83, 16, 72, 47, 54, 31, 95, 68, 21, 84, 59, 13, 75]
            
            
def bubble_sort(elements):
  #find the length of the array
    size = len(elements)
    #the function will run through the arry until the second to last element
    for i in range(size-1):
      
        swapped = False
        #we need to run through the second iteration of the array but as the end elements are sorted we dont have to keep checking them so thats why we minus by i
        for j in range(size -1 - i):
          #this is the first element
            a = elements[j]
            #this is the second element since it is the first plus 1
            b = elements[j+1]
            if a > b:
              #if the first element is greater than the second element then we swap them
                elements[j], elements[j+1] = elements[j+1], elements[j]
                swapped = True
        if not swapped:
            break
    return elements
  
print(bubble_sort(elements))


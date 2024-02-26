import time


elements1 = [765, 234, 512, 789, 321, 456, 876, 123, 678, 543,
890, 456, 234, 765, 321, 908, 567, 876, 345, 654,
432, 789, 123, 890, 567, 876, 345, 654, 321, 908,
765, 432, 789, 123, 890, 567, 876, 345, 654, 321,
908, 765, 432, 789, 123, 890, 567, 876, 345, 654]

elements2 = [456, 234, 765, 321, 908, 567, 876, 345, 654, 432,
789, 123, 890, 567, 876, 345, 654, 321, 908, 765,
432, 789, 123, 890, 567, 876, 345, 654, 321, 908,
765, 432, 789, 123, 890, 567, 876, 345, 654, 321,
908, 765, 432, 789, 123, 890, 567, 876, 345, 654]

elements3 = [654, 321, 908, 765, 432, 789, 123, 890, 567, 876,
345, 654, 321, 908, 765, 432, 789, 123, 890, 567,
876, 345, 654, 321, 908, 765, 432, 789, 123, 890,
567, 876, 345, 654, 321, 908, 765, 432, 789, 123,
890, 567, 876, 345, 654, 321, 908, 765, 432, 789]

elements4 = [432, 765, 123, 908, 234, 567, 876, 345, 654, 321,
789, 876, 345, 654, 321, 908, 567, 876, 345, 654,
432, 789, 123, 890, 567, 876, 345, 654, 321, 908,
765, 432, 789, 123, 890, 567, 876, 345, 654, 321,
908, 765, 432, 789, 123, 890, 567, 876, 345, 654,
321, 908, 765, 432, 789, 123, 890, 567, 876, 345,
654, 321, 908, 765, 432, 789, 123, 890, 567, 876,
345, 654, 321, 908, 765, 432, 789, 123, 890, 567,
876, 345, 654, 321, 908, 765, 432, 789, 123, 890,
567, 876, 345, 654, 321, 908, 765, 432, 789, 123,
890, 567, 876, 345, 654, 321, 908, 765, 432, 789,
123, 890, 567, 876, 345, 654, 321, 908, 765, 432,
789, 123, 890, 567, 876, 345, 654, 321, 908, 765,
432, 789, 123, 890, 567, 876, 345, 654, 321, 908,
765, 432, 789, 123, 890, 567, 876, 345, 654, 321,
908, 765, 432, 789, 123, 890, 567, 876, 345, 654,
321, 908, 765, 432, 789, 123, 890, 567, 876, 345,
654, 321, 908, 765, 432, 789, 123, 890, 567, 876,
345, 654, 321, 908, 765, 432, 789, 123, 890, 567]

elements5 = ["apple", "banana", "orange", "grape", "kiwi", "pineapple", "mango", "peach", "pear", "watermelon",
"strawberry", "blueberry", "raspberry", "blackberry", "lemon", "lime", "cherry", "plum", "apricot", "fig",
"grapefruit", "pomegranate", "avocado", "papaya", "coconut", "passionfruit", "guava", "lychee", "dragonfruit",
"persimmon", "raspberry", "blackberry", "strawberry", "cranberry", "blueberry", "elderberry", "gooseberry",
"boysenberry", "currant", "huckleberry", "blackcurrant", "lingonberry", "mulberry", "raspberry", "sloeberry",
"marionberry", "tayberry", "loganberry"]



def bubble_sort(elements):
    size = len(elements)
    for i in range(size - 1):
          swapped = False
          for j in range(size - 1 - i):
             if elements[j] > elements[j + 1]:
                  elements[j], elements[j + 1] = elements[j + 1], elements[j]
                  swapped = True
          if not swapped:
              break
              
start = time.time()
bubble_sort(elements1)
end = time.time()
print("Time for bubble sort: ", end - start)
    
    
def insertion_sort(elements):
       for i in range(1, len(elements)):
           anchor = elements[i]
           j = i - 1
           while j >= 0 and anchor < elements[j]:
               elements[j + 1] = elements[j]
               j = j - 1
           elements[j + 1] = anchor 
        
        

start_time = time.time()
end_time = time.time()
elapsed_time = end_time - start_time
formatted_time = "{:.10f}".format(elapsed_time)
            
start = time.time()
insertion_sort(elements1)
end = time.time()
print("Time for insertion sort: ", formatted_time)
    

start = time.time()
bubble_sort(elements2)
end = time.time()
print("Time for bubble sort: ", end - start)

start = time.time()
insertion_sort(elements2)
end = time.time()
print("Time for insertion sort: ", end - start)


start = time.time()
bubble_sort(elements3)
end = time.time()
print("Time for bubble sort: ", end - start)

start = time.time()
insertion_sort(elements3)
end = time.time()
print("Time for insertion sort: ", end - start)


start = time.time()
bubble_sort(elements4)
end = time.time()
print("Time for bubble sort: ", end - start)

start = time.time()
insertion_sort(elements4)
end = time.time()
print("Time for insertion sort: ", end - start)


start = time.time()
bubble_sort(elements5)
end = time.time()
print("Time for bubble sort: ", end - start)

start = time.time()
insertion_sort(elements5)
end = time.time()
print("Time for insertion sort: ", end - start)
print("the strings have been sorted")

# The bubble sort algorithm is faster than the insertion sort algorithm.
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
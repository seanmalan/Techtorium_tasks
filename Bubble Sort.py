



elements = [
  {"name": "Mona", "transaction_amount": 2000, "device": "iphone-8"},
  {"name": "John", "transaction_amount": 1000, "device": "iphone-10"},
  {"name": "Stacey", "transaction_amount": 4000, "device": "iphone-8"},
  {"name": "Abbey", "transaction_amount": 3000, "device": "iphone-11"},
  {"name": "Abbie", "transaction_amount": 15000, "device": "iphone-11"},
  {"name": "Albert", "transaction_amount": 800, "device": "iphone-11"},
  {"name": "Josh", "transaction_amount": 5700, "device": "iphone-11"},
  {"name": "Sam", "transaction_amount": 6000, "device": "iphone-11"},
  {"name": "David", "transaction_amount": 6200, "device": "iphone-11"},
  {"name": "Rob", "transaction_amount": 9700, "device": "iphone-11"},
  {"name": "Bob", "transaction_amount": 9750, "device": "iphone-11"},
  {"name": "Benny", "transaction_amount": 2450, "device": "iphone-11"},
]




def bubble_sort(elements, key=None):
    size = len(elements)
    for i in range(size-1):
        swapped = False
        for j in range(size -1 - i):
            a = elements[j][key]
            b = elements[j+1][key]
            if a > b:
                elements[j], elements[j+1] = elements[j+1], elements[j]
                swapped = True
        if not swapped:
            break
        
bubble_sort(elements, key="name")

print(elements)


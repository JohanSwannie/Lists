# LISTS - List is a collection which is ordered and changeable. Allows duplicate members
import operator
import itertools

# LIST Constructors
# -----------------

lst1 = list((1, 4, 9, 10, 5, 19, 4))
lst2 = list({'Mother', 'Father', 'Brother', 'Sister'})
lst3 = list(['z', 'p19', [18, 17], True, 18.14])
lst4 = list({1:'s', 2:'z', 3:'p'})
lst5 = list('MammaMia')
lst6 = [1, 'a', True, 'Hallo', [4, 7], False]
lst7 = lst1 + lst2
lst8 = []

# LIST - Access Items + Iterations
# --------------------------------
s = ' '
lst10 = ['lekker', 12, True, [15, 17], 'house', 17.34]
print('some items in list 8 are : ', lst10[1], s, lst10[::-1], s, lst10[1:-1], s, lst10[:4], s, lst10[-4:-2])
print(lst10[3][0])

lst12 = [10, 4, -1, 12, 11, 19, 22, 14, 9, 31, 25, 21, 'disk', 'tape', 'bob']
print('result of sum is : ', list(map(sum, zip([lst12[1], lst12[6]], [lst12[0], lst12[4]]))))

if 'disks' in lst12 or 'tapes' in lst12 or 'bob' in lst12:
    print('yes one of them found in lst12')
else:
    print("Stellie won this round")

print('lst12 items are : ', end='')
for t in lst12:
    print(t, end='  ')
print()
print('length of lst12 is : ', len(lst12))

# Change items in a LIST
# ----------------------

lst13 = ['Orange', 'Blue', 'Green', 'Purple', 'Pink', 'Red', 'Cyan', 'Powderblue']
lst13[4] = 'Gray'

# Add items to a LIST
# -------------------

lst14 = ['Lemon', 'Peach', 'Apple', 'Fig', 'Guava', 'Grape']
lst14.append('Orange')

lst14.insert(2, 'Kiwifruit')

lst14[2] = ['Banana', 'Mango']

# Remove items from a LIST
# ------------------------

lst15 = ['Georgetown', 'Miami', 'Auckland', 'Tauranga', 'Wellington', 'Pretoria']

lst15.remove('Miami')                                             # Remove specified Item

lst15.pop()                                                       # Remove last Item
lst15.pop(2)                                                      # Remove item at Index 2

del lst15[1]                                                      # Remove Item at specified Index

lst15.clear()                                                     # Remove all Items from the LIST

del lst15                                                         # Delete the LIST Completely

# Copy a LIST - join LISTS
# ------------------------

lst16 = ['a', 'f', 'z', 'e', 'r']
lst17 = ['d', 'w', 'q', 'b', 'o']
lst18 = lst16.copy()
lst19 = list(lst16)
lst20 = lst16 + lst17

for x in lst17:
    lst16.append(x)

lst21 = ['Joe', 'Martin', 'Mary', 'Chantelle', 'John']
lst22 = ['Darius', 'Melany', 'Richard', 'Peter']
lst21.extend(lst22)
lst21.extend(['Pumpkin', 'Ball'])

# COUNT in LIST - will return the amount of times an Item occurs in the LIST
# --------------------------------------------------------------------------

lst23 = [4, 11, 18, 4, 19, 22, 10, 4, 7, 5]
print(lst23.count(4))

# INDEX in LIST - will return index of specified Item
# ---------------------------------------------------

lst24 = ['Mathematics', 'Geopgraphy', 'History', 'Biology', 'Programming']
print(lst24.index('History'))

# REVERSE in LIST - will Reverse the LIST
# ---------------------------------------

lst25 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst25.reverse()
print(lst25)

# OR

lst26 = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print('lst26 is now : ', lst26[::-1])

# SORT in LIST
# ------------

lst27 = [119, 44, 35, 10, 91, 4, 18, 7, 71, 22]
lst27.sort()
s1 = sorted(lst27)
lst27.sort(reverse=True)

def sortFunc(x):                                   # Sort with longest Length first
    return len(x)

lst28 = ['BFlat-John', 'AMajor-Kenny', 'CSharp-Melissa', 'DMinor-Bo', 'FMinor-Johnny']

lst28.sort(key=sortFunc, reverse=True)
print(lst28)

# Multi-dimensional LISTS
#------------------------

d = '  -  '
lst29 = [14, 'Hello', True, [19.33, [15, 29, [11, 31, 44]]], 'Python', 'Javascript']
print(lst29[0], d, lst29[3], d, lst29[3][1], d, lst29[3][1][1], d, lst29[3][1][2][2], d, lst29[4])

# LIST Comprehensions
# -------------------

lst30 = [((x * 2) / 8) for x in range(10)]
print(lst30)

lst31 = [char for char in 'Monday' if char != 'a']
print(lst31)

lst32 = list(map(lambda i: i, 'Fantastic'))
print(lst32)

lst33 = [h for h in range(33) if ((h * 3) % 8) == 0 if h != 0]
print(lst33)

lst34 = [j for j in range(100, 300) if j % 11 == 0]
print('lst34 is now  : ', lst34)

lst35 = ['good', 'bad', 'friendly', 'unfriendly', 'love', 'hate', 'compassion', 'coldness', 'yes', 'no']
lst36 = ['badly', 'good', 'nasty', 'friendly', 'love', 'hostile', 'yes']
lst37 = [('True' + ' --> ' + lst36[x]) if lst36[x] in lst35 else False for x in range(7)]
print(lst37)

for x in range(7, 13):
    l = 'lst' + str(x-6)
    lst38 = [j for j in range(1, 145) if j % x == 0]
    print(l, '=', lst38)

print()
print('----------------------------------------------------------------------------------------------')
print()

for i in range(2, 13):
    s = 'lst' + str(i)
    r = i * 12 + 1
    lst39 = [q for q in range(r) if q % i == 0 if q != 0]
    print(s, '=', lst39)



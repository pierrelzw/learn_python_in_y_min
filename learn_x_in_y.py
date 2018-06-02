# negate with not

print(not True) # => False
print(not False) # => True

# Boolean operator

print(True and False) # => False
print(False or True) #=> True

# Note using Bool operators with ints
0lsi and 2
-5 or 0
0 == False
2 == True
1 == True
-5 != False != True # => True

# Equality is ==
1 == 1
2 == 1

# Inequality is !=
1 != 1 #=> False
2 != 1 #=> True

# More comparisons 
1 < 10 # => True
1 > 10 # => False 
2 <= 2 # => True
2 >= 2 # => True

# Comparisons can be cahined! 
1 < 2 < 3 # => True
2 < 3 < 2 # => False

#( is vs. ==) is checks if two variables refer to the same object, but == checks
# if the objects pointed to have the same values.
a = [1, 2, 3, 4] # Point a at a new list, [1, 2, 3, 4]
b = a            # Point b at what a is pointing to 
b is a           # => True, a and b refer to the same object
b == a           # => True, a's and b's object are equal
b = [1, 2, 3, 4] # Point b at a new list, [1, 2, 3, 4]
b is a           # => False, a abd b do not refer to the same object 
b == a           # => True, a's and b's objects are equal

# Strings are crated with " or '

"This is a string."
'This is also a string.'

# String can be added too! But try not to do this.
"Hello " + "world!" #=> "Hello world!"
# String literals(but not variables) can be concatenated without using '+'
"Hello " "world!" #=> "Hello world!" 
a = "Hello " "world!" # this works too!

# A string can be treated like a list of characters
"This is a string"[0] # => 'T'

# You can find the length of a string
len("This is a string")

# .format can be used to format strings, like:
"{} can be {}".format("strings", "interpolated") #=> String can be interpolated"

# You can repeat the formatting arguments to save some typing.
"{0} be nimble, {0} be quick, {0} jump over the {1}".format("Jack", "candle stick")

# You can use keywors if you don't want to count.
"{name} wants to eat {food}".format(name = "Bob", food="lasagna")

# If your Python 3 code also needs to run on Python 2.x and below, you can also still use the old style of formatting:
"%s can be %s the %s way" %("Strings", "interpolated", "old")

# None is a object
None

# Don't use the equality "==" symbol to compare objects to None
# Use "is" instead. This checks for equality of object identity.

"etc" is None # => False
None is None #=> True

# None, 0 and empty strings/lists/dicts/tuples all evaulate to False.
# All other values are True

bool(0) # => False
bool(None) # => False
bool("")  # => False
bool([]) # => False
bool({}) # => False
bool(()) # => False




###############################
### 2. Variables and collections 
###############################

# Simple way to get inot data from console
input_string_var = raw_input("please enter the input string: ") # Return the data as a string

input_var = input("Enter some data: ") # Evaluate the data as python code 
# Warning: Caution is recommended for input() method usage 
# Note: I python3, input() is deprecated and raw_input is renamed to input()


"yahoo!" if 3 > 2 else 2 # => "yahoo!" 

li = []
other_li = [4, 5, 6]

li.append(1) # li is now [1]
li.append(2) # li is now [1, 2]
li.append(4) # li is now [1, 2, 4]
li.append(3) # li is now [1, 2, 4, 3]

li.pop() # li is now [1, 2, 4]

li.append(3) # li is now [1, 2, 4, 3]

li[0] # => 1
li[-1] # => 3

li[1:3] # => [2, 4]
li[2:] # => [4, 3]
li[:3] # => [1, 2, 4]

# Select every second entry
li[::2] # => [1, 4]

# Return a reversed copy of list
li[::-1] # => [3, 4, 2, 1]

# Use any combination of these to make advanced slices
# li[start:end:step]

# make a one layre deep copy using slices

li2 = li[:] # => li2 = [1, 2, 4, 3] but (li2 is li) will result in false.

# Remove arbitary elements from a list with "del"
del li[2] # li is now [1, 2, 3]

# Remove first occurence ofa value 
li.remove(2) # li is now [1,3]
li.remove(2) # Raises a ValueError as 2 is not in the list 

# insert an element at a specific index
li.insert(1, 2) # li is now [1, 2, 3] again

# get the index of the first item found matching the argument 
li.index(2) # => 1
li.index(4) # => Raises a VAlueError as 4 is not in the list

# Add list 
li + li # => return a new list, [1, 2, 3, 1, 2, 3]

li.extend(li)  # => return a new list, [1, 2, 3, 1, 2, 3]

# Check for existence in a list with "in"
1 in li  # => True

# Examine the length with "len()"
len(li) # => 6

# Tuples are like lists but are immutable
tup = (1, 2, 3)
tup[0]       # => 1 
tup[0] = 3   # Raise a TypeError


# Note that a tuple of length one has to have a comma after the last element
# but tuples of other lengths, even zero,  do not

type((1))    # => <class 'int'>
type((1,))   # => <class 'tuple'>
type(())     # => <class 'tuple'>


# you can do most of the list operations on tuples too 
len(tup)
tup + (4, 5, 6)
tup[:2]
2 in tup

# You can unpack tuples( or lists) into variables
a, b, c = (1, 2, 3)# a=1, b=2, c=3

# You can also extend unpacking
a, *b, c = (1, 2, 3, 4) # a=1, b=[2,3], and c=4

# Tuples are crated by default if you leave out the parentheses
d, e, f = 4, 5, 6

# Now look how easy it is to swap two values

e, d = d, e # e is now 4 and d is now 5


# Dictionaries store mappings from keys to values
empty_dict = {}

# Here is a prefilled dictionary
filled_dict = {"one": 1, "two": 2, "three":3}


# Note keys for dictionaries have to be immutable types. This is to ensure that 
# the key can be converted to a constant hash value for quick look-ups
# Immutable types include ints, floats, stings, tuples.
invalid_dict = {[1, 2, 3] : "123"} #=>raise a TypeError: unhashable type: 'list'
valid_dict = {(1, 2, 3) : [1, 2, 3]}

# Look up values with []
filled_dict["one"] # => 1 


# Get all keys as an iterable with "keys()". We need to wrap the call in list()
# to turn it into a list. We'll talk about those later.
# Note - Dictionary key ordering is not guaranteed. You results might not match this exactly.
list(filled_dict.keys())# => ["three", "two", "one"]
list(filled_dict.values()) # => [3, 2, 1]

# Check for existence of keys in a dictionary with "in"
"one" in filled_dict # => True 
1 in filled_dict # => False 

# Looking up a non-existing key is a KeyError
filled_dict['four'] # KeyError

# Use "get()" method to avoid the KeyError
filled_dict.get("one")      # => 1 
filled_fict.get("four")     # => None 


# The get method supports a default argument when the value is missing 
filled_dict.get("one", 4)    # => 1 
filled_dict.get("four", 4)   # => 4

# Remove keys from a dictionary with del
del filled_dict["one"] # Remove the key "one" from filled dict 

# From Python 3.5 you can also use the additonal unpacking options
{'a' : 1, **{'b' : 2}} # => {'a':1, 'b':2}
{'a' : 1, **{'a' : 2}} # => {'a':2}

# Sets store ... well sets
empty_set = set()

# Initialize a set with a bunch of values. Yeah, it looks a bit like a dict.
some_set = {1, 1, 2, 2, 3, 4} # some_set is now {1, 2, 3, 4}

# Similar to keys of a dictionary, elements of a set have to be immutable.
invalid_set = {[1], 1} # => Raises a TypeError: unhashable type: 'list'
valid_set = {(1,), 1}

# add one more item to the set 
filled_set = some_set
filled_set.add(5)  # filled_set is now {1, 2, 3, 4, 5}

# Do set interection with &
other_set = {3, 4, 5, 6}
filled_set & other_set #=> {3,4,5}

# Do set union with |
filled_set | otherset # => {1,2,3,4,5,6}


# Do set difference with -
{1, 2, 3, 4} - {2, 3, 5}   # => {1,4}

# Do set symmetric difference with ^
# symmetric difference = union - difference 
{1, 2, 3, 4} ^ {2, 3, 5}  #{1, 4, 5}

# Check if set on the left is a subset of set on the right
{1, 2} <= {1, 2, 3} # => True

# Check if set on the left is a superset of set on the right
{1, 2} >= {1, 2, 3}

# Check for existence in a set with in
2 in filled_set   # => True
10 in filled_set  # => False










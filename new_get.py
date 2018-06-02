# Don't use the equality "==" symbol to compare objects to None
# Use "is" instead. This checks for equality of object identity.
"etc" is None  # => False
None is None   # => True    

# Select every second entry
li[::2]   # =>[1, 4]

# Return a reversed copy of the list
li[::-1]  # => [3, 4, 2, 1]

# Use any combination of thes to make advanced slices
# li[start:end:step]

# Note that a tuple of length one has to have a comma after the last element but
# tuples of other lengths, even zero, do not.
type((1))   # => <class 'int'>
type((1,))  # => <class 'tuple'>
type(())    # => <class 'tuple'>

a, *b, c = (1, 2, 3, 4)  # a is now 1, b is now [2, 3] and c is now 4


##########
# 3. Control flow
##########

# The object returned by the range function is an iterable

out_iterator = iter(list(1,2,3,4))
print(next(our_iterator))

import array as arr

z=arr.array('i',[1,2,2,3,3,4,4,5,5,5])

print(z)

print("Number of occurrences of the number 5 in the said array: "+str(z.count(5)))



z.reverse()

print(z)

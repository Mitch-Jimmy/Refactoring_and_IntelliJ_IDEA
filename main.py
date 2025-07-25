id = 5
foo = [ 0, 1, 2, 3, 4 ]

# bigger variable
m = 100
bar = []

for i in range(m):
    bar.append(i)

# function to count even numbers
def countEvenNum(arr, size):
    count = 0
    for i in range(size):
        if arr[i] % 2 == 0:
            count += 1
        else:
            #do nothing
            pass
    return count

# call the function
print("The total number of even numbers in foo are: ", countEvenNum(foo, id))
print("The total number of even numbers in bar are: ", countEvenNum(bar, m))

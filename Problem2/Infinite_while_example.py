#!/usr/bin/env python3

start = int(input("Enter the starting index: "))
end = int(input("Enter the last index: "))

if start > end:
    print("Invalid starting and last index !")
else:
    print("The numbers from ",start,"till ",end,"are:")
    
    #Infinite While loop case
    while(True):
        if start > end:
            break
        if start <= end:
            print(start)
            start = start + 1
    

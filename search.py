# Binary search using Python.
# https://teamerror.net

given_list = [1,3,2,4,5,9,8,7,10,50]
given_list.sort()
start=0
end=len(given_list) - 1
mid = (start+end)//2
item = int(input("Enter the number that you want to search:"))
found = False
while( start<=end and not found):
    mid = (start + end)//2
    if given_list[mid] == item :
        print(f"Item found at location {mid}")
        found= True
    else:
        if item < given_list[mid]:
            last = mid - 1
        else:
            start = mid + 1 

if found == False:
    print("Number is not found.")




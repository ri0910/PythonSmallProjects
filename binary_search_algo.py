def binary_search(list, element):
    start = 0
    end = len(list)
    mid = 0
    steps = 0
    while(start <= end):
        steps += 1
        print("Step " + str(steps) + " : " + str(list[start:end+1]))
        mid = (start + end)//2
        if list[mid] == element:
            print(f"Found the element at step {steps} and at position {mid+1} !")
            break
        elif list[mid] > element:
            end = mid - 1
        elif list[mid] < element:
            start = mid + 1
        else:
            print("Did not find the element")

l = [1,2,3,4,5,6,7,8,9,10]
binary_search(l,8)
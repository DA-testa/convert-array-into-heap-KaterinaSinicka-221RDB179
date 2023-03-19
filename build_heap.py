# python3

def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n = len(data)
    
    def scan(index):
        min_index = index
        l_index = 2 * index + 1
        r_index = 2 * index + 2
        if l_index < n and data[l_index]<data[min_index]:
            min_index = l_index
        if r_index < n and data[r_index]<data[min_index]:
            min_index = r_index
        if index != min_index:
            swaps.append((index, min_index))
            data[index], data[min_index] = data[min_index], data[index]
            scan(min_index) 
    for index in range(n// 2, -1, -1):
        scan(index)

    return swaps

def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    # input from keyboard
    text = input("choose 'I' for input or 'F' for file")
    if "I" in text:
        n = int(input())
        data = list(map(int, input().split()))
    if "F" in text:
        f_name = input("Enter file name: ")
        if "a" not in f_name:
            path = './test/' + f_name
            with open(path, 'r', encoding = 'utf-8') as file:
                n = int(file.readLine())
                data = list(map(int, file.readLine().split()))
    # checks if lenght of data is the same as the said lenght
    assert data is not None and len(data) == n
    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)
    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    assert len(swaps) <= n*4
    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()

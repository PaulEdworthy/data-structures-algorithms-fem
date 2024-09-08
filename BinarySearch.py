from typing import List

data = [2, 6, 9, 22, 43, 67, 99]
target = 8
# comment 

def binary_search(data: List[int], target: int) -> bool:
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if target == data[mid]:
            print("Found")
            return True
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    
    print("Not found")
    return False


def main():
    binary_search(data, target)

if __name__ == '__main__':
    main()

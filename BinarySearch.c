#include <stdio.h>

int main()
{
    int nums[] = {2, 6, 9, 22, 43, 67, 99};
    int target = 67;
    int start = 0;
    int mid = 0;
    int end = sizeof(nums);

    while (start <= end)
    {
        mid = start + (end - start) / 2;

        if (nums[mid] == target)
        {
            printf("Found\n");
            return 0;
        }
        else if (target < nums[mid])
        {
            end = mid - 1;
        }
        else 
        {
            start = mid + 1;
        }
    }
    printf("Not found\n");
    return 0;
}
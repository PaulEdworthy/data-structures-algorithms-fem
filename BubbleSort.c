#include <stdio.h>

int main()
{
    char* test = "Paul\n";
    int nums[] = {5, 2, 9, 0, 7};
    int len = sizeof(nums) / sizeof(nums[0]);

    for (int i = 0; i < len; i++)
    {
        for (int j = 0; j < len - 1 - i; j++)
        {
            if (nums[j] > nums[j + 1])
            {
                int temp = nums[j];
                nums[j] = nums[j + 1];
                nums[j + 1] = temp;
            }
        }
    }
    for(int i = 0; i < len; i++)
    {
        printf("%d", nums[i]);
    }
}

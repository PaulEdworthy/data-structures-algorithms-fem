#include <stdio.h>

int main() {
    int haystack[6] = {1, 5, 8, 33, 65, 98};
    int len = sizeof(haystack) / sizeof(haystack[0]);
    int needle = 5;

    for (int i = 0; i < len; i++) {
        if (haystack[i] == needle) {
            printf("Found it!\n");
            return 0;
        }
    }
    printf("Not found\n");
}
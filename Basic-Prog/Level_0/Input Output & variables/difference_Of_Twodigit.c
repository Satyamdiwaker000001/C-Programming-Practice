#include <stdio.h>
int main()
{
    int p, q, result = 0;
    printf("Enter the first number: ");
    scanf("%d", &p);
    printf("Enter the second number: ");
    scanf("%d", &q);
    result = p - q;
    printf("Difference of two integer %d and %d is: %d", p, q, result);

    return 0;
}
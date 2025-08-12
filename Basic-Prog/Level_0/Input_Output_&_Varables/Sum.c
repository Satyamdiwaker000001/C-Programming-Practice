#include <stdio.h>
int main()
{
    int a, b, sum = 0;
    printf("Enter the value of a : ");
    scanf("%d", &a);
    printf("Enter the value of b : ");
    scanf("%d", &b);

    sum = a + b;
    printf("Sum of %d and %d is：%d", a, b, sum);

    return 0;
}
#include <stdio.h>
int main()
{
    int a, b, div = 1;
    printf("Enter the dividend: ");
    scanf("%d", &a);
    printf("Enter the divisor: ");
    scanf("%d", &b);
    div = a / b;
    printf("Quotient: %d\n", div);
    printf("Remainder: %d", a % b);

    return 0;
}
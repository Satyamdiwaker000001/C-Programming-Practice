#include <stdio.h>
int main()
{

    int a;
    int b;
    int rem;
    printf("Enter any integer number(dividend): ");
    scanf("%d", &a);
    printf("Enter any integer number(divisor): ");
    scanf("%d", &b);

    rem = a % b;
    printf("Remainder is: %d", rem);

    return 0;
}
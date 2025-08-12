#include <stdio.h>
void main()
{
    int c;
    int fah;
    printf("Enter temperature in degree celsius: ");
    scanf("%d", &c);
    fah = (c * 9 / 5) + 32;
    printf("Temperature in fahrenheit is: %d deg.", fah);
}
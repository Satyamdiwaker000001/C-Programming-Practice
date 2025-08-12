#include <stdio.h>
float main()
{
    float area = 0.0, a, pie = 3.1428571428571;
    printf("Enter the radius of the circle in cm: ");
    scanf("%f", &a);
    area = pie * a * a;
    printf("The area of the circle is: %.2f cm sqr", area);

    return 0.0;
}
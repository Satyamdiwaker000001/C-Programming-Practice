#include <stdio.h>
int main()
{
    char name[50];
    int roll = 0;
    printf("Enter your roll number: ");
    scanf("%d", &roll);
    printf("Enter your name: ");
    scanf("%s", name);

    printf("Name : %s\n", name);
    printf("Roll No. : %d", roll);
}
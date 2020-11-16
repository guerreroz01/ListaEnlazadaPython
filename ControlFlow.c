#include <stdio.h>
#include <stdbool.h>


int main(void)
{
    bool pizzaIsHealty;

    int temp;
    printf("Do you like pizza?");
    scanf("%d", &temp);

    pizzaIsHealty = temp;
    
    if (pizzaIsHealty) {

      printf("pizza is the best");
      return 0;
    
    }
}

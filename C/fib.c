#include <stdio.h>
#include <stdlib.h>
#include <string.h>

long long fib_rec(int);
long long fib_list(int); /* dynamic programming */

int 
main(void)
{
    printf("fib_rec(35)=%lld\n",fib_rec(35)); /* => 9227465 */
    printf("fib_list(100)=%lld\n",fib_list(100)); /* => 3736710778780434371 */
    return (0);
}

long long 
fib_rec(int n)
{
    if (n <= 1) {
        return (n);
    } else {
        return (fib_rec(n-1) + fib_rec(n-2));
    }
}

long long
fib_list(int n)
{
    long long list[n+1];
    memset(list, 0, n+1);
    list[0] = 0;
    list[1] = 1;
    int i;

    for (i = 2; i <= n; i++) {
        list[i] = list[i-1] + list[i-2];
    }

    return list[n];
}
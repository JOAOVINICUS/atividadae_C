#include <stdio.h>
#define TAMANHO 10

int pilha[TAMANHO];
int topo = -1;

void empilhar(int item)
{
    if (topo >= TAMANHO - 1)
    {
        printf("Overflow da pilha\n");
    }
    else
    {
        pilha[++topo] = item;
        printf("Inserid o -> %d\n", item);
    }
}

int desempilhar()
{
    if (topo < 0)
    {
        printf("Underflow da pilha\n");
        return 0;
    }
    else
    {
        int item = pilha[topo--];
        return item;
    }
}

int main()
{
    int arr[] = {64, 25, 12, 22, 11, 9};
    int n = sizeof(arr) / sizeof(arr[0]);
    for (int i = 0; i < n; i++)
        empilhar(arr[i]);
    for (int i = 0; i < n; i++)
        printf("%d", desempilhar());
    return 0;
}
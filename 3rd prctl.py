#include <stdio.h>

// Swap function
void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

// ---------- MAX HEAP ----------
void maxHeapify(int arr[], int n, int i)
{
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && arr[left] > arr[largest])
        largest = left;

    if (right < n && arr[right] > arr[largest])
        largest = right;

    if (largest != i)
    {
        swap(&arr[i], &arr[largest]);
        maxHeapify(arr, n, largest);
    }
}

void maxHeapSort(int arr[], int n)
{
    // Build Max Heap
    for (int i = n / 2 - 1; i >= 0; i--)
        maxHeapify(arr, n, i);

    // Heap Sort
    for (int i = n - 1; i > 0; i--)
    {
        swap(&arr[0], &arr[i]);
        maxHeapify(arr, i, 0);
    }
}

// ---------- MIN HEAP ----------
void minHeapify(int arr[], int n, int i)
{
    int smallest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && arr[left] < arr[smallest])
        smallest = left;

    if (right < n && arr[right] < arr[smallest])
        smallest = right;

    if (smallest != i)
    {
        swap(&arr[i], &arr[smallest]);
        minHeapify(arr, n, smallest);
    }
}

void reverseArray(int arr[], int n)
{
    int i = 0, j = n - 1;

    while (i < j)
    {
        swap(&arr[i], &arr[j]);
        i++;
        j--;
    }
}

void minHeapSort(int arr[], int n)
{
    // Build Min Heap
    for (int i = n / 2 - 1; i >= 0; i--)
        minHeapify(arr, n, i);

    // Heap Sort
    for (int i = n - 1; i > 0; i--)
    {
        swap(&arr[0], &arr[i]);
        minHeapify(arr, i, 0);
    }

    // Reverse for Ascending Order
    reverseArray(arr, n);
}

// Print array
void printArray(int arr[], int n)
{
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

// Main Function
int main()
{
    int n;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    int arr1[n], arr2[n];

    printf("Enter %d elements:\n", n);

    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr1[i]);
        arr2[i] = arr1[i];
    }

    printf("\nOriginal Array:\n");
    printArray(arr1, n);

    maxHeapSort(arr1, n);
    printf("\nAfter Max Heap Sort (Ascending):\n");
    printArray(arr1, n);

    minHeapSort(arr2, n);
    printf("\nAfter Min Heap Sort (Ascending):\n");
    printArray(arr2, n);

    return 0;
}

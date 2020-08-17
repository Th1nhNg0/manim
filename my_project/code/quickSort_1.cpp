int partition(int a[], int low, int high) {
    int pivot = a[high];
    int i = low;
    for (int j = low; j <= high - 1; j++) {
        if (a[j] < pivot) {
            swap(a[i], a[j]);
            i++;
        }
    }
    swap(a[i], a[high]);
    return i;
}
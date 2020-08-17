void bubbleSort(int n, int a[]) {
    for (int i = n; i > 0; i--) {
        for (int j = 0; j < i - 1; j++)
            if (a[j] > a[j + 1])
                swap(a[j], a[j + 1]);
    }
}
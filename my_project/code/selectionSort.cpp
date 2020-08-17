for (int i = 0; i < n - 1; i++) {
    int iMin = i;
    for (int j = i + 1; j < n; j++)
        if (a[j] < a[iMin])
            iMin = j;
    swap(a[i], a[iMin]);
}
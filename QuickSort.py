def partition(items, low, high):
    i = low - 1
    pivot = items[high][0]  # Menggunakan indeks 0 (nama) sebagai pivot

    for j in range(low, high):
        if items[j][0] <= pivot:
            i += 1
            items[i], items[j] = items[j], items[i]

    items[i + 1], items[high] = items[high], items[i + 1]
    return i + 1

def quick_sort(items, low, high):
    if low < high:
        pivot_index = partition(items, low, high)
        quick_sort(items, low, pivot_index - 1)
        quick_sort(items, pivot_index + 1, high)

# Contoh penggunaan
shopping_list = [("Apel", 10), ("Mangga", 5), ("Pisang", 3), ("Jeruk", 8)]
quick_sort(shopping_list, 0, len(shopping_list) - 1)
print("Hasil pengurutan:")
for item in shopping_list:
    print(item[0], "-", item[1])

    

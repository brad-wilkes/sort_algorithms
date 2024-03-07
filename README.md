# sort_algorithms
Shaker Sort Basic

Shaker Sort algorithm. Shaker Sort is a comparison-based sorting algorithm that works by repeatedly swapping adjacent elements that are out of order. The algorithm starts by comparing the first two elements and swapping them if the first element is greater than the second element. It then compares the second and third elements, and swaps them if the second element is greater than the third element. This process continues until the entire array is sorted.

The code starts by defining a variable n that represents the length of the input array arr. It then initializes two variables swapped and start to True and 0, respectively. The variable end is initialized to n - 1.

The while loop continues until the variable swapped is set to False. Inside the while loop, the code first performs a forward pass, where it compares each adjacent pair of elements and swaps them if the first element is greater than the second element. The code then checks if the array is sorted. If the array is not sorted, the code performs a backward pass, where it compares each adjacent pair of elements in reverse order and swaps them if the second element is greater than the first element.

The code then increments the variable start and decrements the variable end. The loop continues until the array is sorted.

The function returns the sorted array.

Shaker Sort "any"
Implements a variation of the shaker sort algorithm that uses two passes over the array to ensure that all elements are sorted

The code starts by defining two indices, start and end, that track the beginning and end of the unsorted portion of the array. Then, a while loop is used to repeatedly perform two passes over the array.

In the first pass, a for loop is used to iterate over all indices in the unsorted portion of the array. For each index, the element at that index is compared to the element at the next index. If the element at the current index is greater than the element at the next index, then the two elements are swapped. This process is repeated for all indices in the unsorted portion of the array.

After the first pass, a new list is created that contains tuples of indices where the elements were swapped. If this list is empty, then the array is considered to be sorted. If the list is not empty, then a second pass is performed over the array.

In the second pass, a for loop is used to iterate over all indices in the unsorted portion of the array in reverse order. For each index, the element at that index is compared to the element at the previous index. If the element at the current index is greater than the element at the previous index, then the two elements are swapped. This process is repeated for all indices in the unsorted portion of the array.

After both passes are complete, the start and end indices are updated to reflect the new beginning and end of the unsorted portion of the array, and the process is repeated until the array is sorted.


Shaker Sort With Tools:
Implements the Shaker Sort algorithm with additional tools and features to make the sorting process more efficient.

The main idea of the Shaker Sort algorithm is to repeatedly swap adjacent elements that are out of order. The shaker_sort_with_tools function implements this idea by using two nested for loops: a forward pass and a backward pass.

In the forward pass, the function groups the array elements by their values and checks if any group is out of order. If a group is out of order, the function swaps the first and last element of the group. This process is repeated until no more swaps are needed.

In the backward pass, the function groups the array elements in reverse order and checks if any group is out of order. If a group is out of order, the function swaps the last and first element of the group. This process is also repeated until no more swaps are needed.

The function continues to repeat the forward and backward passes until no more swaps are needed.

The function also includes two helper functions: swap and any. The swap function swaps the elements at the given indices, and the any function returns True if any element in the array satisfies the given condition, and False otherwise.

The function also includes a third helper function, groupby, which is used to group the array elements by a given key and iterate over the groups.
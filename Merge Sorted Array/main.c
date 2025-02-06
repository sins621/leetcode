/*
You are given two integer arrays nums1 and nums2, sorted in non-decreasing
order, and two integers m and n, representing the number of elements in nums1
and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be
stored inside the array nums1. To accommodate this, nums1 has a length of m + n,
where the first m elements denote the elements that should be merged, and the
last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming
from nums1.

Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to
ensure the merge result can fit in nums1.

Constraints:

    nums1.length == m + n
    nums2.length == n
    0 <= m, n <= 200
    1 <= m + n <= 200
    -109 <= nums1[i], nums2[j] <= 109

Follow up: Can you come up with an algorithm that runs in O(m + n) time?
*/
#include <stdio.h>

void merge(int *nums_1, int nums_1_size, int m, int *nums_2, int nums_2_size,
           int n);
void print_int(int value);
void print_arr(int *arr, int arr_size);
void shift_right(int *arr, int arr_size, int index);

int main() {
  int arr_1[] = {1, 2, 3, 0, 0, 0};
  const int arr_1_size = 6;
  const int arr_1_max = 3;

  int arr_2[] = {2, 5, 6};
  const int arr_2_size = 3;
  const int arr_2_max = 3;
  merge(arr_1, arr_1_size, arr_1_max, arr_2, arr_2_size, arr_2_max);
  print_arr(arr_1, arr_1_size);
}

void merge(int *nums_1, int nums_1_size, int m, int *nums_2, int nums_2_size,
           int n) {
  int temp = 0;

  if (nums_2_size == 0) {
    return;
  }

  if (m == 0) {
    for (int i = 0; i < nums_2_size; ++i) {
      nums_1[i] = nums_2[i];
    }
    return;
  }

  for (int o = nums_2_size - 1; o > -1; --o) {
    for (int i = nums_1_size - 1; i > -1; --i) {
      if (nums_1[i] != 0) {
        if (nums_2[o] > nums_1[i]) {
          shift_right(nums_1, nums_1_size, i + 1);
          nums_1[i + 1] = nums_2[o];
          break;
        }
      }
    }
  }
}

void print_int(int value) { printf("%d\n", value); }

void print_arr(int *arr, int arr_size) {
  for (int i = 0; i < arr_size; ++i) {
    printf("%d", arr[i]);
  }
  printf("\n");
}

void shift_right(int *arr, int arr_size, int arr_index) {
  int temp_prev = 0;
  int temp_next = 0;
  temp_prev = arr[arr_index];
  arr[arr_index] = 0;
  for (int i = arr_index + 1; i < arr_size; i++) {
    temp_next = arr[i];
    arr[i] = temp_prev;
    temp_prev = temp_next;
  }
}

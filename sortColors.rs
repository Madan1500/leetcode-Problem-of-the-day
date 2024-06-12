fn bubble_sort(nums:&mut Vec<i32>) {
    // Time Complexity: O(n^2)
    let len = nums.len();
    for i in 0..len {
        for j in 0..(len - i - 1) {
            if nums[j] > nums[j + 1] {
                nums.swap(j, j + 1);
            }
        }
    }

}

fn selection_sort(nums:&mut Vec<i32>) {
    // Time Complexity: O(n^2)
    let len = nums.len();
    for i in 0..len {
        let mut min_index = i;
        for j in (i + 1)..len {
            if nums[j] < nums[min_index] {
                min_index = j;
            }
        }
        nums.swap(i, min_index);
    }
}

fn insertion_sort(nums:&mut Vec<i32>) {
    // Time Complexity: O(n^2)
    let len = nums.len();
    for i in 1..len {
        let mut j = i;
        while j > 0 && nums[j] < nums[j - 1] {
            nums.swap(j, j - 1);
            j -= 1;
        }
    }
}

fn merge_sort(nums:&mut Vec<i32>) {
    // Time Complexity: O(nlogn)
    fn merge(nums:&mut Vec<i32>, left:usize, mid:usize, right:usize) {
        let mut left_part = nums[left..mid].to_vec();
        let mut right_part = nums[mid..right].to_vec();
        let mut i = 0;
        let mut j = 0;
        let mut k = left;
        while i < left_part.len() && j < right_part.len() {
            if left_part[i] < right_part[j] {
                nums[k] = left_part[i];
                i += 1;
            } else {
                nums[k] = right_part[j];
                j += 1;
            }
            k += 1;
        }
        while i < left_part.len() {
            nums[k] = left_part[i];
            i += 1;
            k += 1;
        }
        while j < right_part.len() {
            nums[k] = right_part[j];
            j += 1;
            k += 1;
        }
    }

    fn merge_sort_helper(nums:&mut Vec<i32>, left:usize, right:usize) {
        if left + 1 < right {
            let mid = left + (right - left) / 2;
            merge_sort_helper(nums, left, mid);
            merge_sort_helper(nums, mid, right);
            merge(nums, left, mid, right);
        }
    }

    merge_sort_helper(nums, 0, nums.len());
}

fn quick_sort(nums:&mut Vec<i32>) {
    // Time Complexity: O(nlogn)
    fn partition(nums:&mut Vec<i32>, low:usize, high:usize) -> usize {
        let pivot = nums[high];
        let mut i = low;
        for j in low..high {
            if nums[j] < pivot {
                nums.swap(i, j);
                i += 1;
            }
        }
        nums.swap(i, high);
        i
    }

    fn quick_sort_helper(nums:&mut Vec<i32>, low:usize, high:usize) {
        if low < high {
            let pi = partition(nums, low, high);
            if pi > 0 {
                quick_sort_helper(nums, low, pi - 1);
            }
            quick_sort_helper(nums, pi + 1, high);
        }
    }

    quick_sort_helper(nums, 0, nums.len() - 1);
}

fn main() {
    let mut nums = vec![5, 2, 4, 1, 3];
    bubble_sort(&mut nums);
    println!("{:?}", nums);
}
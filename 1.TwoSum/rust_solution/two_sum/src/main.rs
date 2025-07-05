use std::collections::HashMap;

fn main() {
    let nums: Vec<i32> = vec![1, 2, 3, 4, 5];
    let result = two_sum(nums, 8);
    println!("Result is: {:?}", result)
}

pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    let mut map_of_nums: HashMap<i32, usize> = HashMap::new();

    nums.iter().copied().enumerate().for_each(|(index, value)| {
        map_of_nums.insert(value, index);
    });

    let mut results = Vec::new();
    for (i, value) in nums.iter().enumerate() {
        let other_value = target - value;
        let has_other_value = map_of_nums.contains_key(&other_value);
        if has_other_value && (i != map_of_nums[&other_value]) {
            results.push(i as i32);
            results.push(map_of_nums[&other_value] as i32);
            return results
        }
    }
    
    // CLEANER SOLUTION PRODUCED BY CHATGPT
    // if let Some((i, &value)) = nums.iter().enumerate().find(|(i, &value)| {
    //     if let Some(&other_index) = map_of_nums.get(&(target - value)) {
    //         *i != other_index as usize
    //     } else {
    //         false
    //     }
    // }) {
    //     return vec![i as i32, map_of_nums[&(target - value)]];
    // }


    results
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn two_sum_test_1() {
        let input_vec = vec![2, 7, 11, 15];
        let target = 9;
        let expected_output = vec![0, 1];

        let actual_output = two_sum(input_vec, target);
        assert_eq!(expected_output, actual_output);
    }

    #[test]
    fn two_sum_test_2() {
        let input_vec = vec![3, 2, 4];
        let target = 6;
        let expected_output = vec![1, 2];

        let actual_output = two_sum(input_vec, target);
        assert_eq!(expected_output, actual_output);
    }

    #[test]
    fn two_sum_test_3() {
        let input_vec = vec![3, 3];
        let target = 6;
        let expected_output = vec![0, 1];

        let actual_output = two_sum(input_vec, target);
        assert_eq!(expected_output, actual_output);
    }
}

package main

import "fmt"

func main() {
	fmt.Println("Hello, World!")
}

func twoSum(nums []int, target int) []int {

	mapOfNums := make(map[int]int)

	for i := range nums {
		mapOfNums[nums[i]] = i
	}

	other_value := 0
	for i := range nums {
		other_value = target - nums[i]
		index, ok := mapOfNums[other_value]
		if (ok) && (i != index) {
			return []int{i, index}
		}
	}

	return []int{0, 0}
}

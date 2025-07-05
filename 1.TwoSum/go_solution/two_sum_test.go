package main

import "testing"

func TestAdd1(t *testing.T) {
	results := twoSum([]int{2, 7, 11, 15}, 9)
	expected := []int{0, 1}

	checkResults(t, results, expected)
}

func TestAdd2(t *testing.T) {
	results := twoSum([]int{3, 2, 4}, 6)
	expected := []int{1, 2}

	checkResults(t, results, expected)
}

func TestAdd3(t *testing.T) {
	results := twoSum([]int{3, 3}, 6)
	expected := []int{0, 1}

	checkResults(t, results, expected)
}

func checkResults(t *testing.T, results []int, expected []int) {
	if len(results) != len(expected) {
		t.Errorf("Result %q, Expected %q", results, expected)
	}

	for i := range results {
		if results[i] != expected[i] {
			t.Errorf("Result %q, Expected %q", results, expected)
		}
	}
}

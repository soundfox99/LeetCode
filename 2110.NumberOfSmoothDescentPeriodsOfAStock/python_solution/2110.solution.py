from typing import List

def getDescentPeriods(prices: List[int]) -> int:

        result = 0
        def helper(
            prices: List[int],
            start_index: int,
            end_index: int,
            result: int) -> int:
            
            if end_index - start_index > 0:
                if end_index >= len(prices):
                    return 0
                
                if prices[end_index] - prices[end_index - 1] > 1:
                    return 0

            result += helper(
                prices,
                start_index,
                end_index + 1,
                result
            ) + 1

            result += helper(
                prices,
                start_index + 1,
                end_index + 1,
                result
            ) + 1

            return result

        result = helper(
            prices,
            0,
            0,
            result
        )

        return result


def main():
    test_case_input_1 = [3,2,1,4]
    test_case_output_1 = 7
    computed_output = getDescentPeriods(test_case_input_1)
    assert test_case_output_1 == computed_output

if __name__ == "__main__":
    main()
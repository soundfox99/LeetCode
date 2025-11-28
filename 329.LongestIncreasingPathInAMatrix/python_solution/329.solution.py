from typing import List


def longestIncreasingPath(matrix: List[List[int]]) -> int:
    
    def helper(
        matrix: List[List[int]],
        cache: dict[tuple[int, int], int],
        current_position: tuple[int, int]
    ) -> int:
        
        if current_position in cache:
            return cache[current_position]
        
        can_move_right: bool = (len(matrix[0]) > current_position[1] + 1) and matrix[current_position[0]][current_position[1]] < matrix[current_position[0]][current_position[1] + 1]
        can_move_left: bool = (0 <= current_position[1] - 1) and matrix[current_position[0]][current_position[1]] < matrix[current_position[0]][current_position[1] - 1]
        can_move_up: bool = (0 <= current_position[0] - 1) and matrix[current_position[0]][current_position[1]] < matrix[current_position[0] - 1][current_position[1]]
        can_move_down: bool = (len(matrix) > current_position[0] + 1) and matrix[current_position[0]][current_position[1]] < matrix[current_position[0] + 1][current_position[1]]

        if not can_move_right and not can_move_left and not can_move_up and not can_move_down:
            cache[current_position] = 1
            return cache[current_position]
        
        max_path_length = 0
        if can_move_right:
            path_length = helper(
                matrix=matrix,
                cache=cache,
                current_position=tuple([current_position[0], current_position[1] + 1])
            ) + 1
            max_path_length = max(max_path_length, path_length)
        if can_move_left:
            path_length = helper(
                matrix=matrix,
                cache=cache,
                current_position=tuple([current_position[0], current_position[1] - 1])
            ) + 1
            max_path_length = max(max_path_length, path_length)
        if can_move_up:
            path_length = helper(
                matrix=matrix,
                cache=cache,
                current_position=tuple([current_position[0] - 1, current_position[1]])
            ) + 1
            max_path_length = max(max_path_length, path_length)
        if can_move_down:
            path_length = helper(
                matrix=matrix,
                cache=cache,
                current_position=tuple([current_position[0] + 1, current_position[1]])
            ) + 1
            max_path_length = max(max_path_length, path_length)

        cache[current_position] = max_path_length
        return cache[current_position]
            
    cache: dict[tuple[int, int], int] = {}

    max_path_length = 0
    for m in range(len(matrix)):
        for n in range(len(matrix[m])):
            max_path_length = max(
                max_path_length,
                helper(
                    matrix=matrix,
                    cache=cache,
                    current_position=(m, n)
                )
            )

    return max_path_length



def main():
    matrix = [[9,9,4],[6,6,8],[2,1,1]]
    result = longestIncreasingPath(
        matrix=matrix
    )
    assert result == 4

    matrix = [[3,4,5],[3,2,6],[2,2,1]]
    result = longestIncreasingPath(
        matrix=matrix
    )
    assert result == 4

    matrix = [[1]]
    result = longestIncreasingPath(
        matrix=matrix
    )
    assert result == 1

if __name__ == "__main__":
    main()
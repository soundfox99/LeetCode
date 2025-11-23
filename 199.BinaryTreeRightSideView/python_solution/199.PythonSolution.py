from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        final_result = []
        tree_layer = 0

        return self._rightSideViewHelper(
            result = final_result,
            tree_layer = tree_layer,
            node = root
        )

    def _rightSideViewHelper(
        self,
        result: list[int],
        tree_layer: int,
        node: Optional[TreeNode]
    ) -> list[int]:

        if node is None:
            return result

        result = self._modify_result_list(
            result = result,
            current_tree_layer = tree_layer,
            current_node_value = node.val
        )
        self._rightSideViewHelper(
            result = result,
            tree_layer = tree_layer + 1,
            node = node.left
        )
        self._rightSideViewHelper(
            result = result,
            tree_layer = tree_layer + 1,
            node = node.right
        )

        return result

    def _modify_result_list(
        self,
        result: list[int],
        current_tree_layer: int,
        current_node_value: int
    ) -> list[int]:

        if current_tree_layer < len(result):
            result[current_tree_layer] = current_node_value
        elif current_tree_layer == len(result):
            result.append(current_node_value)
        else:
            print("Something is not right with your modify_result_list function")

        return result
        

def _convert_list_to_tree(
    input_list: list[int],
    current_position: int,
) -> Optional[TreeNode]:

    if current_position > len(input_list) or input_list[current_position - 1] is None:
        return None

    node = TreeNode()
    node.val = input_list[current_position - 1]
    node.left = _convert_list_to_tree(
        input_list,
        current_position * 2
    )
    node.right = _convert_list_to_tree(
        input_list,
        (current_position * 2) + 1
    )

    return node


def main():
    # Test solution

    examples = [
        ([1,2,3,None,5,None,4], [1,3,4]),
        ([1, 2, 3, 4, None, None, None, 5],[1, 3, 4, 5]),
        ([1, None, 3],[1, 3]),
        ([],[]),
    ]

    for input, output in examples:
        solution = Solution()
        root = _convert_list_to_tree(input, 1)
        assert(
            solution.rightSideView(root) == output
        )


if __name__ == "__main__":
    main()
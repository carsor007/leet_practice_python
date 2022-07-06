def findSubsets(arr, n)->list[str]:
    # Base case
    if n == 0:
        return [""]
    # If there is only one element in array
    if n == 1:
        return [str(i) for i in arr]
    # If there are more than one element in array
    else:
        # Get all subsets of array of size n-1
        subsets = findSubsets(arr, n-1)
        # Get all subsets of array of size n-1
        subsets_1 = findSubsets(arr, n-2)
        # Concatenate all subsets of array of size n-1 with all subsets of array of size n-2
        return [str(i) + str(j) for i in subsets for j in subsets_1]




class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: TreeNode)->int:
    if root is None:
        return 0
    else:
        left_height = maxDepth(root.left)
        right_height = maxDepth(root.right)
        return max(left_height, right_height) + 1
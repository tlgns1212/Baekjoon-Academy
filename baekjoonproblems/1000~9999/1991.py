class Tree:
    def __init__(self, me, left, right):
        self.data = me
        self.left = left
        self.right = right

def preorder(head):
    print(head.data, end = "")
    if head.left != ".":
        preorder(tree[head.left])
    if head.right != ".":
        preorder(tree[head.right])

def inorder(head):
    if head.left != ".":
        inorder(tree[head.left])
    print(head.data, end = "")
    if head.right != ".":
        inorder(tree[head.right])

def postorder(head):
    if head.left != ".":
        postorder(tree[head.left])
    if head.right != ".":
        postorder(tree[head.right])
    print(head.data, end = "")

N = int(input())
tree = {}
for _ in range(N):
    stuff = input().split()
    tree[stuff[0]] = Tree(stuff[0],stuff[1],stuff[2])
preorder(tree["A"])
print()
inorder(tree["A"])
print()
postorder(tree["A"])

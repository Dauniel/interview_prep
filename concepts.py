class ListNode:
    def __init__(self, value: int = 0, next = None):
        self.value = value
        self.next = next

node2 = ListNode(2)
node3 = ListNode(3)


x = [1,2,3,4,5]
print(x[:4])

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
x = fib(5)
print(x)


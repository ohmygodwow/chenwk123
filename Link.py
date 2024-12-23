import sys


# 定义链表的数据结构
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    # 将数组转为链表结构


def generate_node(nums):
    # 定义一个哑节点
    p_head = ListNode(1)
    temp_head = p_head
    for num in nums:
        temp = ListNode(num)
        temp_head.next = temp
        temp_head = temp_head.next
    return p_head.next

if __name__ == "__main__":
    nums_1 = [2,4,9]
    nums_2 = [5,6,4,9]
    linkx = ListNode(0)
    l3 = linkx
    headA = generate_node(nums_1)
    headB = generate_node(nums_2)
    A=[]
    B=[]
    while headA != None:
        A.append(headA.val)
        headA = headA.next
    while headB != None:
        B.append(headB.val)
        headB = headB.next
    print(A)
    print(B)
    num_A=int(''.join(map(str,A))[::-1])
    num_B=int(''.join(map(str,B))[::-1])
    sum_AB=num_A+num_B
    print(sum_AB)
    # sumx = str(sum_AB)[::-1]
    # for i in sumx:
    #     l3.next = ListNode(int(i))
    #     l3 = l3.next
    # linkx=linkx.next
    # while linkx != None:
    #     print(linkx.val)
    #     linkx = linkx.next




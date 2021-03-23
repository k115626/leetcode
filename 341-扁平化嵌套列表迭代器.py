"""
解题思路：
1. 使用队列和递归
2. 使用yield和yield from
   for i in range(10):
       yield i
         ||
   yield from range(10)
"""

# 思路1
# from queue import Queue
# que = Queue()
# def gen(nestedList):
#     for i in nestedList:
#         if i.isInteger():
#             que.put(i.getInteger())
#         else:
#             gen(i.getList())

# class NestedIterator:
#     def __init__(self, nestedList: [NestedInteger]):
#         gen(nestedList)
#         self.que = que
    
#     def next(self) -> int:
#         if self.hasNext():
#             return self.que.get()
    
#     def hasNext(self) -> bool:
#         if self.que.empty():
#             return False
#         return True


# 思路2
def gen(nestedList):
    for i in nestedList:
        if i.isInteger():
            yield i.getInteger()
        else:
            yield from gen(i.getList())

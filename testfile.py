from createstack import stack
from createstack import stack_pop

def testcase():
    assert(stack()) == [45, 66]
    assert(stack_pop()) == [66,32]





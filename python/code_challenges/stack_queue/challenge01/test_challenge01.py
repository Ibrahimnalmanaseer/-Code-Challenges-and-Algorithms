# Write your test here
from challenge01 import MyQueue


def test_queue_push():

    object_1=MyQueue()
    object_1.push(1)
    object_1.push(2)
    object_1.push(3)
    object_1.push(4)

    actual=object_1.queue
    expect=[1,2,3,4]
    assert actual == expect




def test_queue_pop():

    object_1=MyQueue()
    object_1.push(1)
    object_1.push(2)
    object_1.push(3)
    object_1.push(4)
    
    actual=object_1.pop(),object_1.queue
    expect=1,[2,3,4]
    assert actual == expect



def test_queue_peek():

    object_1=MyQueue()
    object_1.push(1)
    object_1.push(2)
    actual=object_1.peek()
    expect= 1
    assert actual == expect


def test_queue_empty():

    object_1=MyQueue()
    object_1.push(1)
    object_1.push(2)
    actual=object_1.empty()
    expect= False
    assert actual == expect
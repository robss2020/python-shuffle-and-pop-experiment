## Changing pop() to tracking a head doesn't improve speeds. Why is pop() so smart?

I was running a monte carlo experiment that included shuffling lists and then reading the results one by one.

Since pop() returns a new list with one less element on it, I thought I would get a huge speedup by removing
pop() and just keeping track of the subscript (via a headat "pointer" holding a subscript.)

For example https://docs.python.org/3/tutorial/datastructures.html mentions "Remove the item at the given position in the list, and return it."
Removing an item seems like a pretty expensive operation! After all, I couldn't imagine that it is implemented as a linked list, since you can
randomly access any element.

## The experiment

I shuffled 10,000,000 items in a list and then pop()'d them off one by one, repeating the experiment 100 times.
Next I tried the alternative approach of keeping track of a headat variable to see what subscript we're at.  That wouldn't require any mutation of the list!


## The expectation

I was expecting a huge speedup when I stopped mutating the list and just kept track of the index I'm at.


## Results

The results of all 100 runs was:

`Finished  100  runs of shuffling and popping from  10000000  elements in  1036.0079972743988 seconds.`

`Finished  100  runs of shuffling and manually 'popping' via headat tracking from  10000000  elements in  1037.989679813385 seconds.`

Since we were doing 100 runs that is an average of 10.36 seconds via popping and 10.37 seconds without mutating the list at all.
Not terribly bad for handling and shuffling a list of 10m items, but no speedup from removing the pop().


## Pretty chart

My flatline in all its glory.  Notice the conspicuous lack of speedup!

![ Comparison of pop()-ing versus tracking a headat pointer.](https://github.com/robss2020/python-shuffle-and-pop-experiment/blob/main/comparison.png "Flatline")


## Investigating how it does it

A quick ChatGPT query told me that the pop() is implemented here:

https://github.com/python/cpython/blob/main/Objects/listobject.c

To me it still looks like it's moving things around a bit, in this line:

`if ((size_after_pop - index) > 0) {`
            `memmove(&items[index], &items[index+1], (size_after_pop - index) * sizeof(PyObject *));`
        `}`


How can ten million memmoves not be any more expensive than just not doing them at all?

Well, whatever the answer is saving, those memmoves doesn't save any time. pop() is no more expensive than not doing the pop() at all, so there are no savings to be had here.
It is pretty fast.


# Conclusions
Changing pop() to keeping track of a head pointer doesn't give any speed benefit. For whatever reason, the way Python implements lists itself makes a pop() operation just as fast.
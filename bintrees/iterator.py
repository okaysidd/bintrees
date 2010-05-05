#!/usr/bin/env python
#coding:utf-8
# Author:  Mozman
# Purpose: iterator provides a TreeIterator for binary trees
# Created: 04.05.2010

class TreeIterator(object):
    __slots__ = ['_tree', '_direction', '_item', '_retfunc', ]
    def __init__(self, tree, rtype='key', reverse=False):
        """
        Params:

        tree -- a binary tree, required methods: min_item, max_item, prev_item, succ_item
        rtype -- 'key', 'value', 'item'
        reverse -- False: ascending order; True: descending order
        """
        self._tree = tree
        self._item = None
        self._direction = -1 if reverse else +1

        if rtype == 'key':
            self._retfunc = lambda item: item[0]
        elif rtype == 'value':
            self._retfunc = lambda item: item[1]
        elif rtype == 'item':
            self._retfunc = lambda item: item
        else:
            raise ValueError("Unknown return type '{0}'".format(rtype))

    @property
    def key(self):
        return self._item[0]

    @property
    def value(self):
        return self._item[1]

    @property
    def item(self):
        return self._item

    def __iter__(self):
        return self

    def next(self):
        return self._step(1)

    def prev(self):
        return self._step(-1)

    def _step(self, steps):
        if self._item is None:
            if self._direction == -1:
                self._item = self._tree.max_item()
            else:
                self._item = self._tree.min_item()
        else:
            step_dir = self._direction * steps
            step_func = self._tree.succ_item if step_dir > 0 else self._tree.prev_item
            try:
                self._item = step_func(self._item[0])
            except KeyError:
                raise StopIteration
        return self._retfunc(self._item)

    def goto(self, key):
        node = self._tree.find_node(key)
        if node is not None:
            self._item = (node.key, node.value)
        else:
            raise KeyError(unicode(key))
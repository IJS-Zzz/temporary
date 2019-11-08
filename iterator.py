# -*- coding: utf-8 -*-


class Iterator((object)):
    def __init__(self, iterable, even=False):
        self._step = 2
        self._first = 0 if not even else 1
        self._iter = None
        self._items = iterable

    def __iter__(self):
        return self

    def __next__(self):
        try:
            if not self._iter:
                self._iter = iter(self._items)
                self._skip(self._first)
                return next(self._iter)

            self._skip(self._step - 1)
            return next(self._iter)
        except StopIteration:
            self._iter = None
            raise

    next = __next__  # for Python 2

    def _skip(self, n):
        if not self._iter:
            return

        for _ in range(n):
            next(self._iter)


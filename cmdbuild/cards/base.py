'''
Copyright 2023 Paolo Smiraglia <paolo.smiraglia@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to
deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
sell copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
IN THE SOFTWARE.
'''

import logging

from restfly.endpoint import APIEndpoint

LOG = logging.getLogger(__name__)


class CardsIterator:
    # query parameters
    _page = 0
    _start = 0
    _limit = 50

    # total number of cards
    total = 1

    # cards of the current page
    page = []

    # consumed items (total)
    count = 0

    # consumed items (page)
    page_count = 0

    # debug
    _pages_requested = 1

    def __init__(self, api, path, **kwargs):
        self._api = api
        self._path = path

    def _get_page(self):
        # make the API call
        resp = self._get_data()

        # obtain total number of cards
        meta = resp.get('meta')
        self.total = meta.get('total')

        # reset the cards counter for the current page
        self.page_count = 0

        # get the cards
        self.page = resp.get('data', [])

        # debug
        LOG.debug(f'Requested pages: {self._pages_requested}')
        LOG.debug(f'Records in current page: {len(self.page)}')
        LOG.debug(f'Total records: {self.total}')
        self._pages_requested += 1

    def _get_data(self):
        # build the query
        query = {}
        query['page'] = self._page
        query['start'] = self._start
        query['limit'] = self._limit

        # make the API call
        resp = self._api.get(self._path, params=query).json()

        # increase query parameters
        self._start += self._limit
        self._page += 1

        return resp

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        # ending conditions
        if self.count >= self.total:
            raise StopIteration()

        if self.page_count >= len(self.page) and self.count <= self.total:
            self._get_page()
            if len(self.page) == 0:
                raise StopIteration()

        # consume the iterator
        item = self.page[self.page_count]
        self.count += 1
        self.page_count += 1

        LOG.debug(f'Consumed {self.count}/{self.total} cards')
        return item


class Card(APIEndpoint):
    _class_id = None

    def __init__(self, api):
        self._path = f'classes/{self._class_id}/cards'
        super(Card, self).__init__(api)

    def list(self, **kwargs):
        return CardsIterator(self._api, self._path)

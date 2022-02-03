#
#  Copyright © 2022 Ingram Micro Inc. All rights reserved.
#

from cachetools import LFUCache

from lark import Lark
from lark.exceptions import LarkError

from py_rql.exceptions import RQLFilterParsingError
from py_rql.grammar import RQL_GRAMMAR


class RQLLarkParser(Lark):
    def __init__(self, *args, **kwargs):
        super(RQLLarkParser, self).__init__(*args, **kwargs)

        self._cache = LFUCache(maxsize=1000)

    def parse_query(self, query):
        cache_key = hash(query)
        if cache_key in self._cache:
            return self._cache[cache_key]
        try:
            rql_ast = self.parse(query)
            self._cache[cache_key] = rql_ast
            return rql_ast
        except LarkError:
            raise RQLFilterParsingError()


RQLParser = RQLLarkParser(RQL_GRAMMAR, parser='lalr', start='start')
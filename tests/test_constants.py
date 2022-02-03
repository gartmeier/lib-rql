#
#  Copyright © 2022 Ingram Micro Inc. All rights reserved.
#

from py_rql.constants import FilterLookups

import pytest


@pytest.mark.parametrize('func', ('numeric', 'string', 'boolean'))
def test_filter_lookups_non_null(func):
    result = getattr(FilterLookups, func)()
    result.discard(FilterLookups.NULL)

    assert result == getattr(FilterLookups, func)(with_null=False)
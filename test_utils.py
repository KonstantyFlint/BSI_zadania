from math import exp

import pytest
import utils


@pytest.mark.parametrize('time,failure_rate,anticipated_result',
                         [
                             (10, 0.4, lambda t: exp(-1 * 0.4 * t)),

                         ])
def test_z_1_a(time, failure_rate, anticipated_result):
    tested_function = utils.make_reliability_function(failure_rate)
    assert tested_function(time) == anticipated_result(time)

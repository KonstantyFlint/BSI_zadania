from math import exp, log

import pytest
import utils


@pytest.mark.parametrize('time,failure_rate,anticipated_result',
                         [
                             (10, 0.4, lambda t: exp(-1 * 0.4 * t)),
                             (1067, 0.84, lambda t: exp(-1 * 0.84 * t)),
                             (23, 0.05, lambda t: exp(-1 * 0.05 * t)),
                         ])
def test_make_reliability_function(time, failure_rate, anticipated_result):
    tested_function = utils.make_reliability_function(failure_rate)
    assert tested_function(time) == anticipated_result(time)


@pytest.mark.parametrize('time, tested_time, reliability,anticipated_result',
                         [
                             (23, 100, 0.85, utils.make_reliability_function(log(0.85) / 23 / -1)),
                         ])
def test_deduce_reliability_function(time, tested_time, reliability, anticipated_result):
    failure_rate = log(reliability) / time / -1
    tested_function = utils.make_reliability_function(failure_rate)
    assert tested_function(tested_time) == anticipated_result(tested_time)

from math import sqrt
from pytest import approx

import pytest
import functions


@pytest.mark.parametrize('reliability_m,time_m,time_r,anticipated_result',
                         [
                             (0.97, 100, 200, approx(0.9409, 0.001)),
                             (0.97, 200, 100, sqrt(0.97)),

                         ])
def test_z_1_a(reliability_m, time_m, time_r, anticipated_result):
    assert functions.z_1_a(reliability_m, time_m, time_r) == anticipated_result


@pytest.mark.parametrize('reliability_m,time_m,time_survived,time_r,anticipated_result',
                         [
                             (0.97, 100, 900, 1000, approx(0.97, 0.001)),
                             (0.8, 80, 500, 1100, approx(0.1876, 0.001))
                         ])
def test_z_1_b(reliability_m, time_m, time_survived, time_r, anticipated_result):
    assert functions.z_1_b(reliability_m, time_m, time_survived, time_r) == anticipated_result


@pytest.mark.parametrize('failure_rate_a, failure_rate_b, count, time,anticipated_result',
                         [
                             (0.00000005, 0.00000025, 5000, 350, {0.08750000000000001, 0.4375}),
                             # ()
                         ])
def test_z_2(failure_rate_a, failure_rate_b, count, time, anticipated_result):
    assert functions.z_2(failure_rate_a, failure_rate_b, count, time) == anticipated_result


@pytest.mark.parametrize('failure_rate, time_survived, time_r,anticipated_result',
                         [
                             (0.0001, 100, 300, approx(0.98, 0.01)),
                             # ()
                         ])
def test_z_3(failure_rate, time_survived, time_r, anticipated_result):
    assert functions.z_3(failure_rate, time_survived, time_r) == anticipated_result


@pytest.mark.parametrize('reliability, time,anticipated_result',
                         [
                             (0.95, 500,
                              {'failure rate': approx(0.0001, 0.00000000001), 'MTBF': approx(10000, 0.0000001)})
                         ])
def test_z_4(reliability, time, anticipated_result):
    assert functions.z_4(reliability, time) == anticipated_result


@pytest.mark.parametrize('failure_rate, warranty_fail,anticipated_result',
                         [
                             (0.4, 0.05, approx(0.128, 0.01))
                         ])
def test_z_5(failure_rate, warranty_fail, anticipated_result):
    assert functions.z_5(failure_rate, warranty_fail) == anticipated_result

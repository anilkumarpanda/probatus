import numpy as np
import pandas as pd

import pytest

from pyrisk.utils import assure_numpy_array, check_1d, DimensionalityError


def test_check_numpy_array_list():
    x = [1, 2, 3]
    x_array = assure_numpy_array(x)
    assert isinstance(x_array, np.ndarray)
    np.testing.assert_array_equal(x_array, np.array(x))


def test_check_numpy_array_array():
    x = np.array([1, 2, 3])
    x_array = assure_numpy_array(x)
    assert isinstance(x_array, np.ndarray)
    np.testing.assert_array_equal(x_array, x)


def test_check_numpy_array_dataframe():
    x = pd.DataFrame({'x': [1, 2, 3]})
    x_array = assure_numpy_array(x)
    assert isinstance(x_array, np.ndarray)
    np.testing.assert_array_equal(x_array, np.array([1, 2, 3]))


def test_check_numpy_array_series():
    x = pd.Series([1, 2, 3])
    x_array = assure_numpy_array(x)
    assert isinstance(x_array, np.ndarray)
    np.testing.assert_array_equal(x_array, np.array([1, 2, 3]))


def test_check_1d_list():
    x = [1, 2, 3]
    assert check_1d(x)
    _ = [[1, 2], [1, 2, 3]]
    assert pytest.raises(DimensionalityError)
    _ = [1, [1, 2, 3]]
    assert pytest.raises(DimensionalityError)


def test_check_1d_array():
    x = np.array([1, 2, 3])
    assert check_1d(x)
    _ = np.array([[1, 2], [1, 2, 3]])
    assert pytest.raises(DimensionalityError)
    _ = np.array([0, [1, 2, 3]])
    assert pytest.raises(DimensionalityError)


def test_check_1d_dataframe():
    x = pd.DataFrame({'x': [1, 2, 3]})
    assert check_1d(x)
    _ = pd.DataFrame({'x': [1, 2, 3], 'y': [1, 2, 3]})
    assert pytest.raises(DimensionalityError)
    _ = pd.DataFrame({'x': [1, 2, 3, [4, 5]]})
    assert pytest.raises(DimensionalityError)


def test_check_1d_series():
    x = pd.Series([1, 2, 3])
    assert check_1d(x)
    _ = pd.Series([1, [2, 3]])
    assert pytest.raises(DimensionalityError)
    _ = pd.Series([[1], [2, 3]])
    assert pytest.raises(DimensionalityError)
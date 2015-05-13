#!/usr/bin/python3

import os

import pytest

import environmental


class Configuration:
    no_default = environmental.Int('INT_NO_DEFAULT')
    bool = environmental.Bool('BOOL', False)
    complex = environmental.Complex('COMPLEX', complex(1, 1))
    float = environmental.Float('FLOAT', 42.2)
    integer = environmental.Int('INT', 42)
    list = environmental.List('LIST', [])
    set = environmental.Set('SET', {1, 2, 3})
    string = environmental.Str('STR', 'test string')
    tuple = environmental.Tuple('TUPLE', (1, 2, 3))


def test_no_default():
    config = Configuration()

    with pytest.raises(AttributeError):
        integer = config.no_default


def test_bool():
    config = Configuration()

    assert isinstance(config.bool, bool)
    assert not config.bool
    config.bool = True
    assert isinstance(config.bool, bool)
    assert config.bool
    assert isinstance(os.environ['BOOL'], str)
    assert os.environ['BOOL'] == 'True'

    with pytest.raises(ValueError):
        config.bool = 1

    os.environ['BOOL'] = 'False'
    assert config.bool is False


def test_complex():
    config = Configuration()

    assert isinstance(config.complex, complex)
    assert config.complex == complex(1, 1)
    config.complex = complex(2, 2)
    assert isinstance(config.complex, complex)
    assert config.complex == complex(2, 2)
    assert isinstance(os.environ['COMPLEX'], str)
    assert os.environ['COMPLEX'] == '(2+2j)'

    config.complex = 1
    assert isinstance(config.complex, complex)
    assert config.complex == complex(1, 0)
    assert os.environ['COMPLEX'] == '(1+0j)'

    os.environ['COMPLEX'] = '(4+2j)'
    assert config.complex == complex(4, 2)

    with pytest.raises(ValueError):
        config.complex = 'random string'


def test_float():
    config = Configuration()

    assert isinstance(config.float, float)
    assert config.float == 42.2
    config.float = 1.2
    assert isinstance(config.float, float)
    assert config.float == 1.2
    assert isinstance(os.environ['FLOAT'], str)
    assert os.environ['FLOAT'] == '1.2'

    config.float = 1
    assert config.float == 1.0
    assert os.environ['FLOAT'] == '1.0'

    os.environ['FLOAT'] = '12.3'
    assert config.float == 12.3

    with pytest.raises(ValueError):
        config.float = 'random string'


def test_int():
    config = Configuration()

    assert isinstance(config.integer, int)
    assert config.integer == 42
    config.integer = 1
    assert isinstance(config.integer, int)
    assert config.integer == 1
    assert isinstance(os.environ['INT'], str)
    assert os.environ['INT'] == '1'

    with pytest.raises(ValueError):
        config.integer = 'a'

    os.environ['INT'] = 'a'
    with pytest.raises(ValueError):
        integer = config.integer


def test_list():
    config = Configuration()

    assert isinstance(config.list, list)
    assert config.list == []
    config.list.append('1')
    assert config.list == ['1']
    assert 'LIST' not in os.environ   # changing a mutable object will not change the environment
    config.list = config.list  # but reassigning will
    assert os.environ['LIST'] == "['1']"

    with pytest.raises(ValueError):
        config.list = 'a'

    os.environ['LIST'] = 'a'
    with pytest.raises(ValueError):
        l = config.list


def test_set():
    config = Configuration()

    assert isinstance(config.set, set)
    assert config.set == {1, 2, 3}
    config.set.add('4')
    assert config.set == {1, 2, 3, '4'}
    assert 'SET' not in os.environ   # changing a mutable object will not change the environment
    config.set = config.set  # but reassigning will
    assert len(os.environ['SET']) == len("{1, 2, 3, '4'}")

    with pytest.raises(ValueError):
        config.set = 'a'

    os.environ['SET'] = 'a'
    with pytest.raises(ValueError):
        l = config.set


def test_tuple():
    config = Configuration()

    assert isinstance(config.tuple, tuple)
    assert config.tuple == (1, 2, 3)
    config.tuple = (4, 5)
    assert isinstance(config.tuple, tuple)
    assert config.tuple == (4, 5)
    assert os.environ['TUPLE'] == "(4, 5)"

    with pytest.raises(ValueError):
        config.tuple = 'a'

    os.environ['TUPLE'] = 'a'
    with pytest.raises(ValueError):
        l = config.tuple

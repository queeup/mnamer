import pytest

from mnamer.setting_spec import SettingSpec
from mnamer.types import SettingType

pytestmark = pytest.mark.local


def test_setting_spec__serialize__default():
    default = {
        "action": None,
        "choices": None,
        "dest": None,
        "flags": None,
        "group": SettingType.PARAMETER,
        "help": None,
        "nargs": None,
        "type": None,
    }
    setting_spec = SettingSpec(SettingType.PARAMETER)
    assert setting_spec.as_dict() == default


def test_setting_spec__serialize__override():
    spec = {
        "action": "count",
        "choices": ["a", "b", "c"],
        "dest": "foo",
        "flags": ["-f", "--foo"],
        "group": SettingType.PARAMETER,
        "help": "foos your bars",
        "nargs": "+",
        "type": int,
    }
    setting_spec = SettingSpec(**spec)
    assert setting_spec.as_dict() == spec


def test_setting_spec__registration():
    spec = {
        "dest": "foo",
        "flags": ["-f", "--f"],
        "group": SettingType.DIRECTIVE,
        "help": "foos your bars",
    }
    setting_spec = SettingSpec(**spec)
    args, kwargs = setting_spec.registration
    assert args == ["-f", "--f"]
    assert kwargs == {"dest": "foo", "help": "foos your bars"}

import sys
import types

# Provide stubs for optional dependencies
sys.modules.setdefault('magic', types.ModuleType('magic'))
sys.modules.setdefault('requests', types.ModuleType('requests'))
bs4_stub = types.ModuleType('bs4')
bs4_stub.BeautifulSoup = type('BeautifulSoup', (), {})
sys.modules.setdefault('bs4', bs4_stub)
dateparser_stub = types.ModuleType('dateparser')
dateparser_stub.parse = lambda *args, **kwargs: None
sys.modules.setdefault('dateparser', dateparser_stub)
dcj_stub = types.ModuleType('dataclasses_json')
dcj_stub.dataclass_json = lambda *args, **kwargs: (lambda cls: cls)
sys.modules.setdefault('dataclasses_json', dcj_stub)
aenum_stub = types.ModuleType('aenum')
import enum as _enum
aenum_stub.MultiValueEnum = _enum.Enum
sys.modules.setdefault('aenum', aenum_stub)

# Expose the src directory as the 'stips' package so we can import the code
stips_pkg = types.ModuleType('stips')
stips_pkg.__path__ = ['src']
sys.modules.setdefault('stips', stips_pkg)

from stips.client import StipsClient
import stips.utils as utils


class DummyHTTP:
    def post(self, **kwargs):
        self.kwargs = kwargs
        return kwargs


def test_ask_uses_link_param():
    client = StipsClient()
    client.cookies = {'dummy': '1'}  # bypass cookie requirement
    client.http = DummyHTTP()

    result = client.ask('title', link='https://example.com')

    assert result['params']['q_link'] == 'https://example.com'


def test_ask_uses_qlink_link_helper():
    client = StipsClient()
    client.cookies = {'dummy': '1'}
    client.http = DummyHTTP()

    original = utils.qlink_link
    utils.qlink_link = lambda link: f'transformed:{link}'
    try:
        result = client.ask('title', link='value')
    finally:
        utils.qlink_link = original

    assert result['params']['q_link'] == 'transformed:value'

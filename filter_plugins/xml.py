# pylint: disable=too-few-public-methods

import traceback
import xmlplain
from ansible import errors


def to_pretty_plain_xml(src_obj):
    plain_xml_str = None
    try:
        plain_xml_str = xmlplain.xml_from_obj(src_obj).decode("utf-8")
    except Exception as xml_exception:
        exc_msg = "to_pretty_plain_xml(): Cannot convert obj to xml:\n%s" % traceback.format_exc()
        raise errors.AnsibleFilterError(exc_msg) from xml_exception
    return plain_xml_str


class FilterModule():
    filter_map = {
        'to_pretty_plain_xml': to_pretty_plain_xml
    }

    def filters(self):
        return self.filter_map

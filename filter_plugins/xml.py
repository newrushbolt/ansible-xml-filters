# pylint: disable=too-few-public-methods,missing-module-docstring

import traceback
import xmlplain
from ansible import errors


def to_pretty_plain_xml(src_obj, src_codepage="utf-8"):
    # pylint: disable=trailing-whitespace
    """
    Ansible filter-plugin to format data structure to XML.

    EXAMPLE:
    ```
    - hosts: localhost
      gather_facts: false
      become: false
      vars:
        config_struct:
          sizes:
            '@extra': mutable
            height: '960'
            weight: '1440'
      tasks:
        - debug:
            msg: "{{ config_struct | to_pretty_plain_xml() }}"
    ```

    KNOWN ISSUES:
    * According to XML your should have exact one root-level key.
    * No numeric data types allowed, nor booleans.  
      You can use ONLY dicts and strings.  
      Although you can use lists they are useless in XML:
        ```
        # Raw data
        sizes:
            - test1
            - test2

        # XML
            <?xml version="1.0" encoding="UTF-8"?>
            <sizes>test1test2</sizes>
        ```
    * You can set XML-attributes by prefixing @ to name of a key:
        ```
        # Raw data
        sizes:
            '@extra': mutable
            data: some_data

        # XML
        <?xml version="1.0" encoding="UTF-8"?>
        <sizes extra="mutable">
            <data>some_data</data>
        </sizes>
        ```
    """
    plain_xml_str = None
    try:
        plain_xml_str = xmlplain.xml_from_obj(src_obj).decode(src_codepage)
    except Exception as xml_exception:
        exc_msg = "to_pretty_plain_xml(): Cannot convert obj to xml:\n%s" % traceback.format_exc()
        raise errors.AnsibleFilterError(exc_msg) from xml_exception
    return plain_xml_str


class FilterModule():
    """Ansible interface class"""
    filter_map = {
        'to_pretty_plain_xml': to_pretty_plain_xml
    }

    def filters(self):
        """Ansible interface function"""
        return self.filter_map

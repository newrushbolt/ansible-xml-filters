#! /bin/env python3


import re
import sys
import logging

from filter_plugins import xml

README_END_MARK = 'AUTOGEN_MARK -->'

src_readme = ""
try:
    src_readme = sys.stdin.read()
except Exception as exc:
    logging.error("Cannot read from stdin: %s", exc)
if src_readme == "":
    logging.error("No input read. Pass me a readme file.")
    sys.exit(1)
end_mark_index = src_readme.index(README_END_MARK)
if end_mark_index == -1:
    logging.error("Readme end phrase '%s' is not found in readme.", README_END_MARK)
    sys.exit(1)
end_mark_end = end_mark_index + len(README_END_MARK)
dst_readme = src_readme[:end_mark_end]

ansible_modules = {}
try:
    ansible_modules = xml.FilterModule().filters()
except Exception as exc:
    logging.error("Cannot read ansible modules: %s", exc)
if len(ansible_modules) == 0:
    logging.error("Imported file has no ansible modules")
    sys.exit(1)

modules_doc = ""
for module_name, module_function in ansible_modules.items():
    untabbed_function_doc = re.sub(r"^    ", "", module_function.__doc__, flags=re.MULTILINE)
    doc_header = f"\n\n### {module_name}\n\n"
    module_doc = doc_header + untabbed_function_doc
    modules_doc = modules_doc + module_doc
dst_readme = dst_readme + modules_doc
print(dst_readme)

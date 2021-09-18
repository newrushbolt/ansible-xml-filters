# ansible-xml-filters

## Installation

First you need to install requirements:  
`pip install -r requirements.txt`

You have two options installing filters:

### Copying to your playbook directory (prefered)

By default ansible is searching for `*_plugins` directories in your `playbook_dir`.
Just copy `filter_plugins` folder to your playbook directory, and you are good to go.

### Using PATH for filter_plugins

Plugin must be placed in directory where ansible is looking for filter_plugins.  
You can check configured path like this:
`ansible-config dump|grep DEFAULT_FILTER_PLUGIN_PATH`
You can either copy plugin to configured directory or modify Ansbile `FILTER_PLUGIN_PATH` via config\env.
https://docs.ansible.com/ansible/2.9/reference_appendices/config.html#default-filter-plugin-path

## to_pretty_plain_xml

_Get doc:_  
`python -c 'import re; from filter_plugins import xml; print(re.sub(r"^    ", "", xml.to_pretty_plain_xml.__doc__, flags=re.MULTILINE))'`

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

## Plugins
Docs below are docstrings from filter_plugins/xml.py, glued here by `apply_docstring_to_readme.py`
DO NOT EDIT THEM BY HAND!
To update README run:
`python apply_docstring_to_readme.py < README.md > NEW_README.md`
<!-- AUTOGEN_MARK -->

### to_pretty_plain_xml


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


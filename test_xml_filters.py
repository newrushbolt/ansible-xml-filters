import subprocess


test_playbook_body = """
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
    - copy:
        content: "{{ config_struct | to_pretty_plain_xml() }}"
        dest: .test_data.xml
"""

test_playbook_output = """<?xml version="1.0" encoding="UTF-8"?>
<sizes extra="mutable">
  <height>960</height>
  <weight>1440</weight>
</sizes>
"""


def setup():
    with open(".test_playbook.yml", "w") as playbook_file:
        playbook_file.write(test_playbook_body)

def test_to_pretty_plain_xml():
    test_result = subprocess.run(["ansible-playbook", ".test_playbook.yml"], capture_output=True)
    assert test_result.returncode == 0

    with open(".test_data.xml", 'r') as data_file:
      raw_file = data_file.read()
      assert raw_file == test_playbook_output

#!/usr/bin/env python
import re
import sys

# TODO: Fix me

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

module_name = "{{ cookiecutter.directory_name}}"

if not re.match(MODULE_REGEX, module_name):
    print(
        "ERROR: (%s) is not a valid Python module name. Please do not use a - and use _ instead"
        % module_name
    )

    # Exit to cancel project
    sys.exit(1)

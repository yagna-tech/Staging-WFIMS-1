#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "pursuite.settings.settings"
    )

    PROJECT_ROOT = os.path.dirname(__file__)
    sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))

    #from django.core.management import execute_from_command_line
    from configurations.management import execute_from_command_line

    execute_from_command_line(sys.argv)

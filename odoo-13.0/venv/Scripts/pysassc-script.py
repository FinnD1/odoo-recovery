#!c:\users\admin\downloads\compressed\odoo-13.0\odoo-13.0\venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'libsass==0.22.0','console_scripts','pysassc'
__requires__ = 'libsass==0.22.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('libsass==0.22.0', 'console_scripts', 'pysassc')()
    )

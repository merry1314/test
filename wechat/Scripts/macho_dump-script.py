#!E:\pythonProject\weixin\wechat\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'macholib==1.11','console_scripts','macho_dump'
__requires__ = 'macholib==1.11'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('macholib==1.11', 'console_scripts', 'macho_dump')()
    )

#!C:\Users\cdt\PycharmProjects\camera_control\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'opencv-iav==0.0.3','console_scripts','opencv_iav'
__requires__ = 'opencv-iav==0.0.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('opencv-iav==0.0.3', 'console_scripts', 'opencv_iav')()
    )

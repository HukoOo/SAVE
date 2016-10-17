from PyQt4 import uic
import os
import sys
import subprocess

print uic

subprocess.call('python /usr/lib/python2.7/dist-packages/PyQt4/uic/pyuic.py -x UI/mainwindow.ui -o ~/PycharmProjects/pyqt/main_window.py', shell=True)

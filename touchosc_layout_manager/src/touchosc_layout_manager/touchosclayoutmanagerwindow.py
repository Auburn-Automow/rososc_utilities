#!/usr/bin/env python

"""
This module provides a wrapper and some implementation to the main windows ui.
"""

import sys, os

from logging import debug, info, warning, error

try:
    import roslib; roslib.load_manifest('touchosc_layout_manager')
    setattr(sys, 'SELECT_QT_BINDING', 'pyside')
    from rosgui.QtBindingHelper import loadUi
except Exception:
    error("Couldn't load ROS or rosgui", exc_info=1)
    # TODO: Try loading with out rosgui's QtBindingHelper
    sys.exit(-1)

from PySide import QtCore, QtGui

class TouchOSCLayoutManagerWindow(QtGui.QMainWindow):
    """This class represents the Main Window of the application"""
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        ui_file = os.path.dirname(os.path.realpath(__file__))
        ui_file = os.path.join(ui_file, 'touchosclayoutmanagerwindow.ui')
        
        loadUi(ui_file, self)
    

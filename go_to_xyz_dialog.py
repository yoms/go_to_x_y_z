# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GoToXYZDialog
                                 A QGIS plugin
 Create a polygon on XYZ bbox
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-04-02
        git sha              : $Format:%H$
        copyright            : (C) 2020 by Guillaume Hormière
        email                : hormiere.guillaume@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets, QtGui

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'go_to_xyz_dialog_base.ui'))


class GoToXYZDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(GoToXYZDialog, self).__init__(parent)
        self.setupUi(self)
        self.z_lineEdit.setValidator(QtGui.QIntValidator(self.z_lineEdit))
        self.x_lineEdit.setValidator(QtGui.QIntValidator(self.x_lineEdit))
        self.y_lineEdit.setValidator(QtGui.QIntValidator(self.y_lineEdit))

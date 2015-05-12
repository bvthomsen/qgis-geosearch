# -*- coding: utf-8 -*-
"""
/***************************************************************************
Name                 : geosearch_dk
Description          : Search suggestions in QGIS using GST's geosearch service
Date                 : 24-05-2013
copyright            : (C) 2013 by Septima
author               : asger@septima.dk
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 3 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui_settings import Ui_Dialog

MUNCODE_REGEX = '[0-9,]*'

class SettingsDialog (QDialog, Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        
        regex = QRegExp('', Qt.CaseInsensitive)
        self.muncodeValidator = QRegExpValidator( MUNCODE_REGEX )
        self.kommunekoderLineEdit.setValidator( self.muncodeValidator, self.kommunekoderLineEdit )

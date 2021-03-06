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

# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog

from searchbox import SearchBox


class SeptimaGeoSearch:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface

        # initialize plugin directory
        self.plugin_dir = QFileInfo(QgsApplication.qgisUserDbFilePath()).path() + "/python/plugins/" + __package__

        # config
        self.config = QSettings()

        # initialize locale
        localePath = ""
        locale = self.config.value("locale/userLocale")[0:2]

        if QFileInfo(self.plugin_dir).exists():
            localePath = self.plugin_dir + "/i18n/" + locale + ".qm"

        if QFileInfo(localePath).exists():
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

    def initGui(self):
        # create the widget to display information
        self.searchwidget = SearchBox(self.iface)
        # create the dockwidget with the correct parent and add the valuewidget
        self.searchdockwidget = QDockWidget(
            "Geosearch DK", self.iface.mainWindow()
        )
        self.searchdockwidget.setObjectName("Geosearch DK")
        self.searchdockwidget.setWidget(self.searchwidget)
        # add the dockwidget to iface
        self.iface.addDockWidget(
            Qt.TopDockWidgetArea, self.searchdockwidget
        )

        # Menu items
        self.configAction = QAction(
            QIcon(),
            QCoreApplication.translate('Geosearch DK', "&Indstillinger"),
            self.iface.mainWindow()
        )
        self.aboutAction = QAction(
            QIcon(),
            QCoreApplication.translate('Geosearch DK', "&Om pluginet"),
            self.iface.mainWindow()
        )

        self.configAction.triggered.connect(
            self.searchwidget.show_settings_dialog
        )
        self.aboutAction.triggered.connect(self.searchwidget.show_about_dialog)

        self.iface.addPluginToMenu("Geosearch DK", self.configAction)
        self.iface.addPluginToMenu("Geosearch DK", self.aboutAction)

    def unload(self):
        self.searchwidget.unload() # try to avoid processing events, when QGIS is closing
        self.iface.removePluginMenu("Geosearch DK", self.configAction)
        self.iface.removePluginMenu("Geosearch DK", self.aboutAction)
        self.iface.removeDockWidget(self.searchdockwidget)

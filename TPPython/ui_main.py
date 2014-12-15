# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/coccie/TPPython/annuaire_view.ui'
#
# Created: Mon Sep 29 16:11:02 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Annuaire_view(object):
    def setupUi(self, Annuaire_view):
        Annuaire_view.setObjectName(_fromUtf8("Annuaire_view"))
        Annuaire_view.resize(978, 376)
        self.centralWidget = QtGui.QWidget(Annuaire_view)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.lineEdit = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(6, 7, 871, 24))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(887, 6, 85, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.treeWidget = QtGui.QTreeWidget(self.centralWidget)
        self.treeWidget.setGeometry(QtCore.QRect(6, 37, 971, 231))
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 270, 111, 41))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.pushButton_2 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.message = QtGui.QLabel(self.centralWidget)
        self.message.setGeometry(QtCore.QRect(260, 274, 131, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.message.setFont(font)
        self.message.setStyleSheet(_fromUtf8("color: rgb(85, 170, 0);"))
        self.message.setObjectName(_fromUtf8("message"))
        Annuaire_view.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(Annuaire_view)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 978, 22))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuContact = QtGui.QMenu(self.menuBar)
        self.menuContact.setObjectName(_fromUtf8("menuContact"))
        Annuaire_view.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(Annuaire_view)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        Annuaire_view.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(Annuaire_view)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        Annuaire_view.setStatusBar(self.statusBar)
        self.toolBar = QtGui.QToolBar(Annuaire_view)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        Annuaire_view.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtGui.QToolBar(Annuaire_view)
        self.toolBar_2.setObjectName(_fromUtf8("toolBar_2"))
        Annuaire_view.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.actionNouveau = QtGui.QAction(Annuaire_view)
        self.actionNouveau.setObjectName(_fromUtf8("actionNouveau"))
        self.actionSupprimer = QtGui.QAction(Annuaire_view)
        self.actionSupprimer.setObjectName(_fromUtf8("actionSupprimer"))
        self.actionExtraire_CSV = QtGui.QAction(Annuaire_view)
        self.actionExtraire_CSV.setObjectName(_fromUtf8("actionExtraire_CSV"))
        self.actionNouveau_2 = QtGui.QAction(Annuaire_view)
        self.actionNouveau_2.setObjectName(_fromUtf8("actionNouveau_2"))
        self.actionSupprimer_2 = QtGui.QAction(Annuaire_view)
        self.actionSupprimer_2.setObjectName(_fromUtf8("actionSupprimer_2"))
        self.actionSupprimer_3 = QtGui.QAction(Annuaire_view)
        self.actionSupprimer_3.setObjectName(_fromUtf8("actionSupprimer_3"))
        self.actionSupprimer_4 = QtGui.QAction(Annuaire_view)
        self.actionSupprimer_4.setObjectName(_fromUtf8("actionSupprimer_4"))
        self.actionSupprimer_5 = QtGui.QAction(Annuaire_view)
        self.actionSupprimer_5.setObjectName(_fromUtf8("actionSupprimer_5"))
        self.actionImport_CSV = QtGui.QAction(Annuaire_view)
        self.actionImport_CSV.setObjectName(_fromUtf8("actionImport_CSV"))
        self.actionModifier = QtGui.QAction(Annuaire_view)
        self.actionModifier.setObjectName(_fromUtf8("actionModifier"))
        self.menuContact.addAction(self.actionNouveau)
        self.menuContact.addAction(self.actionModifier)
        self.menuContact.addAction(self.actionExtraire_CSV)
        self.menuBar.addAction(self.menuContact.menuAction())

        self.retranslateUi(Annuaire_view)
        QtCore.QMetaObject.connectSlotsByName(Annuaire_view)

    def retranslateUi(self, Annuaire_view):
        Annuaire_view.setWindowTitle(_translate("Annuaire_view", "TPAnnuaire", None))
        self.lineEdit.setText(_translate("Annuaire_view", "Recherche", None))
        self.pushButton.setText(_translate("Annuaire_view", "OK", None))
        self.treeWidget.headerItem().setText(0, _translate("Annuaire_view", "Nom", None))
        self.treeWidget.headerItem().setText(1, _translate("Annuaire_view", "Prénom", None))
        self.treeWidget.headerItem().setText(2, _translate("Annuaire_view", "Email ", None))
        self.treeWidget.headerItem().setText(3, _translate("Annuaire_view", "Téléphone", None))
        self.treeWidget.headerItem().setText(4, _translate("Annuaire_view", "Adresse", None))
        self.treeWidget.headerItem().setText(5, _translate("Annuaire_view", "Ville", None))
        self.treeWidget.headerItem().setText(6, _translate("Annuaire_view", "Code", None))
        self.treeWidget.headerItem().setText(7, _translate("Annuaire_view", "Groupe", None))
        self.pushButton_2.setText(_translate("Annuaire_view", "Supprimer", None))
        self.message.setText(_translate("Annuaire_view", "Export réussi ! ", None))
        self.message.setVisible(False)
        self.menuContact.setTitle(_translate("Annuaire_view", "Contact", None))
        self.toolBar.setWindowTitle(_translate("Annuaire_view", "toolBar", None))
        self.toolBar_2.setWindowTitle(_translate("Annuaire_view", "toolBar_2", None))
        self.actionNouveau.setText(_translate("Annuaire_view", "Nouveau", None))
        self.actionSupprimer.setText(_translate("Annuaire_view", "Supprimer", None))
        self.actionExtraire_CSV.setText(_translate("Annuaire_view", "Export CSV", None))
        self.actionNouveau_2.setText(_translate("Annuaire_view", "Nouveau", None))
        self.actionSupprimer_2.setText(_translate("Annuaire_view", "Supprimer", None))
        self.actionSupprimer_3.setText(_translate("Annuaire_view", "Supprimer", None))
        self.actionSupprimer_4.setText(_translate("Annuaire_view", "Supprimer", None))
        self.actionSupprimer_5.setText(_translate("Annuaire_view", "Supprimer", None))
        self.actionImport_CSV.setText(_translate("Annuaire_view", "Import CSV", None))
        self.actionModifier.setText(_translate("Annuaire_view", "Modifier", None))


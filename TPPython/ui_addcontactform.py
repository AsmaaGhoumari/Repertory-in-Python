# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/coccie/TPPython/uiaddcontactform.ui'
#
# Created: Mon Sep 29 00:15:00 2014
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

class Ui_uiAddContactForm(object):
    def setupUi(self, uiAddContactForm):
        uiAddContactForm.setObjectName(_fromUtf8("uiAddContactForm"))
        uiAddContactForm.resize(305, 327)
        self.formLayoutWidget = QtGui.QWidget(uiAddContactForm)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 14, 281, 306))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.name = QtGui.QLineEdit(self.formLayoutWidget)
        self.name.setObjectName(_fromUtf8("name"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.name)
        self.firstname = QtGui.QLineEdit(self.formLayoutWidget)
        self.firstname.setObjectName(_fromUtf8("firstname"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.firstname)
        self.mail = QtGui.QLineEdit(self.formLayoutWidget)
        self.mail.setObjectName(_fromUtf8("mail"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.mail)
        self.label_5 = QtGui.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_5)
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.comboBox = QtGui.QComboBox(self.formLayoutWidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.comboBox)
        self.label_4 = QtGui.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.phone = QtGui.QLineEdit(self.formLayoutWidget)
        self.phone.setObjectName(_fromUtf8("phone"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.phone)
        self.label_7 = QtGui.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_7)
        self.buttonBox = QtGui.QDialogButtonBox(self.formLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.formLayout.setWidget(15, QtGui.QFormLayout.FieldRole, self.buttonBox)
        self.label_6 = QtGui.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_6)
        self.zip = QtGui.QLineEdit(self.formLayoutWidget)
        self.zip.setObjectName(_fromUtf8("zip"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.zip)
        self.label_8 = QtGui.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_8)
        self.address = QtGui.QLineEdit(self.formLayoutWidget)
        self.address.setObjectName(_fromUtf8("address"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.address)
        self.city = QtGui.QLineEdit(self.formLayoutWidget)
        self.city.setObjectName(_fromUtf8("city"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.city)
        self.checkBox = QtGui.QCheckBox(self.formLayoutWidget)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.formLayout.setWidget(11, QtGui.QFormLayout.FieldRole, self.checkBox)

        self.retranslateUi(uiAddContactForm)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), uiAddContactForm.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), uiAddContactForm.reject)
        QtCore.QMetaObject.connectSlotsByName(uiAddContactForm)

    def retranslateUi(self, uiAddContactForm):
        uiAddContactForm.setWindowTitle(_translate("uiAddContactForm", "Contact", None))
        self.label_5.setText(_translate("uiAddContactForm", "Code postal :", None))
        self.label.setText(_translate("uiAddContactForm", "Nom :", None))
        self.label_3.setText(_translate("uiAddContactForm", "Email : ", None))
        self.label_2.setText(_translate("uiAddContactForm", "Prénom : ", None))
        self.comboBox.setItemText(0, _translate("uiAddContactForm", "Amis", None))
        self.comboBox.setItemText(1, _translate("uiAddContactForm", "Famille", None))
        self.comboBox.setItemText(2, _translate("uiAddContactForm", "Collègues", None))
        self.comboBox.setItemText(3, _translate("uiAddContactForm", "Connaissances", None))
        self.comboBox.setItemText(4, _translate("uiAddContactForm", "Autres", None))
        self.label_4.setText(_translate("uiAddContactForm", "Telephone :", None))
        self.label_7.setText(_translate("uiAddContactForm", "Goupe :", None))
        self.label_6.setText(_translate("uiAddContactForm", "Ville :", None))
        self.label_8.setText(_translate("uiAddContactForm", "Adresse : ", None))
        self.checkBox.setText(_translate("uiAddContactForm", "update", None))
        self.checkBox.setVisible (False)


from ui_main import *
from ui_addcontactform import *
from PyQt4 import QtCore, QtGui

class Annuaire_view():
    #Constructeur de la classe
    def __init__(self, app, controller) :
    	self.ui = Ui_Annuaire_view() #raccourci nom de la classe dans ui_main.py 
    	self.controller = controller #on lui donne son controleur
    	self.ui.setupUi(app) #init l'appi 
        self.ui.dialogForm = QtGui.QDialog() #creation de la fenetre
     

        self.slotConnectUi() 

    #recollecte tous les signaux
    def slotConnectUi(self) :
       self.ui.actionNouveau.triggered.connect(self.showAddContactForm)
       self.ui.dialogForm.accepted.connect(self.addContact)
       self.ui.actionModifier.triggered.connect(self.modifyContact)
       self.ui.actionExtraire_CSV.triggered.connect(self.extractCSV)
       self.ui.pushButton_2.clicked.connect(self.deleteContact)
       self.ui.pushButton.clicked.connect(self.recherche)

    def extractCSV(self) : 
    	self.controller.extractCSV()

   
    def displayMessageExportCSV(self, signum=None, frame=None, bool=False):
    	self.ui.message.setVisible(bool)

    def deleteContact(self) :
    	contactToDelete = self.ui.treeWidget.currentItem() 
    	self.controller.deleteContact( contactToDelete )
    	self.ui.treeWidget.takeTopLevelItem( self.ui.treeWidget.indexOfTopLevelItem( contactToDelete ) )

    def addContact(self) :
    	lastname = self.ui.dialogForm.ui.name.text()
    	firstname = self.ui.dialogForm.ui.firstname.text()
    	mail = self.ui.dialogForm.ui.mail.text()
    	phone = self.ui.dialogForm.ui.phone.text()
    	city = self.ui.dialogForm.ui.city.text()
    	address = self.ui.dialogForm.ui.address.text()
    	zip = self.ui.dialogForm.ui.zip.text()
    	group = self.ui.dialogForm.ui.comboBox.currentText()

    	if self.ui.dialogForm.ui.checkBox.isChecked():
    		self.deleteContact()

    	self.controller.addContact(lastname, firstname, mail, phone, address, city, zip, group)

    def modifyContact(self) :
    	contact = self.ui.treeWidget.currentItem() #reprend l'element courant
    	#affiche le widget de nouveau contact

        u = Ui_uiAddContactForm()
        u.setupUi(self.ui.dialogForm)
        self.ui.dialogForm.ui = u
    	self.ui.dialogForm.ui.name.setText(contact.text(0)) #affiche le contact avec les coordonees courantes
    	self.ui.dialogForm.ui.firstname.setText(contact.text(1))
    	self.ui.dialogForm.ui.mail.setText(contact.text(2))
    	self.ui.dialogForm.ui.phone.setText(contact.text(3))
    	self.ui.dialogForm.ui.city.setText(contact.text(4))
    	self.ui.dialogForm.ui.address.setText(contact.text(5))
    	self.ui.dialogForm.ui.zip.setText(contact.text(6))

    	self.ui.dialogForm.ui.checkBox.setCheckState(QtCore.Qt.Checked)
        self.ui.dialogForm.exec_()

    def updateView(self, contact) :
    	print "LOG -- VIEW -- updateView"
    	#creation du Qtreewidget, setup, et affichage 
    	qtwi = QtGui.QTreeWidgetItem()
    	qtwi.setText(0, contact.getNom() )
    	qtwi.setText(1, contact.getPrenom() )
    	qtwi.setText(2, contact.getEmail() )
    	qtwi.setText(3, contact.getTel() )
       	qtwi.setText(4, contact.getAdresse() )
       	qtwi.setText(5, contact.getVille() )
       	qtwi.setText(6, contact.getCodePostal() )
       	qtwi.setText(7, contact.getGroupe() )

    	self.ui.treeWidget.addTopLevelItem(qtwi)


    def showAddContactForm(self) :
        u = Ui_uiAddContactForm()
        u.setupUi(self.ui.dialogForm)
        self.ui.dialogForm.ui = u
        self.ui.dialogForm.exec_()

    def recherche(self):
    	text = self.ui.lineEdit.text()
    	self.controller.recherche(text) 

    def affichageRecherche(self, listeContact):
    	self.ui.treeWidget.clear()
    	for contact in listeContact:
    		self.updateView(contact)
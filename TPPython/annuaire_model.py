# -*- coding: utf-8 -*-


from contact import * 
import sys
import csv  
from ui_main import *
from PyQt4 import QtGui

class Annuaire_model:

    def __init__(self):
    	self.listOfContacts = []
        pass

    def createContact(self, lastname, firstname, mail, phone, address, city, zip, group):
        return Contact(lastname, firstname, mail, phone, address, city ,zip, group)

    def addToListOfContacts(self, contact) :
    	self.listOfContacts.append(contact)

    def updateContact(self, contactID, field, newValue) :
    	setNewValue = getattr(contact, "set"+field)
    	indexToUpdate = self.listOfContacts.index ( self.findContactByID(contactID) )
    	self.listOfContacts[ indexToUpdate ].setNewValue( newValue )

    def deleteContact(self, contactID) :
    	self.listOfContacts.remove( self.findContactByID(contactID) )

    def readContact(self, contactID) :
   		if contactID == None:
   			return self.listOfContacts
   		else:
   			return self.findContactByID(contactID)

    def findContactByID(self, contactID) :
    	return next(contact for contact in self.listOfContacts if self.createContactID(contact) == contactID )

    def createContactID(self, contact) :
    	return contact.getNom() + "_" + contact.getPrenom()

	def size(self) :
   		return len(self.listOfContacts)

    def exportCSV(self) :
    	fileName = "ExportContacts.csv"
        with open(fileName, 'wb') as csvfile:
            csvExport = csv.writer(csvfile, delimiter=';', 
            					   quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for contact in self.listOfContacts :
            	csvExport.writerow([contact.getNom()] + [contact.getPrenom()] +  [contact.getEmail()]  + [contact.getTel()] + [contact.getAdresse()] +[contact.getVille()] + [ contact.getCodePostal()] + [contact.getGroupe()])
    
    def recherche(self, text):
    	list_of_contactes = list()
    	for contact in self.listOfContacts:
    		print text
    		if contact.getNom() == text:    			
    			list_of_contactes.append(contact)
    			
    	return list_of_contactes		
            	
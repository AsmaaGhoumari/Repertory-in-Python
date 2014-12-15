#!/usr/bin/python2.7.6
# -*- coding: utf-8 -*-

from annuaire_view import *
from annuaire_model import *
 
import contact
import sys
import signal

class Annuaire_controller:
    #Constructeur de la classe
    def __init__(self, app):
        self.ui = Annuaire_view(app, self)
        self.model = Annuaire_model()
        pass

    #affichage du message de l export reussi    
    def extractCSV(self) : 
        signal.signal(signal.SIGALRM, self.ui.displayMessageExportCSV)
        signal.setitimer(signal.ITIMER_REAL, 5)
        self.model.exportCSV()
        self.ui.displayMessageExportCSV(bool=True)

    #TODO 
    def addContact(self, lastname, firstname, mail, phone, address, city, zip, group):
        print "LOG -- CONTROL -- addContact"
        if lastname == "": 
            print "il faut un nom ! " 
        else : 
            newContact = self.model.createContact(lastname, firstname, mail, phone, address, city, zip, group)
            self.model.addToListOfContacts(newContact)
            self.ui.updateView(newContact)

    #recupère les infos, creation d un contact, qu'on va supprimer dans la liste
    def deleteContact(self, treeWidgetItem):
        lastname = treeWidgetItem.text(0)
        firstname = treeWidgetItem.text(1)
        mail = treeWidgetItem.text(2)
        phone = treeWidgetItem.text(3)
        address = treeWidgetItem.text(4)
        city = treeWidgetItem.text(5)
        zip = treeWidgetItem.text(6)
        group = treeWidgetItem.text(7)
        newContact = self.model.createContact(lastname, firstname, mail, phone, address, city, zip, group)
        self.model.deleteContact( self.model.createContactID( newContact ) )

    def recherche(self, text):
        Liste = self.model.recherche(text)
        self.ui.affichageRecherche(Liste)
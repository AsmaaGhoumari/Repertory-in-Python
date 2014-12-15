#!/usr/bin/python2.7.6
# -*- coding: utf-8 -*-

#Definition de la classe contenant les informations d'une personne
class Contact:

      def __init__(self, nom, prenom, email, tel, adresse, ville, codePostal, groupe) :
          self.nom      = nom
          self.prenom   = prenom
          self.tel      = tel
          self.adresse  = adresse
          self.ville    = ville
          self.codePostal = codePostal
          self.email    = email
          self.groupe   = groupe

      def getGroupe(self) :
          return self.groupe

      def setGroupe(self, groupe) :
          self.groupe = groupe

      def getNom(self) :
          return self.nom

      def setNom(self, nom) :
          self.nom = nom

      def getPrenom(self) :
          return self.prenom

      def setPrenom(self, prenom) :
          self.prenom=prenom

      def getTel(self) :
          return self.tel

      def setTel(self, tel) :
          self.tel = tel

      def getVille(self) :
          return self.ville

      def setVille(self, ville) :
          self.ville = ville

      def getCodePostal(self) :
          return self.codePostal

      def setCodePostal(self, codePostal) :
          self.codePostal = codePostal

      def getAdresse(self) :
          return self.adresse

      def setAdresse(self, adresse) :
          self.adresse = adresse

      def getEmail(self) :
          return self.email

      def setEmail(self, email) :
          self.email = email
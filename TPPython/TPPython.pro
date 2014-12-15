#-------------------------------------------------
#
# Project created by QtCreator 2014-09-28T13:08:40
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = TPPython
TEMPLATE = app


SOURCES += main.cpp\
        annuaire_view.cpp \
    

HEADERS  += annuaire_view.h \
    uiaddcontactform.h \
   

FORMS    += annuaire_view.ui \
    uiaddcontactform.ui

OTHER_FILES += \
    annuaire_controller.py \
    annuaire_model.py \
    annuaire_view.py \
    contact.py \
    main.py

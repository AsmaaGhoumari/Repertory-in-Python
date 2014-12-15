#include "uiaddcontactform.h"
#include "ui_uiaddcontactform.h"

uiAddContactForm::uiAddContactForm(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::uiAddContactForm)
{
    ui->setupUi(this);
}

uiAddContactForm::~uiAddContactForm()
{
    delete ui;
}

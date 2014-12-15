#include "annuaire_view.h"
#include "ui_annuaire_view.h"

Annuaire_view::Annuaire_view(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::Annuaire_view)
{
    ui->setupUi(this);
}

Annuaire_view::~Annuaire_view()
{
    delete ui;
}

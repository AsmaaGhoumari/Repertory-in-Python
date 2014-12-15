#ifndef ANNUAIRE_VIEW_H
#define ANNUAIRE_VIEW_H

#include <QMainWindow>

namespace Ui {
class Annuaire_view;
}

class Annuaire_view : public QMainWindow
{
    Q_OBJECT

public:
    explicit Annuaire_view(QWidget *parent = 0);
    ~Annuaire_view();

private:
    Ui::Annuaire_view *ui;
};

#endif // ANNUAIRE_VIEW_H

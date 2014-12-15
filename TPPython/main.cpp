#include "annuaire_view.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    Annuaire_view w;
    w.show();

    return a.exec();
}

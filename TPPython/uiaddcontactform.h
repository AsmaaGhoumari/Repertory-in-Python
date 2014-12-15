#ifndef UIADDCONTACTFORM_H
#define UIADDCONTACTFORM_H

#include <QDialog>

namespace Ui {
class uiAddContactForm;
}

class uiAddContactForm : public QDialog
{
    Q_OBJECT

public:
    explicit uiAddContactForm(QWidget *parent = 0);
    ~uiAddContactForm();

private:
    Ui::uiAddContactForm *ui;
};

#endif // UIADDCONTACTFORM_H

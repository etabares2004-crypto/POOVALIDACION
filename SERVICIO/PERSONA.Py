from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QMainWindow, QMessageBox

from DATOS.persona_DAO import PersonaDAO
from DOMINIO.persona import Persona
from UI.vtnPrincipal import Ui_vtnPrincipal


class PersonaServicio(QMainWindow):
    '''
    clase que genera la logica de los objetos
    '''
    def __init__(self):
        super(PersonaServicio, self).__init__()
        self.ui=Ui_vtnPrincipal()
        self.ui.setupUi(self)
        self.ui.btnGuardar.clicked.connect(self.guardar)
        self.ui.btnLimpiar.clicked.connect(self.limpiar)
        self.ui.txtCedula.setValidator(QIntValidator())
        'Para validar solo 10 dígitos'


    def guardar(self):
        nombre = self.ui.txtNombre.text()
        apellido = self.ui.txtApellido.text()
        cedula = self.ui.txtCedula.text()
        sexo = self.ui.cbsexo.currentText()
        # Validación de los datos del formulario
        if nombre == "":
            QMessageBox.warning(self, 'Advertencia', 'Debe ingresar el nombre')
        elif apellido == "":
            QMessageBox.warning(self, 'Advertencia', 'Debe ingresar el apellido')
        elif len(cedula)< 10:
            QMessageBox.warning(self, 'Advertencia', 'Debe ingresar la cedula')
        elif sexo == "Seleccionar":
            QMessageBox.warning(self, 'Advertencia', 'Debe seleccionar el sexo')
        else:
            persona = Persona(cedula=cedula, nombre=nombre, apellido=apellido, sexo=sexo)
            PersonaDAO.insertar_persona(persona)
            print(persona)
            #print(nombre)
            #print(apellido)
            #print(cedula)
            #print(sexo)
            # Mostrar confirmación de que guardo
            self.ui.statusbar.showMessage('Se guardó la información', 3000)
            # borrar campos del formulario
            self.ui.txtNombre.setText('')
            self.ui.txtApellido.setText('')
            self.ui.txtCedula.setText('')

    def limpiar(self):
        self.ui.txtNombre.setText('')
        self.ui.txtApellido.setText('')
        self.ui.txtCedula.setText('')
        self.ui.cbSexo.setCurrentText('Seleccionar')

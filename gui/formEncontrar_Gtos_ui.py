# Form implementation generated from reading ui file 'c:\Users\smart\OneDrive\Escritorio\gac_py_V1.02\gui\formEncontrar_Gtos.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_formClientes(object):
    def setupUi(self, formClientes):
        formClientes.setObjectName("formClientes")
        formClientes.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        formClientes.resize(677, 636)
        formClientes.setWindowTitle("")
        formClientes.setStyleSheet("background-color: rgb(245, 245, 252);")
        self.frame = QtWidgets.QFrame(parent=formClientes)
        self.frame.setGeometry(QtCore.QRect(0, 0, 681, 71))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setStyleSheet("background-color: rgb(8, 14, 91);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label_6 = QtWidgets.QLabel(parent=self.frame)
        self.label_6.setGeometry(QtCore.QRect(0, 40, 832, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(19, 39, 113);\n"
"color: rgb(255, 78, 2);\n"
"color: rgb(216, 224, 236);")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.frame_2 = QtWidgets.QFrame(parent=formClientes)
        self.frame_2.setGeometry(QtCore.QRect(0, 70, 681, 211))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 500))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(245, 245, 252);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.groupBox = QtWidgets.QGroupBox(parent=self.frame_2)
        self.groupBox.setGeometry(QtCore.QRect(20, 19, 641, 181))
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(200, 20, 431, 141))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lblProv = QtWidgets.QLabel(parent=self.groupBox_2)
        self.lblProv.setGeometry(QtCore.QRect(60, 40, 111, 16))
        self.lblProv.setObjectName("lblProv")
        self.radioButton_prov = QtWidgets.QRadioButton(parent=self.groupBox)
        self.radioButton_prov.setGeometry(QtCore.QRect(30, 40, 89, 20))
        self.radioButton_prov.setObjectName("radioButton_prov")
        self.radioButton_tgasto = QtWidgets.QRadioButton(parent=self.groupBox)
        self.radioButton_tgasto.setGeometry(QtCore.QRect(30, 100, 111, 20))
        self.radioButton_tgasto.setObjectName("radioButton_tgasto")
        self.radioButton_fechas = QtWidgets.QRadioButton(parent=self.groupBox)
        self.radioButton_fechas.setGeometry(QtCore.QRect(30, 130, 89, 20))
        self.radioButton_fechas.setObjectName("radioButton_fechas")
        self.radioButton_emp = QtWidgets.QRadioButton(parent=self.groupBox)
        self.radioButton_emp.setGeometry(QtCore.QRect(30, 70, 89, 20))
        self.radioButton_emp.setObjectName("radioButton_emp")
        self.frame_3 = QtWidgets.QFrame(parent=formClientes)
        self.frame_3.setGeometry(QtCore.QRect(0, 270, 681, 51))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.btnSalir = QtWidgets.QPushButton(parent=self.frame_3)
        self.btnSalir.setGeometry(QtCore.QRect(400, 10, 261, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        self.btnSalir.setFont(font)
        self.btnSalir.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnSalir.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.btnSalir.setStyleSheet("background-color: rgb(8, 19, 95);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\smart\\OneDrive\\Escritorio\\gac_py_V1.02\\gui\\../iconos/salir.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnSalir.setIcon(icon)
        self.btnSalir.setIconSize(QtCore.QSize(20, 20))
        self.btnSalir.setFlat(True)
        self.btnSalir.setObjectName("btnSalir")
        self.btnConsultar = QtWidgets.QPushButton(parent=self.frame_3)
        self.btnConsultar.setGeometry(QtCore.QRect(20, 10, 271, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        self.btnConsultar.setFont(font)
        self.btnConsultar.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnConsultar.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.btnConsultar.setStyleSheet("background-color: rgb(8, 19, 95);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\smart\\OneDrive\\Escritorio\\gac_py_V1.02\\gui\\../iconos/buscarDb.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnConsultar.setIcon(icon1)
        self.btnConsultar.setIconSize(QtCore.QSize(30, 30))
        self.btnConsultar.setFlat(True)
        self.btnConsultar.setObjectName("btnConsultar")
        self.dateEdit_fecha_ini = QtWidgets.QDateEdit(parent=formClientes)
        self.dateEdit_fecha_ini.setGeometry(QtCore.QRect(160, 380, 110, 30))
        self.dateEdit_fecha_ini.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"color: rgb(0, 0, 0);")
        self.dateEdit_fecha_ini.setCalendarPopup(True)
        self.dateEdit_fecha_ini.setObjectName("dateEdit_fecha_ini")
        self.dateEdit_fecha_fin = QtWidgets.QDateEdit(parent=formClientes)
        self.dateEdit_fecha_fin.setGeometry(QtCore.QRect(330, 380, 110, 30))
        self.dateEdit_fecha_fin.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"color: rgb(0, 0, 0);")
        self.dateEdit_fecha_fin.setCalendarPopup(True)
        self.dateEdit_fecha_fin.setObjectName("dateEdit_fecha_fin")
        self.lblFecha_inicial = QtWidgets.QLabel(parent=formClientes)
        self.lblFecha_inicial.setGeometry(QtCore.QRect(160, 360, 71, 16))
        self.lblFecha_inicial.setObjectName("lblFecha_inicial")
        self.lclFecha_final = QtWidgets.QLabel(parent=formClientes)
        self.lclFecha_final.setGeometry(QtCore.QRect(330, 360, 71, 16))
        self.lclFecha_final.setObjectName("lclFecha_final")
        self.lblTipo_ingreso = QtWidgets.QLabel(parent=formClientes)
        self.lblTipo_ingreso.setGeometry(QtCore.QRect(210, 430, 81, 16))
        self.lblTipo_ingreso.setObjectName("lblTipo_ingreso")
        self.cmb_tipo_ing = QtWidgets.QComboBox(parent=formClientes)
        self.cmb_tipo_ing.setGeometry(QtCore.QRect(140, 460, 231, 30))
        self.cmb_tipo_ing.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.cmb_tipo_ing.setObjectName("cmb_tipo_ing")
        self.cmb_tipo_ing.addItem("")
        self.cmb_tipo_ing.addItem("")
        self.cmb_tipo_ing.addItem("")
        self.cmb_tipo_ing.addItem("")
        self.cmb_tipo_ing.addItem("")
        self.cmb_tipo_ing.addItem("")
        self.cmb_tipo_cartera = QtWidgets.QComboBox(parent=formClientes)
        self.cmb_tipo_cartera.setGeometry(QtCore.QRect(380, 450, 191, 30))
        self.cmb_tipo_cartera.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.cmb_tipo_cartera.setObjectName("cmb_tipo_cartera")
        self.cmb_tipo_cartera.addItem("")
        self.cmb_tipo_cartera.addItem("")
        self.cmb_tipo_cartera.addItem("")
        self.lblTipo_cartera = QtWidgets.QLabel(parent=formClientes)
        self.lblTipo_cartera.setGeometry(QtCore.QRect(380, 430, 71, 16))
        self.lblTipo_cartera.setObjectName("lblTipo_cartera")
        self.cmb_prov = QtWidgets.QComboBox(parent=formClientes)
        self.cmb_prov.setGeometry(QtCore.QRect(280, 170, 311, 30))
        self.cmb_prov.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.cmb_prov.setObjectName("cmb_prov")
        self.cmb_prov.addItem("")

        self.retranslateUi(formClientes)
        QtCore.QMetaObject.connectSlotsByName(formClientes)

    def retranslateUi(self, formClientes):
        _translate = QtCore.QCoreApplication.translate
        self.label_6.setText(_translate("formClientes", "  BUSCAR INFORMACION"))
        self.groupBox.setTitle(_translate("formClientes", "Opciones Busqueda"))
        self.groupBox_2.setTitle(_translate("formClientes", "Proveedor"))
        self.lblProv.setText(_translate("formClientes", "Prestador Servicios"))
        self.radioButton_prov.setText(_translate("formClientes", "Proveedor"))
        self.radioButton_tgasto.setText(_translate("formClientes", "Tipo Gasto"))
        self.radioButton_fechas.setText(_translate("formClientes", "Fechas"))
        self.radioButton_emp.setText(_translate("formClientes", "Empleado"))
        self.btnSalir.setText(_translate("formClientes", "Salir"))
        self.btnConsultar.setText(_translate("formClientes", "Consultar"))
        self.lblFecha_inicial.setText(_translate("formClientes", "Fecha Inicial"))
        self.lclFecha_final.setText(_translate("formClientes", "Fecha Final"))
        self.lblTipo_ingreso.setText(_translate("formClientes", "Tipo Ingreso"))
        self.cmb_tipo_ing.setItemText(0, _translate("formClientes", "---selecciona una opcion---"))
        self.cmb_tipo_ing.setItemText(1, _translate("formClientes", "pago mensual"))
        self.cmb_tipo_ing.setItemText(2, _translate("formClientes", "pago atrasado"))
        self.cmb_tipo_ing.setItemText(3, _translate("formClientes", "pago anticipado"))
        self.cmb_tipo_ing.setItemText(4, _translate("formClientes", "pago no identificado"))
        self.cmb_tipo_ing.setItemText(5, _translate("formClientes", "pago parcial o a cuenta"))
        self.cmb_tipo_cartera.setItemText(0, _translate("formClientes", "-selecciona una opcion-"))
        self.cmb_tipo_cartera.setItemText(1, _translate("formClientes", "locales comerciales"))
        self.cmb_tipo_cartera.setItemText(2, _translate("formClientes", "areas comunes"))
        self.lblTipo_cartera.setText(_translate("formClientes", "Tipo Cartera"))
        self.cmb_prov.setItemText(0, _translate("formClientes", "---selecciona una opcion---"))

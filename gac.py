from datetime import datetime
import csv
import sys
import os
from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem, QFileDialog, QLineEdit, QApplication
from data import ctasbancos
from data.cartera import CarteraDataAC, CarteraDataCM, CarteraDataGral
from data.clientes import BuscarCliente, ClientesData
from data.contratos import ContratosData
from data.editcontrato import EditContratoData
#from data.editcuotas import CuotasDataGral
from data.facturas import FacturasData
from data.periodo import PeriodosCargaData
from data.regareac import RegACData
from data.regcliente import RegClienteData
from data.regcontrato import RegContratoData
from data.proveedores import ProveedoresData
from data.regctabancos import RegCtasBancoData
from data.regempleado import  RegEmpleadoData
from data.regfacturas import RegFacturaData
from data.reggastos import GastosDataGral, RegGastoData
from data.reglocal import RegLocalData
from data.regpagos import   RegCarteraData, RegCobranzaData
from data.ubicaciones import  AreasData, ListaAreasData, ListaCuotasData, UbicacionesData
from data.usuario import UsuarioData
from model.ctasbancos import Cuentas
from model.editcontrato import EditContrato
from model.operaciones import Reg_Cartera, Reg_Cobranza, Reg_Factura, Reg_Gasto
from model.regProveedor import RegProveedor
from model.regareac import RegAC
from model.regcliente import RegCliente
from model.regcontrato import RegContrato
from model.regempleado import RegEmpleado
from model.reglocal import RegLocal
from model.regperiodofacturacion import RegPeriodoFacturacion
from model.user import Usuario 
import xlsxwriter
from PyQt6.QtGui import QIcon

current_datetime = datetime.today()

###############################################PANTALLA PRINCIPAL####################################################################################
class PantallaPrincipal():
    @staticmethod
    def resource_path(relative_path):
    # Get absolute path to resource, works for dev and for PyInstaller
        try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
            
        return os.path.join(base_path, relative_path)
    
    
    def __init__(self):
        #icon_pp= QIcon("C:/Users/smart/OneDrive/Escritorio/gac_py_V1.02/iconos/cartera.ico")
        #self.pp = uic.loadUi(self.resource_path("C:/Users/smart/OneDrive/Escritorio/gac_py_V1.02/gui/formMain.ui"))
        self.pp = uic.loadUi(self.resource_path("gui/formMain.ui"))
        self.pp.setWindowIcon(QIcon(self.resource_path("iconos/cartera.ico")))
        self.pp.setWindowTitle("Gestor Administrativo Condominal")
        self.pp.show()
        self.pp.resize(1132,805)
        self.pp.lblImagen.setGeometry(9,9,1200,690)
        self.pp.btnInvisible.setGeometry(130,410,211,20)
        self.pp.btnInvisible.setFlat(True)
        self.pp.btnInvisible.clicked.connect(self.mostrar_recuperar_pass)
        self.pp.pushB_user.setVisible(False)
        self.pp.pushB_pass.setVisible(False)
        self.pp.btnRecuperar.setVisible(False) 
        self.pp.menubar.setVisible(False)
        self.pp.txtNameUser.setVisible(False)
        self.pp.btnEntrar.clicked.connect(self.validar_acceso)
        self.pp.btnNewUser.clicked.connect(self.select_new_user)
        self.pp.btnReg_new_user.setVisible(False)
        self.pp.pushB_user.clicked.connect(self.ayuda_user)
        self.pp.pushB_pass.clicked.connect(self.ayuda_pass)
        self.pp.btnReg_new_user.clicked.connect(self.reg_new_user)
        self.pp.btnIngresar.clicked.connect(self.mostrar_panel)
        self.pp.btnRegresar.clicked.connect(self.ocultar_panel)
        self.pp.actionRegMovCM.triggered.connect(self.abrir_form_PPCM)
        self.pp.actionRegMovAC.triggered.connect(self.abrir_form_PPAC)    
        self.pp.actionRegistrar_cliente.triggered.connect(self.abrir_form_clientes)
        self.pp.btnRecuperar.clicked.connect(self.recuperar_pass)
        self.pp.actionAltaLocal.triggered.connect(self.abrir_form_alta_local)
        self.pp.actionAltaAC.triggered.connect(self.abrir_form_alta_AC)
        self.pp.actionCarga_Clientes.triggered.connect(self.carga_clientes_bd)
        self.pp.actionCarga_Locales.triggered.connect(self.carga_ubicaciones_bd)
        self.pp.actionCarga_Areas_Comunes.triggered.connect(self.carga_areasC_bd)
        self.pp.actionCarga_Contratos.triggered.connect(self.carga_contratos_bd)
        self.pp.actionCarga_Saldos_Iniciales.triggered.connect(self.carga_saldos_iniciales_cartera)
        self.pp.actionCarga_Empleados.triggered.connect(self.carga_empleados_bd)
        self.pp.toolButton.clicked.connect(self.mostrar_password)
        self.pp.actionRegCuentas.triggered.connect(self.abrir_form_banco)
        self.pp.actionRegContrato.triggered.connect(self.abrir_form_contratos)
        self.pp.actionBuscar_Contratos.triggered.connect(self.abrir_form_buscar_contratos)
        self.pp.actionFacturacion_Masiva.triggered.connect(self.abrir_form_cmasiva)
        self.pp.actionRegistrar_Gastos.triggered.connect(self.abrir_form_gastos)
        self.pp.actionAlta_Prest_Serv.triggered.connect(self.abrir_form_alta_proveedor)
        self.pp.actionAlta_Empleado.triggered.connect(self.abrir_form_alta_empleado)
        self.pp.actionReporte_Ingresos.triggered.connect(self.abrir_form_reporte_ingresos)
        self.pp.actionReporte_Gastos.triggered.connect(self.abrir_form_rep_gastos)
        self.pp.actionIncrementar.triggered.connect(self.form_incre_cuotas)
        self.pp.actionRegistro_O_Ingresos.triggered.connect(self.form_reg_Ogtos)
        self.pp.btnSalirPP.clicked.connect(self.salir_pp) 
    
    
    
            
    def carga_clientes_bd(self):
        m=QMessageBox()
        m.setIcon(QMessageBox.Icon.Information)
        m.setWindowTitle("Carga BD Clientes")
        m.setStandardButtons(QMessageBox.StandardButton.Ok)
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self.pp, "Seleccionar archivo", "", "Archivos CSV (*.csv);;Todos los archivos (*)")
        
        if file_path:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Skip the header row
                data = [row for row in reader]
                try:
                    for row in data:
                        if len(row) != 14:
                            m.setText("El archivo CSV no tiene el formato correcto")
                            m.exec()
                            return
                        carga_clientes = RegCliente(
                            nombre=row[1],
                            rfc=row[2],
                            tContribuyente=row[3],
                            curp=row[4],
                            num_area_o_local=row[5],
                            tCliente=row[6],
                            giro=row[7],
                            direccion=row[8],
                            numcel=row[9],
                            email=row[10],
                            fechareg=current_datetime.strftime("%Y-%m-%d %H:%M:%S"),
                            status_cliente=row[12],
                            usuario=row[13]
                        )
                        objData = RegClienteData()
                        if objData.registrar(carga_clientes):
                            m.setText("info clientes cargada con exito")
                        else:
                            m.setText("clientes no registrados")
                except Exception as e:
                    m.setText(f"Error en la carga de clientes: \n{e}")        
        m.exec()               
                        
    def carga_ubicaciones_bd(self):
        m=QMessageBox()
        m.setIcon(QMessageBox.Icon.Information)
        m.setWindowTitle("Carga BD Locales")
        m.setStandardButtons(QMessageBox.StandardButton.Ok)
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self.pp, "Seleccionar archivo", "", "Archivos CSV (*.csv);;Todos los archivos (*)")
        
        if file_path:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Skip the header row
                data = [row for row in reader]
                try:
                    for row in data:
                        if len(row) != 12:
                            m.setText("El archivo CSV no tiene el formato correcto")
                            m.exec()
                            return
                        carga_locales = RegLocal(
                            num_local=row[1],
                            superficie=row[2],
                            cuota=row[3],
                            dg=row[4],
                            nom_propietario=row[5],
                            rfc_propietario=row[6],
                            cliente=row[7],
                            giro=row[8],
                            status=False,
                            usuario=self.pp.lblName_User.text(),
                            fechareg=current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                            )
                        objData = RegLocalData()
                        if objData.registrar(carga_locales):
                            m.setText("Ubicaciones cargadas con exito")
                        else:
                            m.setText("base datos cargada")
                except Exception as e:
                    m.setText(f"Error en la carga de ubicaciones: {e}")        
        m.exec()                           
                
    def carga_areasC_bd(self):
        m=QMessageBox()
        m.setIcon(QMessageBox.Icon.Information)
        m.setWindowTitle("Carga BD Areas Comunes")
        m.setStandardButtons(QMessageBox.StandardButton.Ok)
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self.pp, "Seleccionar archivo", "", "Archivos CSV (*.csv);;Todos los archivos (*)")
        
        if file_path:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Skip the header row
                data = [row for row in reader]
                try:
                    for row in data:
                        if len(row) != 13:
                                m.setText("El archivo CSV no tiene el formato correcto")
                                m.exec()
                                return
                        carga_areas = RegAC(
                            num_area=row[1],
                            cliente_fact=row[2],
                            cuota=row[3],
                            dg=row[4],
                            tipo_area=row[5],
                            cantidad=row[6],
                            sup=row[7],
                            giro=row[8],
                            contrato=row[9],
                            status=False,
                            fReg=current_datetime.strftime("%Y-%m-%d %H:%M:%S"),
                            usuario=self.pp.lblName_User.text()
                            )
                        objData = RegACData()
                        if objData.registrar(carga_areas):
                            m.setText("Areas Comunes cargadas con exito")
                        else:
                            m.setText("base de datos cargada")
                except Exception as e:
                    m.setText(f"Error en la carga de areas comunes: {e}")
        m.exec()             
    
    def carga_contratos_bd(self):
        m=QMessageBox()
        m.setIcon(QMessageBox.Icon.Information)
        m.setWindowTitle("Carga BD Contratos")
        m.setStandardButtons(QMessageBox.StandardButton.Ok)
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self.pp, "Seleccionar archivo", "", "Archivos CSV (*.csv);;Todos los archivos (*)")
        
        if file_path:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Skip the header row
                data = [row for row in reader]
                try:
                    for row in data:
                        if len(row) != 13:
                                m.setText("El archivo CSV no tiene el formato correcto")
                                m.exec()
                                return
                        carga_contratos = RegContrato(
                            n_contrato=row[1],
                            c_facturacion=row[2],
                            n_area=row[3],
                            f_inicio=row[4],
                            f_fin=row[5],
                            m_cuota=row[6],
                            m_dg=row[7],
                            t_contrato=row[8],
                            s_contrato=row[9],
                            s_vigencia=row[10],
                            r_usuario=self.pp.lblName_User.text(),
                            f_registro=current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                            )
                        objData = RegContratoData()
                        if objData.registrar(carga_contratos):
                            m.setText("Contratos cargados con exito")
                        else:
                            m.setText("base de datos cargada")
                except Exception as e:
                    m.setText(f"Error en la carga de contratos : {e}")
        m.exec()             
        
    def carga_saldos_iniciales_cartera(self):
        m=QMessageBox()
        m.setIcon(QMessageBox.Icon.Information)
        m.setWindowTitle("Carga BD Saldos Iniciales")
        m.setStandardButtons(QMessageBox.StandardButton.Ok)
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self.pp, "Seleccionar archivo", "", "Archivos CSV (*.csv);;Todos los archivos (*)")
        
        if file_path:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Skip the header row
                data = [row for row in reader]
                try:
                    for row in data:
                        if len(row) != 18:
                                m.setText("El archivo CSV no tiene el formato correcto")
                                m.exec()
                                return
                        carga_carteraini = Reg_Cartera(
                            local_o_area=row[1],
                            clienteFact=row[2],
                            tipoCartera=row[3],
                            tipoCuota=row[4],
                            tipo_factura=row[5],
                            numFact=row[6],
                            importeAdeudo=row[7],
                            importePago=row[8],
                            fPago_Cobro=row[9],
                            ctaBanco=row[10],
                            formaPago=row[11],
                            cheque=row[12],
                            numContrato=row[13],
                            statusPago=False,
                            usuario=self.pp.lblName_User.text(),
                            fechaReg=current_datetime.strftime("%Y-%m-%d %H:%M:%S"),
                            comentarios=row[17]
                            )
                        objData = RegCarteraData()
                        if objData._registrar(carga_carteraini):
                            m.setText("Saldos Iniciales cargados con exito")
                        else:
                            m.setText("base de datos cargada")
                except Exception as e:
                    m.setText(f"Error en la carga de saldos iniciales: {e}")
        m.exec()                                      

    def carga_empleados_bd(self):
        m=QMessageBox()
        m.setIcon(QMessageBox.Icon.Information)
        m.setWindowTitle("Carga BD Empleados")
        m.setStandardButtons(QMessageBox.StandardButton.Ok)
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self.pp, "Seleccionar archivo", "", "Archivos CSV (*.csv);;Todos los archivos (*)")
        
        if file_path:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Skip the header row
                data = [row for row in reader]
                try:
                    for row in data:
                        if len(row) != 19:
                            m.setText("El archivo CSV no tiene el formato correcto")
                            m.exec()
                            return
                        carga_empleados=RegEmpleado(
                            nombres=row[1].upper(),
                            apellido_pat=row[2].upper(),
                            apellido_mat=row[3].upper(),
                            rfc=row[4].upper(),
                            curp=row[5].upper(),
                            numnss=row[6],
                            f_nacimiento=row[7],
                            puesto=row[8],
                            departamento=row[9],
                            sueldo=row[10],
                            direccion=row[11].upper(),
                            telefono=row[12],
                            email=row[13],
                            f_ingreso=row[14],
                            f_baja=row[15],
                            status=row[16],
                            usuario=row[17],
                            f_reg=row[18]
                            )
                        objData = RegEmpleadoData()
                        if objData.registrar(carga_empleados):
                            m.setText("info empleados cargada con exito")
                        else:
                            m.seText("empleado no registrado")
                except Exception as e:
                    m.setText(f"Error en la carga de empleado: \n{e}")        
        m.exec()                        
                                                    
    def mostrar_panel(self):
        self.pp.lblImagen.setGeometry(9,9,680,690)
        self.pp.btnNewUser.setGeometry(110, 490, 250, 30)
        self.pp.btnIngresar.setVisible(False)
        self.pp.btnNewUser.setText("Nuevo Usuario")
        self.pp.btnInvisible.setVisible(True)
        self.pp.lblRecPassword.setVisible(True) 
        self.pp.btnEntrar.setVisible(True)
        self.pp.btnNewUser.setVisible(True)
        self.pp.txtPassword.setVisible(True)
        self.pp.txtUsuario.setText("administrador")
        self.pp.txtPassword.setText("adMin_81@")
        self.pp.txtNameUser.setText("")
        self.pp.toolButton.setVisible(True)
        self.pp.pushB_user.setVisible(False)
        self.pp.pushB_pass.setVisible(False)
        self.pp.btnReg_new_user.setVisible(False)
        self.pp.txtPassword.setEchoMode(QLineEdit.EchoMode.Password)    
        
    def ocultar_panel(self):
        self.pp.btnIngresar.setVisible(True)
        self.pp.lblImagen.setGeometry(9,9,1200,690) 
        self.pp.txtNameUser.setVisible(False)
        self.pp.btnNewUser.setVisible(False)
        self.pp.btnRecuperar.setVisible(False)
        self.pp.txtUsuario.setText("")
        self.pp.txtPassword.setText("")
                      
    def mostrar_password(self):
        self.pp.txtPassword.setEchoMode(QLineEdit.EchoMode.Normal)    
     
    def ayuda_user(self):
        m=QMessageBox()
        m.setIcon(QMessageBox.Icon.Information)
        m.setWindowTitle("Ayuda Usuario")
        m.setText("El usuario debe tener al menos 5 caracteres")
        m.exec()
    
    def ayuda_pass(self):
        m=QMessageBox()
        m.setIcon(QMessageBox.Icon.Information)
        m.setWindowTitle("Ayuda Password")
        m.setText("La contraseña debe tener al menos 8 caracteres \nLa contraseña debe contener al menos una letra mayuscula \nLa contraseña debe contener al menos un carácter especial: @ # $ % * ") 
        m.exec()
            
    def salir_pp(self):
        self.pp.close()  
 
    
 
 ##############################################LOG IN###################################################       
    def validar_acceso(self):
        self.pp.actionCarga_Clientes.setEnabled(False)
        self.pp.actionCarga_Locales.setEnabled(False)
        self.pp.actionCarga_Areas_Comunes.setEnabled(False)
        self.pp.actionCarga_Contratos.setEnabled(False)
        self.pp.actionCarga_Saldos_Iniciales.setEnabled(False)
        self.pp.actionRegCuentas.setEnabled(False)
        self.pp.actionAltaLocal.setEnabled(False)
        m=QMessageBox()
        m.setIcon(QMessageBox.Icon.Information)
        m.setWindowTitle("Log In")
        
        if  self.pp.txtUsuario.text()=="":
            m.setText("Ingrese un Usuario")    
            self.pp.txtUsuario.setFocus()
            
        elif self.pp.txtPassword.text()=="":
            m.setText("Ingrese una contraseña")
            self.pp.txtPassword.setFocus()        
        else:
            user_info= Usuario(usuario=self.pp.txtUsuario.text(),clave=self.pp.txtPassword.text())
            usuData= UsuarioData()
            res= usuData.login(user_info)
            if res:
                self.pp.menubar.setVisible(True)
                nom_user=self.pp.txtUsuario.text()
                self.pp.lblImagen.setGeometry(9,9,1200,690) 
                m.setText("Hola""  " + nom_user)
                self.pp.btnIngresar.setVisible(True)
                #self.pp.btnReiniciar.setVisible(True)
                self.pp.statusBar.showMessage("Bienvenido" " "+ nom_user,0)
                self.pp.lblName_User.setText(nom_user)
                if nom_user == "administrador":
                    self.pp.actionCarga_Clientes.setEnabled(True)
                    self.pp.actionCarga_Locales.setEnabled(True)
                    self.pp.actionCarga_Areas_Comunes.setEnabled(True)
                    self.pp.actionCarga_Contratos.setEnabled(True)
                    self.pp.actionCarga_Saldos_Iniciales.setEnabled(True)
                    self.pp.actionRegCuentas.setEnabled(True)
                    self.pp.actionAltaLocal.setEnabled(True)
                else:
                    self.pp.actionRegCuentas.setEnabled(True)       
            else:
                m.setText("Usuario o Contraseña no validos")
                m.setIcon(QMessageBox.Icon.Warning)
                self.pp.btnNewUser.setVisible(True)
                self.pp.txtUsuario.setText("")
                self.pp.txtPassword.setText("")
                self.pp.txtUsuario.setFocus()
        m.exec()        
    
    def select_new_user(self):
        self.pp.btnEntrar.setVisible(False)
        self.pp.btnInvisible.setVisible(False)
        #self.pp.btnNewUser.setGeometry(110, 440, 250, 31)
        self.pp.btnReg_new_user.setVisible(True)
        self.pp.txtNameUser.setGeometry(110,250,250,30)
        self.pp.btnNewUser.setVisible(False)
        self.pp.btnReg_new_user.setGeometry(110, 440, 250, 31)
        self.pp.txtNameUser.setVisible(True)
        self.pp.lblRecPassword.setVisible(False)
        self.pp.txtNameUser.setFocus()
        self.pp.txtUsuario.setText("")
        self.pp.txtPassword.setText("")
        self.pp.pushB_user.setVisible(True)
        self.pp.pushB_pass.setVisible(True)    
         
    def reg_new_user(self):
        mensaje = QMessageBox()
        mensaje.setIcon(QMessageBox.Icon.Information)
        mensaje.setWindowTitle("Registrar Usuario")
        # self.pp.btnEntrar.setVisible(False)
        # self.pp.btnInvisible.setVisible(False)
        # self.pp.btnNewUser.setGeometry(110, 440, 250, 31)
        # self.pp.txtNameUser.setGeometry(110,250,250,30)
        # self.pp.btnNewUser.setText("Registrar")
        # self.pp.txtNameUser.setVisible(True)
        # self.pp.lblRecPassword.setVisible(False)
        # self.pp.txtNameUser.setFocus()
        # self.pp.txtUsuario.setText("")
        # self.pp.txtPassword.setText("")
        # self.pp.pushB_user.setVisible(True)
        # self.pp.pushB_pass.setVisible(True)
        
        nombre= self.pp.txtNameUser.text()
        usuario = self.pp.txtUsuario.text()
        password = self.pp.txtPassword.text()
    
        if nombre=="":
            mensaje.setText("Ingrese un Nombre")
            self.pp.txtNameUser.setFocus()  
        elif usuario == "":
            mensaje.setText("Ingrese un Usuario")
            self.pp.txtUsuario.setFocus()
            
        elif len(usuario)<5:
            mensaje.setText("El usuario debe tener al menos 5 caracteres")
            self.pp.txtUsuario.setFocus() 
               
        elif password == "":
            mensaje.setText("Ingrese una Contraseña")
            self.pp.txtPassword.setFocus()
                    
        elif len(password)<8:
            mensaje.setText("La contraseña debe tener al menos 8 caracteres")
            self.pp.txtPassword.setFocus()
            
        elif not any(char in "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z" for char in password):
            mensaje.setText("La contraseña debe contener al menos una letra mayuscula")
            self.pp.txtPassword.setFocus()    
            
        elif not any(char in "@ # $ % & *" for char in password):
            mensaje.setText("La contraseña debe contener al menos un carácter especial: @ # $ % & * ")
            self.pp.txtPassword.setFocus()
        else:
            usuData = UsuarioData()
            nuevo_usuario = Usuario(nombre=nombre,usuario=usuario, clave=password,usuario_reg=self.pp.lblName_User.text())
            res = usuData.registrar(nuevo_usuario)
            
            if res:
                mensaje.setText("Usuario registrado exitosamente")
                self.pp.txtNameUser.setText("")
                self.pp.txtUsuario.setText("")
                self.pp.txtPassword.setText("")
                self.pp.txtNameUser.setVisible(False)
                self.pp.btnEntrar.setVisible(True)
                self.ocultar_panel()
            else:
                self.pp.txtNameUser.setText("")
                self.pp.txtUsuario.setText("")
                self.pp.txtPassword.setText("")
                mensaje.setIcon(QMessageBox.Icon.Warning)
                mensaje.setText("Usuario ya Registrado") 
        mensaje.exec()    
        
    def mostrar_recuperar_pass(self):
        self.pp.btnInvisible.setVisible(False)
        self.pp.lblRecPassword.setVisible(False)
        self.pp.txtPassword.setVisible(False)
        self.pp.btnEntrar.setVisible(False)
        self.pp.btnNewUser.setVisible(False)
        self.pp.btnRecuperar.setVisible(True)
        self.pp.toolButton.setVisible(False)
        self.pp.btnRecuperar.setGeometry(110,440,250,31)
        self.pp.txtUsuario.setText("")
        self.pp.txtPassword.setText("")
        self.pp.txtUsuario.setFocus()
        
    def recuperar_pass(self):
        m = QMessageBox()
        m.setIcon(QMessageBox.Icon.Information)
        m.setWindowTitle("Recuperar Contraseña")
        
        usuario = self.pp.txtUsuario.text()
        
        if usuario == "":
            m.setText("Ingrese un Usuario")
            self.pp.txtUsuario.setFocus()
        else:
            usuData = UsuarioData()
            res = usuData.recuperar(usuario)
            
            if res:
                m.setText(f"Su contraseña es :  {res}")
                self.pp.txtUsuario.setText("")
            else:
                m.setText("Usuario no encontrado")
                m.setIcon(QMessageBox.Icon.Warning)
                self.pp.txtUsuario.setText("")
                
        m.exec()
    
 
 #################################ALTA LOCALES COMERCIALES###############################################   
    def abrir_form_alta_local(self):
        #self.fal=uic.loadUi(self.resource_path("C:/Users/smart/OneDrive/Escritorio/gac_py_V1.02/gui/formLocales.ui"))
        self.fal=uic.loadUi(self.resource_path("gui/formLocales.ui"))
        self.fal.setWindowTitle("Alta Local Comercial")
        self.fal.show()
        self.fal.txtLocal.setText("L-")
        self.fal.checkBoxStatus.setChecked(True)
        self.fal.txtRFC_p.setText("XAXX010101000")
        self.set_cmb_clientes()
        self.fal.btnGuardar.clicked.connect(self.registrar_local)
        self.fal.btnSalir.clicked.connect(self.salir_form_local) 
            
    def registrar_local(self):       
            m=QMessageBox()
            m.setIcon(QMessageBox.Icon.Information)
            m.setWindowTitle("Alta Local Comercial")
            m.setStandardButtons(QMessageBox.StandardButton.Ok)
        
            if self.fal.txtLocal.text()=="":       
                m.setText("Capture numero de Local")
                self.fal.txtLocal.setFocus()
            
            elif len(self.fal.txtLocal.text())<4:
                m.setText("Numero de local incorrecto")
                self.fal.txtLocal.setFocus()
                    
            elif self.fal.txtSuperficie.text()=="":
                m.setText(" Capture superficie m2")
                self.fal.txtSuperficie.setFocus()
            
            elif not self.fal.txtSuperficie.text().replace('.','',1).isnumeric():   
                m.setText("Captura solo numeros")
                self.fal.txtSuperficie.setText('0.00')
                self.fal.txtSuperficie.setFocus()    
                                
            elif self.fal.cmbClientes.currentIndex()==0:
                m.setText("Selecciona una opcion")
                self.fal.cmbClientes.setFocus()
        
            elif self.fal.txtGiro.text()=="":
                m.setText("Capture Giro del Local")
                self.fal.txtGiro.setFocus()
            
            elif  self.fal.txtCuota.text()=="":
                m.setText("Capture Cuota Mensual")        
                self.fal.txtCuota.setFocus()
                 
            elif not self.fal.txtCuota.text().replace('.',"" ,1).isnumeric():   
                m.setText("Captura solo numeros")
                self.fal.txtCuota.setText('0.00')
                self.fal.txtCuota.setFocus()
            
            elif self.fal.txtRFC_p.text()=="":
                m.setText("Capture RFC Propietario")
                self.fal.txtRFC_p.setFocus()
                
            elif self.fal.txtPropietario.text()=="":
                m.setText("Capture Nombre Propietario")
                self.fal.txtPropietario.setFocus()
                
            else:
                reg_local=RegLocal(
                    num_local=self.fal.txtLocal.text().upper(),
                    superficie=self.fal.txtSuperficie.text(),
                    cuota=self.fal.txtCuota.text(),
                    dg=0,
                    nom_propietario=self.fal.txtPropietario.text().upper(),
                    rfc_propietario=self.fal.txtRFC_p.text().upper(),
                    cliente=self.fal.cmbClientes.currentText().upper(),
                    giro=self.fal.txtGiro.text().upper(),
                    status=False,
                    usuario=self.pp.lblName_User.text(),
                    fechareg=current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                    )
                objData=RegLocalData() 
                if  objData.registrar(info=reg_local):
                    m.setText("Local registrado con exito")
                    self.limpiar_campos_fal()
                else:
                    m.setText("El Local  " + self.fal.txtLocal.text() + "   ya esta registrado")
                    self.limpiar_campos_fal()  
            m.exec()
    
    def set_cmb_clientes(self):
        obj=ClientesData()
        datos=obj.lista_clientes()
        for item in datos:
            self.fal.cmbClientes.addItem(item[1])
          
    def limpiar_campos_fal(self):
        self.fal.txtLocal.setText("L-")
        self.fal.txtSuperficie.setText("")
        self.fal.txtCuota.setText("")
        self.fal.txtPropietario.setText("")
        self.fal.txtRFC_p.setText("XAXX010101000")
        self.fal.cmbClientes.setCurrentIndex(0)
        self.fal.txtGiro.setText("")        
     
    def salir_form_local(self):
        self.fal.close()        
     
          
 #################################ALTA AREAS COMUNES##############################################   
    def abrir_form_alta_AC(self):
       #self.fac=uic.loadUi(self.resource_path("C:/Users/smart/OneDrive/Escritorio/gac_py_V1.02/gui/formAreasComunes.ui"))
        self.fac=uic.loadUi(self.resource_path("gui/formAreasComunes.ui"))
        self.fac.setWindowTitle("Alta area comun")
        self.fac.show()
        self.fac.checkBoxStatus.setChecked(True)
        self.fac.txtArea.setText("A-")
        self.set_cmb_cliente()
        self.fac.btnGuardar.clicked.connect(self.registrar_area)
        self.fac.btnSalir.clicked.connect(self.salir_form_area)
        
    def set_cmb_cliente(self):
        obj=ClientesData()
        datos=obj.lista_clientes()
        for item in datos:
            self.fac.cmbClientes.addItem(item[1])    
 
    def registrar_area(self):
        m=QMessageBox()
        m.setIcon(QMessageBox.Icon.Information)
        m.setWindowTitle("Alta area comun")
        m.setStandardButtons(QMessageBox.StandardButton.Ok)
        
        if self.fac.txtArea.text()=="":       
            m.setText("Capture numero de Area Comun")
            self.fac.txtArea.setFocus()
            
        elif len(self.fac.txtArea.text())<4:
            m.setText("Numero de Area Comun incorrecto")
            self.fac.txtArea.setFocus()
                
        elif self.fac.txtSuperficie.text()=="":
            m.setText(" Capture superficie m2")
            self.fac.txtSuperficie.setFocus()
        
        elif not self.fac.txtSuperficie.text().replace('.','',1).isnumeric():   
            m.setText("Captura solo numeros")
            self.fac.txtSuperficie.setText('0.00')
            self.fac.txtSuperficie.setFocus()    
                        
        elif self.fac.cmbClientes.currentIndex()==0:
            m.setText("Seleccione una opcion")
            self.fac.cmbClientes.setFocus()
    
        elif self.fac.txtGiro.text()=="":
            m.setText("Capture Giro del Area Comun")
            self.fac.txtGiro.setFocus()
        
        elif  self.fac.txtCuota.text()=="":
            m.setText("Capture Cuota Mensual")        
            self.fac.txtCuota.setFocus()
            
        elif not self.fac.txtCuota.text().replace('.',"" ,1).isnumeric():   
            m.setText("Captura solo numeros")
            self.fac.txtCuota.setText('0.00')
            self.fac.txtCuota.setFocus()
        
        elif self.fac.cmbTipoArea.currentIndex()==0:
            m.setText("Selecione una opcion")
            self.fac.txtRFC_p.setFocus()
            
        elif self.fac.txtDG.text()=="":
            m.setText("Capture Deposito Garantia")
            self.fac.txtDG.setFocus()
            
        elif not self.fac.txtDG.text().replace('.',"",1).isnumeric():     
            m.setText("Captura solo numeros")
            self.fac.txtDG.setText('0.00')
            self.fac.txtDG.setFocus()    
        else:
            reg_area=RegAC(
                num_area=self.fac.txtArea.text().upper(),
                cliente_fact=self.fac.cmbClientes.currentText().upper(),
                cuota=self.fac.txtCuota.text(),
                dg=self.fac.txtDG.text(),
                tipo_area=self.fac.cmbTipoArea.currentText(),
                cantidad=1,
                sup=self.fac.txtSuperficie.text(),
                giro=self.fac.txtGiro.text().upper(),
                contrato="",
                status=False,
                fReg=current_datetime.strftime("%Y-%m-%d %H:%M:%S"),
                usuario=self.pp.lblName_User.text()
                )
            objData=RegACData()
            if  objData.registrar(info=reg_area):
                m.setText("Area Comun registrada con exito")
                self.limpiar_campos_fac()
            else:
                m.setText("El Area Comun  " + self.fac.txtArea.text() + "   ya esta registrado")
                self.limpiar_campos_fac()
        m.exec()
     
    def limpiar_campos_fac(self):
        self.fac.txtArea.setText("A-")
        self.fac.txtSuperficie.setText("")
        self.fac.txtCuota.setText("")
        self.fac.cmbClientes.setCurrentIndex(0)
        self.fac.txtGiro.setText("")  
        self.fac.txtDG.setText("") 
        self.fac.cmbTipoArea.setCurrentIndex(0)    
        
    def salir_form_area(self):
        self.fac.close()   
  
               
 #######################   PANTALLA PRINCIPAL GESTOR LOCALES COMERCIALES#############################################         
    def abrir_form_PPCM(self):
        #self.ppcm = uic.loadUi(self.resource_path("C:/Users/smart/OneDrive/Escritorio/gac_py_V1.02/gui/formPrincipalCM.ui"))
        self.ppcm = uic.loadUi(self.resource_path("gui/formPrincipalCM.ui"))
        self.ppcm.setWindowTitle("Cartera Locales Comerciales")
        self.ppcm.show()
        self.set_cmb_locales_ppcm()
        self.ppcm.cmblocal.currentIndexChanged.connect(self.set_cmb_cliente_ppcm)
        self.ppcm.btnBuscar.clicked.connect(self.mostrar_informacionCM)
        self.ppcm.btnRegCob.clicked.connect(self.validar_campos_PPCM)
        self.ppcm.btnRegFact.clicked.connect(self.abrir_form_facturacionCM)
        self.ppcm.btnEdoCta.clicked.connect(self.exportar_info_a_excelCM)
        self.ppcm.btnSalir.clicked.connect(self.salir_form_PPCM)
                  
    def set_cmb_locales_ppcm(self):
        obj= UbicacionesData()   
        datos=obj.lista_ubicaciones()
        for item in datos:
            self.ppcm.cmblocal.addItem(item[1])
            
    def set_cmb_cliente_ppcm(self,cliente):
        search=BuscarCliente()
        data=search.buscar_cliente(self.ppcm.cmblocal.currentText())
        self.ppcm.tblCarteraCM.clearContents()
        self.ppcm.tblCarteraCM.setRowCount(0)
        self.ppcm.txtSaldo.setText("")
        self.ppcm.txtCliente.setText("")   
        for item in data:
            self.ppcm.txtCliente.setText(item[7])          
                                
    def validar_campos_PPCM(self): 
        if self.ppcm.cmblocal.currentIndex()==0:
            m=QMessageBox()
            m.setIcon(QMessageBox.Icon.Information)
            m.setWindowTitle("registro cobranza cuotas")
            m.setText("Seleccione una opcion")
            m.exec()
        else:
            self.abrir_form_pagosCM()
            
    def salir_form_PPCM(self):
        self.ppcm.close()         
    
    
################################## PAGOS---COBRANZA---LC --######################################        
    def abrir_form_pagosCM(self):
        #self.fpcm=uic.loadUi("gui/formRegPagosCM.ui")
        #self.fpcm = uic.loadUi(self.resource_path("C:/Users/smart/OneDrive/Escritorio/gac_py_V1.02/gui/formRegPagosCM.ui"))
        self.fpcm = uic.loadUi(self.resource_path("gui/formRegPagosCM.ui"))
        self.fpcm.setWindowTitle("registro cobranza cuotas")
        self.fpcm.show()
        self.set_cmb_factura_fpcm()
        self.set_cmb_cta_banco_fpcm()
        self.fpcm.btnRegistrar.clicked.connect(self.registrar_cobranzaCM)
        self.fpcm.btnSalir.clicked.connect(self.salir_form_pagosCM) 
        self.fpcm.txtLocal.setText(self.ppcm.cmblocal.currentText())
        
    def set_cmb_factura_fpcm(self):
        search=FacturasData()
        data=search.lista_facturas(self.ppcm.cmblocal.currentText(),self.ppcm.txtCliente.text())
        for item in data:
            self.fpcm.cmbFactura.addItem(item[6])
            
    def set_cmb_cta_banco_fpcm(self):
        obj=ctasbancos.CuentasData()
        datos=obj.lista_ctas()
        for item in datos:
            self.fpcm.cmbCtaBancaria.addItem(item[2])
              
    def registrar_cobranzaCM(self):
        m=QMessageBox()
        m.setIcon(QMessageBox.Icon.Information)
        m.setWindowTitle("registro cobranza")
        m.setStandardButtons(QMessageBox.StandardButton.Ok)
        
        if self.fpcm.cmbFactura.currentIndex()==0:
            m.setText("selecciona una opcion")     
            self.fpcm.cmbFactura.setFocus()        
        
        elif self.fpcm.cmbTipoCuota.currentIndex()==0:
            m.setText("selecciona una opcion")
            self.fpcm.cmbTipoCuota.setFocus()
                            
        elif self.fpcm.txtImporte.text()=="":
            m.setText("captura un importe")
            self.fpcm.txtImporte.setFocus()
            
        elif not self.fpcm.txtImporte.text().replace('.', '', 1).isnumeric():      
            m.setText("captura solo numeros")
            self.fpcm.txtImporte.setText('0.00')
            self.fpcm.txtImporte.setFocus()
              
        elif self.fpcm.cmbFormaPago.currentIndex()==0:
            m.setText("selecciona una opcion")
            self.fpcm.cmbFormaPago.setFocus()        
        
        elif self.fpcm.cmbCtaBancaria.currentIndex()==0:
            m.setText("selecciona una opcion")
            self.fpcm.cmbCtaBancaria.setFocus()
             
        else:
            regpago=Reg_Cobranza(   
                num_fact=self.fpcm.cmbFactura.currentText(),
                fecha_pago=self.fpcm.boxDate.date().toString("yyyy-MM-dd"),
                importe_pago=self.fpcm.txtImporte.text(),
                forma_pago=self.fpcm.cmbFormaPago.currentText(),
                cta_banco=self.fpcm.cmbCtaBancaria.currentText(),
                num_cheque=self.fpcm.txtCheque.text(),
                tipoCuota=self.fpcm.cmbTipoCuota.currentText(),
                usuario=self.pp.lblName_User.text(),
                fechaReg=current_datetime.strftime("%Y-%m-%d %H:%M:%S"),
                comentarios=self.fpcm.txtComentarios.toPlainText()
                )
            objData=RegCobranzaData()
            if  objData._registrar(info=regpago):
                m.setText("pago registrado con exito")
            
                reg_bd_c=Reg_Cartera(
                    local_o_area=self.fpcm.txtLocal.text(),
                    clienteFact=self.ppcm.txtCliente.text(),
                    tipoCartera="locales comerciales",
                    tipoCuota=self.fpcm.cmbTipoCuota.currentText(),
                    tipo_factura="pago",
                    numFact=self.fpcm.cmbFactura.currentText(),
                    importeAdeudo=0,
                    importePago=self.fpcm.txtImporte.text(),
                    fPago_Cobro=self.fpcm.boxDate.date().toString("yyyy-MM-dd"),
                    ctaBanco=self.fpcm.cmbCtaBancaria.currentText(),    
                    formaPago=self.fpcm.cmbFormaPago.currentText(),
                    cheque=self.fpcm.txtCheque.text(),
                    numContrato="",
                    statusPago="",
                    usuario=self.pp.lblName_User.text(),
                    fechaReg=current_datetime.strftime("%Y-%m-%d %H:%M:%S"),
                    comentarios=self.fpcm.txtComentarios.toPlainText()
                    )
                objData=RegCarteraData()
                if  objData._registrar(info=reg_bd_c):
                    m.setText("registro cartera exitoso")
                    self.limpiar_campos_fpcm()
                else:
                    m.setText("registro cartera no exitoso")
                    self.limpiar_campos_fpcm() 
            else:
                m.setText("pago no registrado")
                self.limpiar_campos_fpcm()  
        m.exec()
    
    def limpiar_campos_fpcm(self):
        self.fpcm.cmbFactura.setCurrentIndex(0)
        self.fpcm.cmbTipoCuota.setCurrentIndex(0)
        self.fpcm.txtImporte.setText("")
        self.fpcm.cmbFormaPago.setCurrentIndex(0)
        self.fpcm.cmbCtaBancaria.setCurrentIndex(0)
        self.fpcm.txtCheque.setText("")
        self.fpcm.txtComentarios.setText("")
    
    def salir_form_pagosCM(self):
        self.fpcm.close() 
    
    
####################################### ---FACTURACION INDIVIDUAL--LC--######################################          
    def abrir_form_facturacionCM(self):
        if self.ppcm.cmblocal.currentIndex()==0:
            m=QMessageBox()
            m.setWindowTitle("registro facturas cuotas")
            m.setIcon(QMessageBox.Icon.Information)
            m.setText("Selecciona una Opcion")
            m.exec()
            self.ppcm.cmblocal.setFocus()
        else:    
            #self.ffcm=uic.loadUi("gui/formRegFacturasCM.ui")
            #self.ffcm = uic.loadUi(self.resource_path("C:/Users/smart/OneDrive/Escritorio/gac_py_V1.02/gui/formRegFacturasCM.ui"))
            self.ffcm = uic.loadUi(self.resource_path("gui/formRegFacturasCM.ui"))
            self.ffcm.setWindowTitle("registro facturas cuotas")
            self.ffcm.show()
            self.ffcm.txtNumFact.setText("F-")
            self.ffcm.txtLocal.setText(self.ppcm.cmblocal.currentText())
            self.ffcm.btnRegistrar.clicked.connect(self.registrar_facturacionCM) 
            self.ffcm.btnSalir.clicked.connect(self.salir_form_facturacionCM)   
        
    def registrar_facturacionCM(self):
        m=QMessageBox()
        m.setIcon(QMessageBox.Icon.Information)
        m.setWindowTitle("registro facturas")
        m.setStandardButtons(QMessageBox.StandardButton.Ok)
            
        if self.ffcm.txtLocal.text()=="":
            m.setText("captura numero local")
            self.ffcm.txtLocal.setFocus()
                        
        elif self.ffcm.cmbTipoCuota.currentIndex()==0:
            m.setText("selecciona una opcion")     
            self.ffcm.cmbTipoCuota.setFocus()
        
        elif self.ffcm.txtNumFact.text()=="":
            m.setText("captura una factura")
            self.ffcm.txtNumFact.setFocus()
                
        elif self.ffcm.txtImporte.text()=="":
            m.setText("captura un importe")
            self.ffcm.txtImporte.setFocus()
            
        elif not self.ffcm.txtImporte.text().replace('.', '', 1).isnumeric():      
            m.setText("captura solo numeros")
            self.ffcm.txtImporte.setText('0.00')
            self.ffcm.txtImporte.setFocus()
                
        else:
            regfact=Reg_Factura(   
                num_factura=self.ffcm.txtNumFact.text().upper(),
                cliente=self.ppcm.txtCliente.text(),
                local_o_area=self.ffcm.txtLocal.text().upper(),
                fecha_factura=self.ffcm.boxDate.date().toString("yyyy-MM-dd"),
                tipo_cuota=self.ffcm.cmbTipoCuota.currentText(),
                importe_factura=self.ffcm.txtImporte.text(),
                tipo_factura=self.ffcm.cmbTipoFact.currentText(),
                tipo_cartera="locales comerciales",
                status_pago=False,
                usuario=self.pp.lblName_User.text(),
                fecha_reg=current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                )
            objData=RegFacturaData()
            if  objData._registrar(info=regfact):
                m.setText("factura registrada con exito")
    
                if self.ffcm.cmbTipoFact.currentIndex() == 2 or self.ffcm.cmbTipoFact.currentIndex() == 3:
                    importeAdeudo = -1 * float(self.ffcm.txtImporte.text())
                else:
                    importeAdeudo = float(self.ffcm.txtImporte.text())
                
                reg_bd_c=Reg_Cartera(
                    local_o_area=self.ffcm.txtLocal.text().upper(),
                    clienteFact=self.ppcm.txtCliente.text(),
                    tipoCartera="locales comerciales",
                    tipoCuota=self.ffcm.cmbTipoCuota.currentText(),
                    tipo_factura=self.ffcm.cmbTipoFact.currentText(),
                    numFact=self.ffcm.txtNumFact.text().upper(),
                    importeAdeudo=importeAdeudo,
                    importePago=0,
                    fPago_Cobro=self.ffcm.boxDate.date().toString("yyyy-MM-dd"), 
                    ctaBanco="",
                    formaPago="",
                    cheque="",
                    numContrato="",
                    statusPago=False,
                    usuario=self.pp.lblName_User.text(),
                    fechaReg=current_datetime.strftime("%Y-%m-%d %H:%M:%S"),
                    comentarios=self.ffcm.txtComentarios.toPlainText()
                    )
                objData=RegCarteraData()
                if  objData._registrar(info=reg_bd_c):
                    m.setText("registro cartera exitoso")
                    self.limpiar_campos_ffcm()
                else:
                    m.setText("registro cartera no exitoso")   
                    self.limpiar_campos_ffcm()
            else:
                m.setText("factura no registrada")
                self.limpiar_campos_ffcm()
        m.exec()
        
    def limpiar_campos_ffcm(self):
        self.ffcm.cmbTipoCuota.setCurrentIndex(0)
        self.ffcm.txtNumFact.setText("")
        self.ffcm.txtImporte.setText("")
        self.ffcm.cmbTipoFact.setCurrentIndex(0)
        self.ffcm.txtComentarios.setText("")

    def salir_form_facturacionCM(self):
        self.ffcm.close()   
   
   
#############################PANTALLA PRINCIPAL GESTOR AREAS COMUNES#############################################    
    def abrir_form_PPAC(self):
        #self.ppac = uic.loadUi("gui/formPrincipalAC.ui")
        #self.ppac = uic.loadUi(self.resource_path("C:/Users/smart/OneDrive/Escritorio/gac_py_V1.02/gui/formPrincipalAC.ui"))
        self.ppac = uic.loadUi(self.resource_path("gui/formPrincipalAC.ui"))
        self.ppac.setWindowTitle("Cartera Areas Comunes")
        self.ppac.show()   
        self.set_cmb_contratos_PPAC()
        self.ppac.cmbContrato.currentIndexChanged.connect(self.set_cmb_area_PPAC)
        self.ppac.btnBuscar.clicked.connect(self.mostrar_informacionAC)
        self.ppac.btnRegCob.clicked.connect(self.validar_campos_PPAC)
        self.ppac.btnRegFact.clicked.connect(self.abrir_form_facturacionAC)
        self.ppac.btnEdoCta.clicked.connect(self.exportar_info_a_excelAC)
        self.ppac.btnSalir.clicked.connect(self.salir_form_PPAC)
  
    def validar_campos_PPAC(self): 
        if self.ppac.cmbContrato.currentIndex()==0: 
            m=QMessageBox()
            m.setWindowTitle("registrar cobranza")
            m.setIcon(QMessageBox.Icon.Information)
            m.setText("Selecciona una opcion")
            m.exec()
        else:
            self.abrir_form_pagosAC()
            
    def set_cmb_contratos_PPAC(self):
        search=ContratosData()
        data=search.lista_contratos()
        for item in data:
            self.ppac.cmbContrato.addItem(item[1]) 
            
    def set_cmb_area_PPAC(self,contrato):
        search=AreasData()
        data=search.lista_areas_x_contrato(self.ppac.cmbContrato.currentText())
        self.ppac.cmbAreaC.clear()
        self.ppac.txtCliente.setText("")
        self.ppac.tblCarteraAC.clearContents()
        self.ppac.tblCarteraAC.setRowCount(0)
        self.ppac.txtSaldo.setText("")   
        for item in data:
            self.ppac.cmbAreaC.addItem(item[3])
            self.ppac.txtCliente.setText(item[2])
                  
    def salir_form_PPAC(self):
        self.ppac.close()    
    
    
################################## PAGOS---COBRANZA--AC --######################################        
    def abrir_form_pagosAC(self):
        #self.fpac=uic.loadUi("gui/formRegPagosAC.ui")
        #self.fpac = uic.loadUi(self.resource_path("C:/Users/smart/OneDrive/Escritorio/gac_py_V1.02/gui/formRegPagosAC.ui"))
        self.fpac = uic.loadUi(self.resource_path("gui/formRegPagosAC.ui"))
        self.fpac.setWindowTitle("registro cobranza cuotas")
        self.fpac.show()
        self.set_cmb_factura_fpac()
        self.set_cmb_cta_banco_fpac()
        self.fpac.txtAreaC.setText(self.ppac.cmbAreaC.currentText())
        self.fpac.btnRegistrar.clicked.connect(self.registrar_cobranzaAC)
        self.fpac.btnSalir.clicked.connect(self.salir_form_pagosAC)
        
    def set_cmb_factura_fpac(self):
        search=FacturasData()
        data=search.lista_facturas(self.ppac.cmbAreaC.currentText(),self.ppac.txtCliente.text())
        for item in data:
            self.fpac.cmbFactura.addItem(item[6])
            
    def set_cmb_cta_banco_fpac(self):
        obj=ctasbancos.CuentasData()
        datos=obj.lista_ctas()
        for item in datos:
            self.fpac.cmbCtaBancaria.addItem(item[2])        
             
    def registrar_cobranzaAC(self):
        m=QMessageBox()
        m.setIcon(QMessageBox.Icon.Information)
        m.setWindowTitle("registro cobranza")
        m.setStandardButtons(QMessageBox.StandardButton.Ok)
                
        if self.fpac.txtAreaC.text()=="":
            m.setText("captura numero area")
            self.fpac.txtAreaC.setFocus()
                        
        elif self.fpac.cmbTipoCuota.currentIndex()==0:
            m.setText("selecciona una opcion")     
            self.fpac.cmbTipoCuota.setFocus()
        
        elif self.fpac.cmbFactura.currentIndex()==0:
            m.setText("selecciona una opcion")
            self.fpac.cmbFactura.setFocus()
                
        elif self.fpac.txtImporte.text()=="":
            m.setText("captura un importe")
            self.fpac.txtImporte.setFocus()
            
        elif not self.fpac.txtImporte.text().replace('.', '', 1).isnumeric():      
            m.setText("captura solo numeros")
            self.fpac.txtImporte.setText('0.00')
            self.fpac.txtImporte.setFocus()
              
        elif self.fpac.cmbFormaPago.currentIndex()==0:
            m.setText("selecciona una opcion")
            self.fpac.cmbFormaPago.setFocus()        
        
        elif self.fpac.cmbCtaBancaria.currentIndex()==0:
            m.setText("selecciona una opcion")
            self.fpac.cmbCtaBancaria.setFocus()
                
        else:
            regpago=Reg_Cobranza(   
                num_fact=self.fpac.cmbFactura.currentText(),
                fecha_pago=self.fpac.boxDate.date().toString("yyyy-MM-dd"),
                importe_pago=self.fpac.txtImporte.text(),
                forma_pago=self.fpac.cmbFormaPago.currentText(),
                cta_banco=self.fpac.cmbCtaBancaria.currentText(),
                num_cheque=self.fpac.txtCheque.text(),
                tipoCuota=self.fpac.cmbTipoCuota.currentText(),
                usuario=self.pp.lblName_User.text(),
                fechaReg=current_datetime.strftime("%Y-%m-%d %H:%M:%S"),
                comentarios=self.fpac.txtComentarios.toPlainText()
                )
            objData=RegCobranzaData()
            if  objData._registrar(info=regpago):
                m.setText("pago registrado con exito")
            
                carga=Reg_Cartera(
                local_o_area=self.fpac.txtAreaC.text(),
                clienteFact=self.ppac.txtCliente.text(),
                tipoCartera="areas comunes",
                tipo_factura="pago",
                tipoCuota=self.fpac.cmbTipoCuota.currentText(),
                numFact=self.fpac.cmbFactura.currentText(),
                importeAdeudo=0,
                importePago=self.fpac.txtImporte.text(),
                fPago_Cobro=self.fpac.boxDate.date().toString("yyyy-MM-dd"), 
                ctaBanco=self.fpac.cmbCtaBancaria.currentText(),
                formaPago=self.fpac.cmbFormaPago.currentText(),
                cheque=self.fpac.txtCheque.text(),
                numContrato=self.ppac.cmbContrato.currentText(),
                statusPago="",
                usuario=self.pp.lblName_User.text(),
                fechaReg=current_datetime.strftime("%Y-%m-%d %H:%M:%S"),
                comentarios=self.fpac.txtComentarios.toPlainText()
                )
                objData=RegCarteraData()
                if  objData._registrar(info=carga):
                    m.setText("registro cartera exitoso")
                    self.limpiar_campos_fpac()
                else:
                    m.setText("registro cartera no exitoso") 
                    self.limpiar_campos_fpac()
            else:
                m.setText("pago no registrado")  
                self.limpiar_campos_fpac()
        m.exec()
        
    def limpiar_campos_fpac(self):
        self.fpac.cmbFactura.setCurrentIndex(0)
        self.fpac.cmbTipoCuota.setCurrentIndex(0)
        self.fpac.txtImporte.setText("")
        self.fpac.cmbFormaPago.setCurrentIndex(0)
        self.fpac.cmbCtaBancaria.setCurrentIndex(0)
        self.fpac.txtCheque.setText("")
        self.fpac.txtComentarios.setText("")
                
    def salir_form_pagosAC(self):
        self.fpac.close() 

        
################################## ---FACTURACION INDIVIDUAL--AC --######################################           
    def abrir_form_facturacionAC(self):
        if self.ppac.cmbContrato.currentIndex()==0:
            m=QMessageBox()
            m.setWindowTitle("registro facturas")
            m.setIcon(QMessageBox.Icon.Information)
            m.setText("Selecciona una Opcion")
            m.exec()
            self.ppac.cmbContrato.setFocus()
        else:
            #self.ffac=uic.loadUi("gui/formRegFacturasAC.ui")
            #self.ffac = uic.loadUi(self.resource_path("C:/Users/smart/OneDrive/Escritorio/gac_py_V1.02/gui/formRegFacturasAC.ui"))
            self.ffac = uic.loadUi(self.resource_path("gui/formRegFacturasAC.ui"))
            self.ffac.setWindowTitle("registro facturas cuotas")
            self.ffac.show()
            self.ffac.txtNumFact.setText("F-")
            self.ffac.txtAreaC.setText(self.ppac.cmbAreaC.currentText())
            self.ffac.btnRegistrar.clicked.connect(self.registrar_facturacionAC) 
            self.ffac.btnSalir.clicked.connect(self.salir_form_facturacionAC)   
            
    def registrar_facturacionAC(self):
        m=QMessageBox()
        m.setIcon(QMessageBox.Icon.Warning)
        m.setWindowTitle("registro facturacion")
        m.setStandardButtons(QMessageBox.StandardButton.Ok)
                
        if self.ffac.txtAreaC.text()=="":
            m.setText("captura numero area")
            self.ffac.txtAreaC.setFocus()
                    
        elif self.ffac.cmbTipoCuota.currentIndex()==0:
            m.setText("selecciona una opcion")     
            self.ffac.cmbTipoCuota.setFocus()
        
        elif self.ffac.txtNumFact.text()=="":
            m.setText("captura una factura")
            self.ffac.txtNumFact.setFocus()
                
        elif self.ffac.txtImporte.text()=="":
            m.setText("captura un importe")
            self.ffac.txtImporte.setFocus()
            
        elif not self.ffac.txtImporte.text().replace('.', '', 1).isnumeric():      
            m.setText("captura solo numeros")
            self.ffac.txtImporte.setText('0.00')
            self.ffac.txtImporte.setFocus()
                
        else:
            regpago=Reg_Factura(   
                num_factura=self.ffac.txtNumFact.text().upper(),
                cliente=self.ppac.txtCliente.text(),
                local_o_area=self.ffac.txtAreaC.text().upper(),
                fecha_factura=self.ffac.boxDate.date().toString("yyyy-MM-dd"),
                tipo_cuota=self.ffac.cmbTipoCuota.currentText(),
                importe_factura=self.ffac.txtImporte.text(),
                tipo_factura=self.ffac.cmbTipoFact.currentText(),
                tipo_cartera="areas comunes",
                status_pago=False,
                usuario=self.pp.lblName_User.text(),
                fecha_reg=current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                )
            objData=RegFacturaData()
            if  objData._registrar(info=regpago):
                m.setText("factura registrada con exito")

                if self.ffac.cmbTipoFact.currentIndex() == 2 or self.ffac.cmbTipoFact.currentIndex() == 3:
                    importe_Adeudo = -1 * float(self.ffac.txtImporte.text())
                else:
                    importe_Adeudo = float(self.ffac.txtImporte.text())
                
                reg_bd_c=Reg_Cartera(
                    local_o_area=self.ffac.txtAreaC.text().upper(),
                    clienteFact=self.ppac.txtCliente.text(),
                    tipoCartera="areas comunes",
                    tipoCuota=self.ffac.cmbTipoCuota.currentText(),
                    tipo_factura=self.ffac.cmbTipoFact.currentText(),
                    numFact=self.ffac.txtNumFact.text().upper(),
                    importeAdeudo=importe_Adeudo,
                    importePago=0,
                    fPago_Cobro=self.ffac.boxDate.date().toString("yyyy-MM-dd"), 
                    ctaBanco="",
                    formaPago="",
                    cheque="",
                    numContrato=self.ppac.cmbContrato.currentText(),
                    statusPago=False,
                    usuario=self.pp.lblName_User.text(),
                    fechaReg=current_datetime.strftime("%Y-%m-%d %H:%M:%S"),
                    comentarios=self.ffac.txtComentarios.toPlainText()
                    )
                objData=RegCarteraData()
                if  objData._registrar(info=reg_bd_c):
                    m.setText("registro cartera exitoso")
                    self.limpiar_campos_ffac()
                else:
                    m.setText("registro cartera no exitoso")
                    self.limpiar_campos_ffac()
            else:
                m.setText("factura no registrada")           
                self.limpiar_campos_ffac()
        m.exec()
        
    def limpiar_campos_ffac(self):
        self.ffac.cmbTipoCuota.setCurrentIndex(0)
        self.ffac.txtNumFact.setText("")
        self.ffac.txtImporte.setText("")
        self.ffac.cmbTipoFact.setCurrentIndex(0)
        self.ffac.txtComentarios.setText("")        
   
    def salir_form_facturacionAC(self):
        self.ffac.close()   
   
                 
##########################  CLIENTES #########################################   
    def abrir_form_clientes(self):
        #self.fcl=uic.loadUi("gui/formClientes.ui")
        #self.fcl = uic.loadUi(self.resource_path("C:/Users/smart/OneDrive/Escritorio/gac_py_V1.02/gui/formClientes.ui"))
        self.fcl = uic.loadUi(self.resource_path("gui/formClientes.ui"))
        self.fcl.setWindowTitle("Registro Clientes")
        self.fcl.show()
        self.fcl.checkBoxStatus.setChecked(True)
        self.fcl.btnGuardar.clicked.connect(self.registrar_cliente)
        self.fcl.btnSalir.clicked.connect(self.salir_form_clientes)  
       
    def registrar_cliente(self):      
            m=QMessageBox()
            m.setIcon(QMessageBox.Icon.Information)
            m.setWindowTitle("registro clientes")
            m.setStandardButtons(QMessageBox.StandardButton.Ok)
        
            if self.fcl.txtNombreCliente.text()=="":       
                m.setText("Captura un Nombre")
                self.fcl.txtNombreCliente.setFocus()
                    
            elif self.fcl.txtRFC.text()=="":
                m.setText(" Captura RFC")
                self.fcl.txtRFC.setFocus()
                            
            elif self.fcl.cmbTipoCliente.currentIndex()==0:
                m.setText("Selecciona una Opcion")     
                self.fcl.cmbTipoCliente.setFocus()
                
            elif self.fcl.txtEmail.text() == "":
                m.setText("Captura Email")
                self.fcl.txtEmail.setFocus()
                
            elif "@" not in self.fcl.txtEmail.text() or "." not in self.fcl.txtEmail.text():
                m.setText("Captura un Email válido")
                self.fcl.txtEmail.setFocus()
        
            elif self.fcl.txtGiro.text()=="":
                m.setText("Captura Giro")
                self.fcl.txtGiro.setFocus()
            
            elif  self.fcl.txtCel.text()=="":
                m.setText("Captura un numero")        
                self.fcl.txtCel.setFocus()
                
            elif not self.fcl.txtCel.text().isnumeric():      
                m.setText("Captura solo numeros")
                self.fcl.txtCel.setText('5')
                self.fcl.txtCel.setFocus()
            
            elif len(self.fcl.txtCel.text())<10:
                m.setText("Captura un numero correcto")
                self.fcl.txtCel.setFocus()
            else:
                regcliente=RegCliente(
                    nombre=self.fcl.txtNombreCliente.text().upper(),
                    rfc= self.fcl.txtRFC.text().upper(),
                    tContribuyente=self.fcl.cmbTipoCliente.currentText(),
                    curp=self.fcl.txtCURP.text().upper(),
                    num_area_o_local="",
                    giro=self.fcl.txtGiro.text(),
                    direccion=self.fcl.txtDireccion.toPlainText(),
                    numcel=self.fcl.txtCel.text(),
                    email=self.fcl.txtEmail.text().lower(),
                    fechareg=current_datetime.strftime("%Y-%m-%d %H:%M:%S"),
                    usuario=self.pp.lblName_User.text(),
                    status_cliente=self.fcl.checkBoxStatus.isChecked(),
                    tCliente=self.fcl.cmbTipoCliente.currentText()
                    )
                objData=RegClienteData()
                if  objData.registrar(info=regcliente):
                    m.setText("cliente registrado con exito")
                    self.limpiar_campos_fcl()
                else:
                    m.setText("cliente no registrado")       
                    self.limpiar_campos_fcl()
            m.exec()
            
    def limpiar_campos_fcl(self):
        self.fcl.txtNombreCliente.setText("")
        self.fcl.txtRFC.setText("")
        self.fcl.cmbTipoCliente.setCurrentIndex(0)
        self.fcl.txtCURP.setText("")
        self.fcl.txtGiro.setText("")
        self.fcl.txtDireccion.setText("")
        self.fcl.txtCel.setText("")
        self.fcl.txtEmail.setText("")
        #self.fcl.checkBoxStatus.setChecked(True)        

    def salir_form_clientes(self):
        self.fcl.close()     
  
        
#########################CTA BANCARIA#################################################
    def abrir_form_banco(self):
        #self.fban=uic.loadUi("gui/formBanco.ui")
        #self.fban = uic.loadUi(self.resource_path("C:/Users/smart/OneDrive/Escritorio/gac_py_V1.02/gui/formBanco.ui"))
        self.fban = uic.loadUi(self.resource_path("gui/formBanco.ui"))
        self.fban.setWindowTitle("Registro Cuentas Bancarias")
        self.fban.btnGuardar.clicked.connect(self.registrar_cta_banco)
        self.fban.btnSalir.clicked.connect(self.salir_form_banco)
        self.fban.show()
        
    def registrar_cta_banco(self):
        m=QMessageBox()
        m.setIcon(QMessageBox.Icon.Information)
        m.setWindowTitle("Registro Cuentas Bancarias")
        m.setStandardButtons(QMessageBox.StandardButton.Ok)
        
        if self.fban.txtNombreBanco.text()=="":       
            m.setText("Captura nombre del banco")
            self.fban.txtNombreBanco.setFocus()
                
        elif self.fban.txtNumCta.text()=="":
            m.setText(" Captura numero de cta bancaria")
            self.fban.txtNumCta.setFocus()
                        
        elif self.fban.cmbTipoCta.currentIndex()==0:
            m.setText("Selecciona una opcion")
            self.fban.cmbTipoCta.setFocus()
        
        elif self.fban.cmbTipoMoneda.currentIndex()==0:
            m.setText("Selecciona una opcion")
            self.fban.cmbTipoMoneda.setFocus()
        else:    
            regCta=Cuentas(
                nombre_banco=self.fban.txtNombreBanco.text().upper(),
                num_cta=self.fban.txtNumCta.text(),
                tipo_cta=self.fban.cmbTipoCta.currentText(),
                tipo_moneda=self.fban.cmbTipoMoneda.currentText(),
                usuario=self.pp.lblName_User.text(),
                fechareg=current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                )
            objData=RegCtasBancoData()
            if  objData.registrar(info=regCta):
                m.setText("Cuenta Bancaria registrada con exito")
                self.limpiar_campos_fban()
            else:
                m.setText("Cuenta Bancaria ya registrada")
                self.limpiar_campos_fban()
        m.exec()
        
    def limpiar_campos_fban(self):
        self.fban.txtNombreBanco.setText("")
        self.fban.txtNumCta.setText("")
        self.fban.cmbTipoCta.setCurrentIndex(0)
        self.fban.cmbTipoMoneda.setCurrentIndex(0) 
                          
    def salir_form_banco(self):
        self.fban.close()
        
 
##################################REGISTRAR CONTRATOS#############################################
    def abrir_form_contratos(self):
        #self.fcon=uic.loadUi("gui/formContratos.ui")
        #self.fcon = uic.loadUi(self.resource_path("C:/Users/smart/OneDrive/Escritorio/gac_py_V1.02/gui/formContratos.ui"))
        self.fcon = uic.loadUi(self.resource_path("gui/formContratos.ui"))
        self.fcon.setWindowTitle("Registro Contratos Areas Comunes")
        self.fcon.show()
        self.set_cmb_ac()
        self.set_cmb_clientes_c()
        self.numeros_contratos()
        self.fcon.cmbAreaComun.currentIndexChanged.connect(self.set_cuota)
        self.fcon.btnGuardar.clicked.connect(self.registrar_contrato)
        self.fcon.btnSalir.clicked.connect(self.salir_form_contratos)
        
    def set_cmb_ac(self):
        obj=ListaAreasData()
        datos=obj.lista_areasC()   
        for item in datos:
            self.fcon.cmbAreaComun.addItem(item[1])
       
    def set_cuota(self,area):
        obj=ListaCuotasData()
        datos=obj.lista_cuotas_x_area(self.fcon.cmbAreaComun.currentText())
        self.fcon.txtCuota.setText("")
        for item in datos:
            self.fcon.txtCuota.setText(str(item[3]))
            self.fcon.txtDG.setText(str(item[4]))
            
    def set_cmb_clientes_c(self):
        search=ClientesData()
        data=search.lista_clientes()
        for item in data:
            self.fcon.cmbCliente.addItem(item[1])        
           
    def registrar_contrato(self):
        m=QMessageBox()
        m.setIcon(QMessageBox.Icon.Information)
        m.setWindowTitle("contratos areas comunes")
        m.setStandardButtons(QMessageBox.StandardButton.Ok)
        
        fecha_ini=self.fcon.dateInicial.date().toString("yyyy-MM-dd")
        fecha_fin=self.fcon.dateFinal.date().toString("yyyy-MM-dd")
        area_comun=self.fcon.cmbAreaComun.currentText()
        cliente=self.fcon.cmbCliente.currentText()
        
        if self.fcon.cmbAreaComun.currentIndex()==0:
            m.setText("Selecciona una Opcion")
            self.fcon.cmbAreaComun.setFocus()
        elif self.fcon.cmbCliente.currentIndex()==0:
            m.setText("Selecciona una Opcion")
            self.fcon.cmbCliente.setFocus()
        elif self.fcon.cmbTipoContrato.currentIndex()==0:
            m.setText("Selecciona una Opcion")
            self.fcon.cmbTipoContrato.setFocus()
        elif fecha_ini == fecha_fin:
            m.setText("Fecha inicial igual a la final")
            self.fcon.dateInicial.setFocus()  
        elif fecha_ini > fecha_fin:
            m.setText("Fecha inicial mayor a la final")
            self.fcon.dateInicial.setFocus()            
        else:       
            regContrato=RegContrato(
                n_contrato=self.fcon.txtNumContrato.text(),
                c_facturacion=cliente,
                n_area=area_comun,
                f_inicio=fecha_ini,
                f_fin=fecha_fin,
                m_cuota=self.fcon.txtCuota.text(),
                m_dg=self.fcon.txtDG.text(),
                t_contrato=self.fcon.cmbTipoContrato.currentText(),
                s_contrato=True,
                s_vigencia=self.vigencia(),
                r_usuario=self.pp.lblName_User.text(),
                f_registro=current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                )
            objData=RegContratoData()
            if objData.obtener_contrato_x_fechaInio_fechaFinal(fecha_ini,fecha_fin,area_comun):
                m.setText("el area comun:  "  + area_comun +  "   tiene contrato en ese periodo")
                self.limpiar_campos_fcon()
            else:
                if  objData.registrar(info=regContrato):
                    m.setText("Contrato registrado con exito")
                    self.limpiar_campos_fcon()
                else:
                    m.setText("Contrato no registrado")
                    self.limpiar_campos_fcon()
        m.exec()
    
    def vigencia(self):
        fechaFin=self.fcon.dateFinal.date().toString("yyyy-MM-dd")
        if fechaFin < current_datetime.strftime("%Y-%m-%d"):
            return True
        else:
            return False
        
    def numeros_contratos(self):
            objData = RegContratoData()
            last_contract = objData.obtener_ultimo_contrato()                
            if last_contract:
                last_contract_number = str(last_contract[0][0])
                if '-' in last_contract_number:
                    last_number = int(last_contract_number.split('-')[1])
                else:
                    last_number = int(last_contract_number)
                new_number = last_number + 1
                new_contract_number = f"C-{new_number:04d}"  #04d = 0001
                self.fcon.txtNumContrato.setText(new_contract_number)
            else:
                new_contract_number = "C-0001"
                self.fcon.txtNumContrato.setText(new_contract_number)
            
    def limpiar_campos_fcon(self):
        self.fcon.cmbAreaComun.setCurrentIndex(0)
        self.fcon.cmbCliente.setCurrentIndex(0)
        self.fcon.cmbTipoContrato.setCurrentIndex(0)
        self.fcon.txtCuota.setText("")
        self.fcon.txtDG.setText("")  
        self.numeros_contratos()
            
    def salir_form_contratos(self):
        self.fcon.close()        

   
##################################BUSCAR Y EDITAR CONTRATOS#############################################           
    def abrir_form_buscar_contratos(self):
        #self.fbc=uic.loadUi("gui/formBcontratos.ui")
        #self.fbc = uic.loadUi(self.resource_path("C:/Users/smart/OneDrive/Escritorio/gac_py_V1.02/gui/formBcontratos.ui"))
        self.fbc = uic.loadUi(self.resource_path("gui/formBcontratos.ui"))
        self.fbc.setWindowTitle("Buscar y Editar Contratos Areas Comunes")
        self.fbc.show()
        self.set_lista_contratos()
        self.fbc.cmbContrato.setCurrentIndex(0)
        self.fbc.checkBvencido.setEnabled(False)
        self.fbc.txtCliente.setReadOnly(True)
        self.fbc.txtArea.setReadOnly(True)
        self.fbc.cmbContrato.currentIndexChanged.connect(self.get_info_contrato)
        self.fbc.btnEditar.clicked.connect(self.guardar_edicion)
        self.fbc.btnSalir.clicked.connect(self.salir_fbc)
        
    def set_lista_contratos(self):
        search=RegContratoData()
        data=search.lista_contratos()
        for item in data:
            self.fbc.cmbContrato.addItem(item[1])   
     
    def get_info_contrato(self,contrato):
        search=RegContratoData()
        data=search.info_contratos(self.fbc.cmbContrato.currentText())
        if data==[]:
                m=QMessageBox()
                m.setWindowTitle("buscar contrato")
                m.setIcon(QMessageBox.Icon.Information)
                m.setText("No hay informacion")
                m.exec()
        else:
            for item in data:
                self.fbc.txtCliente.setText(item[0])
                self.fbc.txtArea.setText(item[1])
                self.fbc.txtfecha_ini.setText(item[2])
                self.fbc.txtfecha_fin.setText(item[3])
                self.fbc.txtCuota.setText(f"{item[4]:.2f}")
                self.fbc.txtDG.setText(f"{item[5]:.2f}")
                self.fbc.checkBActivo.setChecked(item[6].lower()=='true')
                self.fbc.checkBvencido.setChecked(item[7].lower() == 'true')

            if not self.fbc.checkBActivo.isChecked():
                self.fbc.txtfecha_ini.setReadOnly(True)
                self.fbc.txtfecha_fin.setReadOnly(True)
                self.fbc.txtCuota.setReadOnly(True)
                self.fbc.txtDG.setReadOnly(True)
                self.fbc.btnEditar.setEnabled(False)
            else:
                self.fbc.txtfecha_ini.setReadOnly(False)
                self.fbc.txtfecha_fin.setReadOnly(False)
                self.fbc.txtCuota.setReadOnly(False)
                self.fbc.txtDG.setReadOnly(False)
                self.fbc.btnEditar.setEnabled(True)
                             
    def guardar_edicion(self):
        if self.fbc.cmbContrato.currentIndex()==0:
            m=QMessageBox()
            m.setIcon(QMessageBox.Icon.Information)
            m.setWindowTitle("Edicion Contratos")
            m.setText("Selecciona una Opcion")
            m.exec()
        else:
            m=QMessageBox()
            m.setIcon(QMessageBox.Icon.Information)
            m.setWindowTitle("Edicion Contratos")
            m.setText("Se editaran los datos del contrato,\ncontinuar...?")
            m.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
            res=m.exec()
            
            if res == QMessageBox.StandardButton.Ok:
                editContrato=EditContrato(
                    n_contrato=self.fbc.cmbContrato.currentText(),
                    #c_facturacion=self.fbc.txtCliente.text(),
                    #n_area=self.fbc.txtArea.text(),
                    f_inicio=self.fbc.txtfecha_ini.text(),
                    f_fin=self.fbc.txtfecha_fin.text(),
                    m_cuota=self.fbc.txtCuota.text(),
                    m_dg=self.fbc.txtDG.text(),
                    s_contrato=self.fbc.checkBActivo.isChecked(),
                    #s_vigencia=self.fbc.checkBvencido.isChecked(),
                    r_usuario=self.pp.lblName_User.text(),
                    f_registro=current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                    )
                objData=EditContratoData()
                if  objData.editar(info=editContrato):
                    m=QMessageBox()
                    m.setIcon(QMessageBox.Icon.Information)
                    m.setWindowTitle("Edicion Contratos AC")
                    m.setText("Contrato editado con exito")
                    m.exec()
                    self.limpiar_campos()
                    self.get_info_contrato(self.fbc.cmbContrato.currentText())
                    
                else:
                    m.setIcon(QMessageBox.Icon.Information)
                    m.setWindowTitle("Edicion Contratos AC")
                    m=QMessageBox()
                    m.setText("Contrato no editado")
                    m.exec()
                
            elif res == QMessageBox.StandardButton.Cancel:
                m.close()
                
    def limpiar_campos(self):
        #self.fbc.cmbContrato.setCurrentIndex(0)
        self.fbc.txtCliente.setText("")
        self.fbc.txtArea.setText("")
        self.fbc.txtfecha_ini.setText("")
        self.fbc.txtfecha_fin.setText("")
        self.fbc.txtCuota.setText("")
        self.fbc.txtDG.setText("")
        self.fbc.checkBActivo.setChecked(False)
        self.fbc.checkBvencido.setChecked(False)            
                
    def salir_fbc(self):
        self.fbc.close()
    
                 
#####################################TABLA DE INFORMACION CUOTAS MANTTO############################################          
    def mostrar_informacionCM(self):
        if self.ppcm.cmblocal.currentIndex()==0 :
            m=QMessageBox()
            m.setIcon(QMessageBox.Icon.Information)
            m.setWindowTitle("informacion cartera")
            m.setText("Seleccione una Opcion")
            m.exec()
            self.ppcm.cmblocal.setFocus()
        else:    
            search=CarteraDataCM()
            data=search.buscar_info_ubicacion(self.ppcm.cmblocal.currentText(),self.ppcm.txtCliente.text())
            fila=0
            saldo=0
            if data==[]:
                m=QMessageBox()
                m.setIcon(QMessageBox.Icon.Information)
                m.setWindowTitle("informacion cartera")
                m.setText("No hay informacion")
                m.exec()
                self.ppcm.cmblocal.setFocus()
            else:
                self.ppcm.tblCarteraCM.setRowCount(len(data))
                for item in data:
                    saldo += float(item[4])
                    self.ppcm.txtSaldo.setText(f"{saldo:,.2f}")
                    
                for item in data:
                    self.ppcm.tblCarteraCM.setItem(fila,0,QTableWidgetItem(item[0]))
                    self.ppcm.tblCarteraCM.setItem(fila,1,QTableWidgetItem(item[1]))
                    self.ppcm.tblCarteraCM.setItem(fila,2,QTableWidgetItem(str(item[2])))
                    self.ppcm.tblCarteraCM.setItem(fila,3,QTableWidgetItem(str(item[3])))
                    self.ppcm.tblCarteraCM.setItem(fila,4,QTableWidgetItem(str(item[4])))
                    self.ppcm.tblCarteraCM.setItem(fila,5,QTableWidgetItem(item[5]))
                    self.ppcm.tblCarteraCM.setItem(fila,6,QTableWidgetItem(item[6]))
                    self.ppcm.tblCarteraCM.setItem(fila,7,QTableWidgetItem(item[7]))
                    self.ppcm.tblCarteraCM.setItem(fila,8,QTableWidgetItem(item[8]))
                    self.ppcm.tblCarteraCM.setItem(fila,9,QTableWidgetItem(item[9]))
                    fila+=1
                    
    def exportar_info_a_excelCM(self):
        if self.ppcm.cmblocal.currentIndex()==0:
            m=QMessageBox()
            m.setIcon(QMessageBox.Icon.Warning)
            m.setWindowTitle("exportar informacion")
            m.setText("Seleccione una Opcion")
            m.exec()
        else:    
            if self.ppcm.tblCarteraCM.rowCount() > 0:
                file_dialog = QFileDialog()
                file_path, _ = file_dialog.getSaveFileName(self.pp, "Guardar archivo", "", "Archivos Excel (*.xlsx);;Todos los archivos (*)")
                                
                if file_path:
                    try:                            
                        workbook = xlsxwriter.Workbook(file_path)
                        worksheet = workbook.add_worksheet()                        
                        worksheet.write(0, 0, "ESTADO DE CUENTA")
                        worksheet.write(1, 0, "Numero de Local: " + self.ppcm.cmblocal.currentText())
                        worksheet.write(2, 0, "Cliente Facturacion: " + self.ppcm.txtCliente.text())
                        
                        headers = ["tipo_cuota", "num_fact", "importe_adeudo", "importe_pago", "importe_saldo", "fecha", "forma_pago", "num_cheque", "cta_banco","status"]
                        for col_num, header in enumerate(headers):
                            worksheet.write(4, col_num, header)           
                            for row_num in range(self.ppcm.tblCarteraCM.rowCount()):
                                for col_num in range(self.ppcm.tblCarteraCM.columnCount()):
                                    worksheet.write(row_num + 5, col_num, self.ppcm.tblCarteraCM.item(row_num, col_num).text())
                                        
                        workbook.close()               
                        m = QMessageBox()
                        m.setIcon(QMessageBox.Icon.Information)
                        m.setWindowTitle("Exportar a Excel")
                        m.setText("Datos exportados exitosamente a Excel")
                        m.exec()
                    except Exception as e:
                        m = QMessageBox()
                        m.setIcon(QMessageBox.Icon.Critical)
                        m.setWindowTitle("Error")
                        m.setText(f"Error al exportar a Excel: {e}")
                        m.exec()
            elif self.ppcm.tblCarteraCM.rowCount() < 0:
                m = QMessageBox()
                m.setIcon(QMessageBox.Icon.Warning)
                m.setWindowTitle("Exportar a Excel")
                m.setText("No hay datos para exportar")
                m.exec()
                
##############################TABLA DE INFORMACION AREAS COMUNES############################################        
    def mostrar_informacionAC(self):
        if self.ppac.cmbContrato.currentIndex()==0:
            m=QMessageBox()
            m.setIcon(QMessageBox.Icon.Information)
            m.setWindowTitle("informacion cartera")
            m.setText("Selecciona una Opcion")
            m.exec()
            self.ppac.cmbContrato.setFocus()
        else:    
            search=CarteraDataAC()
            data=search.buscar_info_area_x_contrato(self.ppac.cmbContrato.currentText())
            fila=0
            saldo=0
            if data==[]:
                m=QMessageBox()
                m.setWindowTitle("informacion cartera")
                m.setIcon(QMessageBox.Icon.Information)
                m.setText("No hay informacion")
                m.exec()
                self.ppac.tblCarteraAC.clearContents()
                self.ppac.cmbContrato.setFocus()
            else:
                self.ppac.tblCarteraAC.setRowCount(len(data))
                for item in data:
                    saldo += float(item[4])
                    self.ppac.txtSaldo.setText(f"{saldo:,.2f}")
                    
                for item in data:
                     self.ppac.tblCarteraAC.setItem(fila,0,QTableWidgetItem(item[0]))
                     self.ppac.tblCarteraAC.setItem(fila,1,QTableWidgetItem(item[1]))
                     self.ppac.tblCarteraAC.setItem(fila,2,QTableWidgetItem(str(item[2])))
                     self.ppac.tblCarteraAC.setItem(fila,3,QTableWidgetItem(str(item[3])))
                     self.ppac.tblCarteraAC.setItem(fila,4,QTableWidgetItem(str(item[4])))
                     self.ppac.tblCarteraAC.setItem(fila,5,QTableWidgetItem(item[5]))
                     self.ppac.tblCarteraAC.setItem(fila,6,QTableWidgetItem(item[6]))
                     self.ppac.tblCarteraAC.setItem(fila,7,QTableWidgetItem(item[7]))
                     self.ppac.tblCarteraAC.setItem(fila,8,QTableWidgetItem(item[8]))
                     self.ppac.tblCarteraAC.setItem(fila,9,QTableWidgetItem(item[9]))   
                     fila+=1

    def exportar_info_a_excelAC(self):
        if self.ppac.cmbContrato.currentIndex()==0:
            m=QMessageBox()
            m.setIcon(QMessageBox.Icon.Warning)
            m.setWindowTitle("exportar informacion")
            m.setText("Seleccione una Opcion")
            m.exec()
        else:    
            if self.ppac.tblCarteraAC.rowCount() > 0:    
                file_dialog = QFileDialog()
                file_path, _ = file_dialog.getSaveFileName(self.pp, "Guardar archivo", "", "Archivos Excel (*.xlsx);;Todos los archivos (*)")
                                
                if file_path:
                    try:                            
                        workbook = xlsxwriter.Workbook(file_path)
                        worksheet = workbook.add_worksheet()
                        worksheet.write(0, 0, "ESTADO DE CUENTA")
                        worksheet.write(1, 0, "Num.Area Comun: " + self.ppac.cmbAreaC.currentText())
                        worksheet.write(2, 0, "Num.Contrato: "+ self.ppac.cmbContrato.currentText())
                        worksheet.write(3, 0, "Cliente Facturacion: "+ self.ppac.txtCliente.text())
                                        
                        headers = ["contrato", "tipo_cuota","num_fact", "importe_adeudo", "importe_pago", "importe_saldo", "fecha", "forma_pago", "cta_banco","status"]
                        for col_num, header in enumerate(headers):
                            worksheet.write(5, col_num, header)           
                            for row_num in range(self.ppac.tblCarteraAC.rowCount()):
                                for col_num in range(self.ppac.tblCarteraAC.columnCount()):
                                    worksheet.write(row_num + 6, col_num, self.ppac.tblCarteraAC.item(row_num, col_num).text())                
                        workbook.close()               
                        m = QMessageBox()
                        m.setIcon(QMessageBox.Icon.Information)
                        m.setWindowTitle("Exportar a Excel")
                        m.setText("Datos exportados exitosamente a Excel")
                        m.exec()
                    except Exception as e:
                        m = QMessageBox()
                        m.setIcon(QMessageBox.Icon.Critical)
                        m.setWindowTitle("Error")
                        m.setText(f"Error al exportar a Excel: {e}")
                        m.exec()
                else: pass        
            elif self.ppac.tblCarteraAC.rowCount() < 0:    
                m = QMessageBox()
                m.setIcon(QMessageBox.Icon.Warning)
                m.setWindowTitle("Exportar a Excel")
                m.setText("No hay datos para exportar")
                m.exec()
                        
                
########################################CARGA MASIVA DE CUOTAS###########################################################
    def abrir_form_cmasiva(self):
        #self.ffm=uic.loadUi("gui/formFactMasiva.ui")
        #self.ffm = uic.loadUi(self.resource_path("C:/Users/smart/OneDrive/Escritorio/gac_py_V1.02/gui/formFactMasiva.ui"))
        self.ffm = uic.loadUi(self.resource_path("gui/formFactMasiva.ui"))
        self.ffm.setWindowTitle("Carga Mensual Facturas Cuotas")
        self.ffm.show()
        self.ffm.cmbTcartera.setCurrentIndex(0)
        self.ffm.btnEjecutar.clicked.connect(self.seleccion_tipo_cartera)
        self.ffm.btnSalir.clicked.connect(self.salir_form_cmasiva)
    
    def seleccion_tipo_cartera(self):
        m=QMessageBox()
        m.setIcon(QMessageBox.Icon.Information)
        m.setWindowTitle("Carga Mensual")
        if self.ffm.cmbTcartera.currentIndex()==0:
            m.setText("Selecciona una Opcion")
            m.exec()
            self.ffm.cmbTcartera.setFocus()
        elif self.ffm.fechaPeriodo.date().toString("yyyy-MM") < current_datetime.strftime("%Y-%m"):
            m.setText("Periodo menor al actual")
            m.exec()
            self.ffm.fechaPeriodo.setFocus()
        else:
            if self.ffm.cmbTcartera.currentIndex()==1 :
                self.registro_masivo_cuotas_locales()
                m.close()     
            elif self.ffm.cmbTcartera.currentIndex()==2 :
                self.registro_masivo_cuotas_areas()
                m.close()    
            else:
                m.setText("Selecciona una Opcion")
                m.exec()
                self.ffm.cmbTcartera.setFocus()
               
    def registro_masivo_cuotas_locales(self):
        m=QMessageBox()  
        m.setIcon(QMessageBox.Icon.Warning)
        m.setWindowTitle("Carga Cuotas Locales.")
        m.setText("¿¿Se generaran las cuotas?? \ncontinuar....")
        m.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        res=m.exec()
            
        if res==QMessageBox.StandardButton.Ok:
            search=UbicacionesData()
            data=search.lista_ubicaciones()     
            p=self.ffm.fechaPeriodo.date().toString("MMyy")
            if data==[]:
                m=QMessageBox()
                m.setWindowTitle("Carga Mensual")  
                m.setIcon(QMessageBox.Icon.Information)
                m.setText("sin informacion bd")
                m.exec()
            else:
                reg_Periodo=RegPeriodoFacturacion(
                    periodo=self.ffm.fechaPeriodo.date().toString("yyyy-MM-dd"),
                    tipoCartera=self.ffm.cmbTcartera.currentText(),
                    usuario=self.pp.lblName_User.text(),
                    fechaReg=current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                    )
                objData=PeriodosCargaData()
                if objData._registrar_p(info=reg_Periodo):
                    for item in data:
                        reg_facturas=Reg_Factura(
                            num_factura=f"F-{p}",
                            cliente=item[7],
                            local_o_area=item[1],
                            fecha_factura=self.ffm.fechaPeriodo.date().toString("yyyy-MM-dd"),
                            tipo_cuota="cuota ordinaria",
                            importe_factura=item[3],
                            tipo_factura="Ingreso",
                            tipo_cartera="locales comerciales",
                            status_pago=False,
                            usuario=self.pp.lblName_User.text(),
                            fecha_reg=current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                            )
                        objData=RegFacturaData()
                        objData._registrar(info=reg_facturas)
                        
                        reg_cartera=Reg_Cartera(
                            local_o_area=item[1],
                            clienteFact=item[7],
                            tipoCartera="locales comerciales",
                            tipoCuota="cuota ordinaria",
                            tipo_factura="Ingreso",
                            numFact=f"F-{p}",
                            importeAdeudo=item[3],
                            importePago=0,
                            fPago_Cobro=self.ffm.fechaPeriodo.date().toString("yyyy-MM-dd"),
                            ctaBanco="",
                            formaPago="",
                            cheque="",
                            numContrato="",
                            statusPago=False,
                            usuario=self.pp.lblName_User.text(),
                            fechaReg=current_datetime.strftime("%Y-%m-%d %H:%M:%S"),
                            comentarios="carga mensual " + self.ffm.fechaPeriodo.date().toString("yyyy-MM")         
                            )
                        objData=RegCarteraData()
                        objData._registrar(info=reg_cartera)
                         
                    m.setIcon(QMessageBox.Icon.Information)
                    m.setText("carga mensual de cuotas exitosa") 
                    m.exec()
                           
                else:
                    m.setIcon(QMessageBox.Icon.Information)
                    m.setText("Periodo ya registrado")
                    m.exec()    
                                        
        elif res==QMessageBox.StandardButton.Cancel:
            m.close()
                                   
    def registro_masivo_cuotas_areas(self):
        m=QMessageBox()  
        m.setIcon(QMessageBox.Icon.Warning)
        m.setWindowTitle("Carga Cuotas Areas C.")
        m.setText("¿¿Se generaran las facturas \npor cuotas areas comunes?? continuar....")
        m.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        res=m.exec()
            
        if res==QMessageBox.StandardButton.Ok:
            search=ContratosData()
            data=search.lista_contratos()
            p=self.ffm.fechaPeriodo.date().toString("MMyy")
            if data==[]:
                m=QMessageBox()
                m.setWindowTitle("Carga Mensual.")  
                m.setIcon(QMessageBox.Icon.Information)
                m.setText("sin informacion bd")
                m.exec()
            else:
                reg_Periodo=RegPeriodoFacturacion(
                    periodo=self.ffm.fechaPeriodo.date().toString("yyyy-MM-dd"),
                    tipoCartera=self.ffm.cmbTcartera.currentText(),
                    usuario=self.pp.lblName_User.text(),
                    fechaReg=current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                    )
                objData=PeriodosCargaData()
                if objData._registrar_p(info=reg_Periodo): 
                    for item in data:
                        reg_facturas=Reg_Factura(
                            num_factura=f"F-{p}",
                            cliente=item[2],
                            local_o_area=item[3],
                            fecha_factura=self.ffm.fechaPeriodo.date().toString("yyyy-MM-dd"),
                            tipo_cuota="cuota ordinaria",
                            importe_factura=item[6],
                            tipo_factura="Ingreso",
                            tipo_cartera="areas comunes",
                            status_pago=False,
                            usuario=self.pp.lblName_User.text(),
                            fecha_reg=current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                            )
                        objData=RegFacturaData()
                        objData._registrar(info=reg_facturas)
                        
                        reg_cartera=Reg_Cartera(
                            local_o_area=item[3],
                            clienteFact=item[2],
                            tipoCartera="areas comunes",
                            tipoCuota="cuota ordinaria",
                            tipo_factura="Ingreso",
                            numFact=f"F-{p}",
                            importeAdeudo=item[6],
                            importePago=0,
                            fPago_Cobro=self.ffm.fechaPeriodo.date().toString("yyyy-MM-dd"),
                            ctaBanco="",
                            formaPago="",
                            cheque="",
                            numContrato=item[1],  
                            statusPago=False,
                            usuario=self.pp.lblName_User.text(),
                            fechaReg=current_datetime.strftime("%Y-%m-%d %H:%M:%S"),
                            comentarios="Facturacion masiva " + self.ffm.fechaPeriodo.date().toString("yyyy-MM")         
                            )
                        objData=RegCarteraData()
                        objData._registrar(info=reg_cartera)
                        
                    m.setIcon(QMessageBox.Icon.Information)
                    m.setText("carga mensual de cuotas exitosa") 
                    m.exec()     
                          
                else:
                    m.setIcon(QMessageBox.Icon.Information)
                    m.setText("Periodo ya registrado")
                    m.exec()

        elif res==QMessageBox.StandardButton.Cancel:
            m.close()
              
    def salir_form_cmasiva(self):
        self.ffm.close() 
        
        
###################################################MODULO GASTOS#####################################################################
    def abrir_form_gastos(self):
        #self.fexp=uic.loadUi("gui/formRegGastos.ui")
        #self.fexp = uic.loadUi(self.resource_path("C:/Users/smart/OneDrive/Escritorio/gac_py_V1.02/gui/formRegGastos.ui"))
        self.fexp = uic.loadUi(self.resource_path("gui/formRegGastos.ui"))
        self.fexp.setWindowTitle("Registro Gastos Mensuales")
        self.fexp.show()
        self.fexp.txtIVA_ret.setText("0.00")
        self.fexp.txtISR_ret.setText("0.00")
        self.fexp.checkBoxEmpleados.setChecked(False)
        self.fexp.label_proveedor.setText("Proveedor")
        self.set_cmb_proveedor()
        self.fexp.checkBoxEmpleados.clicked.connect(self.check_empleados)
        self.fexp.btnRegistrar.clicked.connect(self.registrar_gasto)
        self.fexp.btnSalir.clicked.connect(self.salir_form_gastos)
         
    def set_cmb_empleados(self):
        search=ProveedoresData()
        data=search.lista_empleados()
        self.fexp.cmbProveedor.clear()
        self.fexp.cmbProveedor.addItem("---Seleccione una opción---")
        for item in data:
            self.fexp.cmbProveedor.addItem(f"{item[1]} {item[2]} {item[3]}")
    
    def set_cmb_proveedor(self):
        search=ProveedoresData()
        data=search.lista_proveedores()
        self.fexp.cmbProveedor.clear()
        self.fexp.cmbProveedor.addItem("---Seleccione una opción---")
        for item in data:
            self.fexp.cmbProveedor.addItem(item[1]) 
     
    def check_empleados(self):
        if self.fexp.checkBoxEmpleados.isChecked():
            self.fexp.label_proveedor.setText("Empleado")
            self.set_cmb_empleados()
        else:
            self.fexp.label_proveedor.setText("Proveedor")
            self.set_cmb_proveedor()

#########################################REGISTRO GASTOS############################################################               

    def registrar_gasto(self):
        m = QMessageBox()
        m.setIcon(QMessageBox.Icon.Information)
        m.setWindowTitle("Registro de Gasto")
        m.setStandardButtons(QMessageBox.StandardButton.Ok)

        if self.fexp.cmbProveedor.currentIndex() == 0:
            m.setText("Selecciona un proveedor")
            self.fexp.cmbProveedor.setFocus()
        elif self.fexp.txtImporte.text() == "":
            m.setText("Captura el importe del gasto")
            self.fexp.txtImporte.setFocus()
        elif not self.fexp.txtImporte.text().replace('.', '', 1).isnumeric():
            m.setText("Captura solo números en el importe")
            self.fexp.txtImporte.setText("")
            self.fexp.txtImporte.setFocus()
        elif self.fexp.txtDescripcion.toPlainText() == "":
            m.setText("Captura el concepto del gasto")
            self.fexp.txtDescripcion.setFocus()
        elif self.fexp.cmbFormaPago.currentIndex() == 0:
            m.setText("Selecciona una forma de pago")
            self.fexp.cmbFormaPago.setFocus()
        elif self.fexp.cmbTipoGasto.currentIndex() == 0:
            m.setText("Selecciona un tipo de gasto")
            self.fexp.cmbTipoGasto.setFocus()
        elif self.fexp.txtnFactura.text() == "":
            m.setText("Captura el número de factura")
            self.fexp.txtnFactura.setFocus()        
        else:
            regGasto = Reg_Gasto(
                num_fact=self.fexp.txtnFactura.text().upper(),
                n_proveedor=self.fexp.cmbProveedor.currentText(),
                t_gasto=self.fexp.cmbTipoGasto.currentText(),
                desc_gasto=self.fexp.txtDescripcion.toPlainText(),
                f_pago=self.fexp.cmbFormaPago.currentText(),
                n_cheque=self.fexp.txtn_cheque.text().upper(),
                i_pago=float(self.fexp.txtImporte.text()),
                iva_ret=float(self.fexp.txtIVA_ret.text()),
                isr_ret=float(self.fexp.txtISR_ret.text()),
                f_gasto=self.fexp.boxDate.date().toString("yyyy-MM-dd"),
                usuario=self.pp.lblName_User.text(),
                f_reg=current_datetime.strftime("%Y-%m-%d %H:%M:%S")
                )
            objData = RegGastoData()
            if objData._registrar(info=regGasto):
                m.setText("Gasto registrado con éxito")
                self.limpiar_campos_fexp()
            else:
                m.setText("Error al registrar el gasto")
                self.limpiar_campos_fexp()
        m.exec()

    def limpiar_campos_fexp(self):
        self.fexp.cmbProveedor.setCurrentIndex(0)
        self.fexp.txtnFactura.setText("")
        self.fexp.cmbTipoGasto.setCurrentIndex(0)
        self.fexp.txtDescripcion.setText("")
        self.fexp.cmbFormaPago.setCurrentIndex(0)
        self.fexp.txtn_cheque.setText("")
        self.fexp.txtImporte.setText("")
        self.fexp.txtIVA_ret.setText("")
        self.fexp.txtISR_ret.setText("")
    
    def salir_form_gastos(self):
        self.fexp.close()
 
                
###########################################REPORTE GASTOS#################################################################################
    def abrir_form_rep_gastos(self):
        self.frg=uic.loadUi(self.resource_path("gui/formReporteGastos.ui"))
        self.frg.setWindowTitle("Reporte de Gastos")
        self.frg.show()
        self.frg.btnBuscar.clicked.connect(self.open_form_search)
        self.frg.btnEliminar.clicked.connect(self.eliminar_registroG)
        self.frg.btnBajar_info.clicked.connect(self.exp_infoG_excel)
        self.frg.btnSalir.clicked.connect(self.salir_form_frg)
                                        
    def open_form_search(self):
        self.fsch=uic.loadUi(self.resource_path("gui/formEncontrar_Gtos.ui"))
        self.fsch.setWindowTitle("Opciones de Consulta")
        self.fsch.show()
        self.fsch.lblProv.setVisible(True)
        self.fsch.cmb_prov.setVisible(True)
        self.fsch.cmb_prov.setCurrentIndex(0)
        self.fsch.cmb_tipo_gtos.setCurrentIndex(0)
        self.fsch.cmb_empleados.setCurrentIndex(0)
        self.frg.txtTotal_g.setText("")
        self.frg.lbl_form_gtos.setText("Proveedor")
        self.frg.tblGastos.clearContents()
        self.fsch.radioButton_emp.clicked.connect(self.opciones_consultaG)
        self.fsch.radioButton_prov.clicked.connect(self.opciones_consultaG)
        self.fsch.radioButton_fechas.clicked.connect(self.opciones_consultaG)
        self.fsch.radioButton_tgasto.clicked.connect(self.opciones_consultaG)
        self.fsch.btnConsultar.clicked.connect(self.mostrar_infoG)
        self.fsch.btnSalir.clicked.connect(self.ex_form_fsch)
        
    def opciones_consultaG(self):
        #xProveedor
        if  self.fsch.radioButton_prov.isChecked():
            self.fsch.lblProv.setVisible(True)
            self.fsch.cmb_prov.setVisible(True)
            self.fsch.cmb_tipo_gtos.setVisible(False)
            self.fsch.lblTipo_Gtos.setVisible(False)
            self.fsch.lblFecha_inicial.setVisible(False)
            self.fsch.lclFecha_final.setVisible(False)
            self.fsch.dateEdit_fecha_ini.setVisible(False)
            self.fsch.dateEdit_fecha_fin.setVisible(False)
            self.fsch.cmb_empleados.setVisible(False)
            self.fsch.lblTrabajador.setVisible(False)
            self.fsch.groupBox_2.setTitle("Proveedor")
            self.list_prov()   
                     
        elif self.fsch.radioButton_tgasto.isChecked():
            self.fsch.cmb_tipo_gtos.setVisible(True)
            self.fsch.lblTipo_Gtos.setVisible(True)
            self.fsch.lblTipo_Gtos.setGeometry(270,150,71,16)
            self.fsch.cmb_tipo_gtos.setGeometry(270,170,291,30)    
            self.fsch.lblProv.setVisible(False)
            self.fsch.cmb_prov.setVisible(False)
            self.fsch.lblFecha_inicial.setVisible(False)
            self.fsch.lclFecha_final.setVisible(False)
            self.fsch.dateEdit_fecha_ini.setVisible(False)
            self.fsch.dateEdit_fecha_fin.setVisible(False)
            self.fsch.cmb_empleados.setVisible(False)
            self.fsch.lblTrabajador.setVisible(False)
            self.fsch.groupBox_2.setTitle("Tipo Gasto")            
            
        elif self.fsch.radioButton_fechas.isChecked():
             self.fsch.lblFecha_inicial.setVisible(True)
             self.fsch.lclFecha_final.setVisible(True)
             self.fsch.dateEdit_fecha_ini.setVisible(True)
             self.fsch.dateEdit_fecha_fin.setVisible(True)
             self.fsch.lblFecha_inicial.setGeometry(270,140,71,16)
             self.fsch.lclFecha_final.setGeometry(440,140,71,16)
             self.fsch.dateEdit_fecha_ini.setGeometry(270,160,110,30)
             self.fsch.dateEdit_fecha_fin.setGeometry(440,160,110,30)   
             self.fsch.lblProv.setVisible(False)
             self.fsch.cmb_prov.setVisible(False)
             self.fsch.cmb_tipo_gtos.setVisible(False)
             self.fsch.lblTipo_Gtos.setVisible(False)
             self.fsch.cmb_empleados.setVisible(False)
             self.fsch.lblTrabajador.setVisible(False)
             self.fsch.groupBox_2.setTitle("Fechas")
             
        elif self.fsch.radioButton_emp.isChecked():
            self.fsch.cmb_empleados.setVisible(True)
            self.fsch.lblTrabajador.setVisible(True)
            self.fsch.lblTrabajador.setGeometry(270,140,71,16)
            self.fsch.cmb_empleados.setGeometry(270,158,290,30)
            self.fsch.cmb_tipo_gtos.setVisible(False)
            self.fsch.lblTipo_Gtos.setVisible(False)
            self.fsch.lblProv.setVisible(False)
            self.fsch.cmb_prov.setVisible(False)
            self.fsch.lblFecha_inicial.setVisible(False)
            self.fsch.lclFecha_final.setVisible(False)
            self.fsch.dateEdit_fecha_ini.setVisible(False)
            self.fsch.dateEdit_fecha_fin.setVisible(False)
            self.fsch.groupBox_2.setTitle("Empleado")  
            self.list_empleados() 
              
    def list_prov(self):
        search=ProveedoresData()
        data= search.lista_proveedores()
        self.fsch.cmb_prov.clear()
        self.fsch.cmb_prov.addItem("---Seleccione una opción---")
        for item in data:
            self.fsch.cmb_prov.addItem(item[1])
    
    def list_empleados(self):
        search=ProveedoresData()
        data=search.lista_empleados()
        self.fsch.cmb_empleados.clear()
        self.fsch.cmb_empleados.addItem("---Seleccione una opción---")
        for item in data:
            self.fsch.cmb_empleados.addItem(f"{item[1]} {item[2]} {item[3]}")
            
    def mostrar_infoG(self):
        if self.fsch.radioButton_prov.isChecked():
            if self.fsch.cmb_prov.currentIndex()==0:
                m=QMessageBox()
                m.setIcon(QMessageBox.Icon.Information)
                m.setWindowTitle("Consultar Gastos")
                m.setText("Selecciona una Opcion")
                m.exec()
            else:
                search=GastosDataGral()
                data=search.get_infox_prov(self.fsch.cmb_prov.currentText())
                self.frg.tblGastos.setRowCount(len(data))
                fila=0
                saldo=0
                if data==[]:
                    m=QMessageBox()
                    m.setIcon(QMessageBox.Icon.Information)
                    m.setWindowTitle("Consultar x Proveedor")
                    m.setText("No hay informacion")
                    m.exec()
                    self.fsch.cmb_prov.setFocus()
                else:
                    for item in data:
                        saldo += float(item[6])
                        self.frg.txtTotal_g.setText(f"{saldo:,.2f}")
                        
                    for item in data:
                        self.frg.tblGastos.setItem(fila,0,QTableWidgetItem(str(item[0])))
                        self.frg.tblGastos.setItem(fila,1,QTableWidgetItem(item[1]))
                        self.frg.tblGastos.setItem(fila,2,QTableWidgetItem(item[2]))
                        self.frg.tblGastos.setItem(fila,3,QTableWidgetItem(item[3]))
                        self.frg.tblGastos.setItem(fila,4,QTableWidgetItem(item[4]))
                        self.frg.tblGastos.setItem(fila,5,QTableWidgetItem(item[5]))
                        self.frg.tblGastos.setItem(fila,6,QTableWidgetItem(str(item[6])))
                        self.frg.tblGastos.setItem(fila,7,QTableWidgetItem(item[7]))
                        self.frg.tblGastos.setItem(fila,8,QTableWidgetItem(str(item[8])))
                        self.frg.tblGastos.setItem(fila,9,QTableWidgetItem(str(item[9])))
                        fila+=1
                    self.frg.lbl_form_gtos.setText("Proveedor")        
                    self.frg.txt_form_gtos.setText(self.fsch.cmb_prov.currentText()) 
                    self.fsch.close()
                    
        elif self.fsch.radioButton_tgasto.isChecked():
            if self.fsch.cmb_tipo_gtos.currentIndex()==0:
                m=QMessageBox()
                m.setIcon(QMessageBox.Icon.Information)
                m.setWindowTitle("Consultar Gastos")
                m.setText("Selecciona una Opcion")
                m.exec()
            else:
                search=GastosDataGral()
                data=search.get_infox_tipoG(self.fsch.cmb_tipo_gtos.currentText())
                self.frg.tblGastos.setRowCount(len(data))
                fila=0
                saldo=0
                if data==[]:
                    m=QMessageBox()
                    m.setIcon(QMessageBox.Icon.Information)
                    m.setWindowTitle("Consultar x Tipo Gasto")
                    m.setText("No hay informacion")
                    m.exec()
                    self.fsch.cmb_tipo_gtos.setFocus()
                else:
                    for item in data:
                        saldo += float(item[6])
                        self.frg.txtTotal_g.setText(f"{saldo:,.2f}")
                        
                    for item in data:
                        self.frg.tblGastos.setItem(fila,0,QTableWidgetItem(str(item[0])))
                        self.frg.tblGastos.setItem(fila,1,QTableWidgetItem(item[1]))
                        self.frg.tblGastos.setItem(fila,2,QTableWidgetItem(item[2]))
                        self.frg.tblGastos.setItem(fila,3,QTableWidgetItem(item[3]))
                        self.frg.tblGastos.setItem(fila,4,QTableWidgetItem(item[4]))
                        self.frg.tblGastos.setItem(fila,5,QTableWidgetItem(item[5]))
                        self.frg.tblGastos.setItem(fila,6,QTableWidgetItem(str(item[6])))
                        self.frg.tblGastos.setItem(fila,7,QTableWidgetItem(item[7]))
                        self.frg.tblGastos.setItem(fila,8,QTableWidgetItem(str(item[8])))
                        self.frg.tblGastos.setItem(fila,9,QTableWidgetItem(str(item[9])))
                        fila+=1
                    self.frg.lbl_form_gtos.setText("Tipo Gasto")                
                    self.frg.txt_form_gtos.setText(self.fsch.cmb_tipo_gtos.currentText()) 
                    self.fsch.close()
                    
        elif self.fsch.radioButton_fechas.isChecked():
            fecha_Ini=self.fsch.dateEdit_fecha_ini.date().toString("yyyy-MM-dd")
            fecha_Fin=self.fsch.dateEdit_fecha_fin.date().toString("yyyy-MM-dd")
            
            if fecha_Ini > fecha_Fin or fecha_Fin < fecha_Ini:
                m=QMessageBox()
                m.setIcon(QMessageBox.Icon.Information)
                m.setWindowTitle("Consultar Gastos x Fechas")
                m.setText("Fechas incorrectas")
                m.exec()
            elif fecha_Ini == fecha_Fin:
                m=QMessageBox()
                m.setIcon(QMessageBox.Icon.Information)
                m.setWindowTitle("Consultar Gastos x Fechas")
                m.setText("Fechas iguales")
                m.exec()    
            else:
                search=GastosDataGral()
                data=search.get_info_xfechas(fecha_Ini,fecha_Fin)
                self.frg.tblGastos.setRowCount(len(data))
                fila=0
                saldo=0
                if data==[]:
                    m=QMessageBox()
                    m.setIcon(QMessageBox.Icon.Information)
                    m.setWindowTitle("Consultar Gastos x Fechas")
                    m.setText("No hay informacion")
                    m.exec()
                else:
                    for item in data:
                        saldo += float(item[6])
                        self.frg.txtTotal_g.setText(f"{saldo:,.2f}")
                        
                    for item in data:
                        self.frg.tblGastos.setItem(fila,0,QTableWidgetItem(str(item[0])))
                        self.frg.tblGastos.setItem(fila,1,QTableWidgetItem(item[1]))
                        self.frg.tblGastos.setItem(fila,2,QTableWidgetItem(item[2]))
                        self.frg.tblGastos.setItem(fila,3,QTableWidgetItem(item[3]))
                        self.frg.tblGastos.setItem(fila,4,QTableWidgetItem(item[4]))
                        self.frg.tblGastos.setItem(fila,5,QTableWidgetItem(item[5]))
                        self.frg.tblGastos.setItem(fila,6,QTableWidgetItem(str(item[6])))
                        self.frg.tblGastos.setItem(fila,7,QTableWidgetItem(item[7]))
                        self.frg.tblGastos.setItem(fila,8,QTableWidgetItem(str(item[8])))
                        self.frg.tblGastos.setItem(fila,9,QTableWidgetItem(str(item[9])))
                        fila+=1
                    self.frg.lbl_form_gtos.setText("Periodo")                
                    self.frg.txt_form_gtos.setText(f" entre:  {fecha_Ini} y {fecha_Fin}") 
                    self.fsch.close()
                                
        elif self.fsch.radioButton_emp.isChecked():
            if self.fsch.cmb_empleados.currentIndex()==0:
                m=QMessageBox()
                m.setIcon(QMessageBox.Icon.Information)
                m.setWindowTitle("Consultar Gastos")
                m.setText("Selecciona una Opcion")
                m.exec()
            else:
                search=GastosDataGral()
                data=search.get_infox_empleado(self.fsch.cmb_empleados.currentText())
                self.frg.tblGastos.setRowCount(len(data))
                fila=0
                saldo=0
                if data==[]:
                    m=QMessageBox()
                    m.setIcon(QMessageBox.Icon.Information)
                    m.setWindowTitle("Consultar x Empledo")
                    m.setText("No hay informacion")
                    m.exec()
                    self.fsch.cmb_empleados.setFocus()
                else:
                    
                    for item in data:
                        saldo += float(item[6])
                        self.frg.txtTotal_g.setText(f"{saldo:,.2f}")
                        
                    for item in data:
                        self.frg.tblGastos.setItem(fila,0,QTableWidgetItem(str(item[0])))
                        self.frg.tblGastos.setItem(fila,1,QTableWidgetItem(item[1]))
                        self.frg.tblGastos.setItem(fila,2,QTableWidgetItem(item[2]))
                        self.frg.tblGastos.setItem(fila,3,QTableWidgetItem(item[3]))
                        self.frg.tblGastos.setItem(fila,4,QTableWidgetItem(item[4]))
                        self.frg.tblGastos.setItem(fila,5,QTableWidgetItem(item[5]))
                        self.frg.tblGastos.setItem(fila,6,QTableWidgetItem(str(item[6])))
                        self.frg.tblGastos.setItem(fila,7,QTableWidgetItem(item[7]))
                        self.frg.tblGastos.setItem(fila,8,QTableWidgetItem(str(item[8])))
                        self.frg.tblGastos.setItem(fila,9,QTableWidgetItem(str(item[9])))
                        fila+=1
                    self.frg.lbl_form_gtos.setText("Empleado")                
                    self.frg.txt_form_gtos.setText(self.fsch.cmb_empleados.currentText()) 
                    self.fsch.close()
        else:
            m=QMessageBox()
            m.setIcon(QMessageBox.Icon.Information)
            m.setWindowTitle("Consulta Gastos")
            m.setText("Selecciona una opcion de busqueda")
            m.exec()

    def eliminar_registroG(self):
        selected_row = self.frg.tblGastos.currentRow()
        if selected_row == -1:
            m = QMessageBox()
            m.setIcon(QMessageBox.Icon.Warning)
            m.setWindowTitle("Eliminar Registro")
            m.setText("Seleccione un registro para eliminar")
            m.exec()
            return

        id_registro = self.frg.tblGastos.item(selected_row, 0).text()
        m = QMessageBox()
        m.setIcon(QMessageBox.Icon.Warning)
        m.setWindowTitle("Eliminar Registro")
        m.setText(f"¿Está seguro de que desea eliminar \nel registro con ID: {id_registro}?")
        m.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        response = m.exec()

        if response == QMessageBox.StandardButton.Yes:
            objData = GastosDataGral()
            if objData.eliminar_regx_id(id_registro):
                self.frg.tblGastos.removeRow(selected_row)
                m = QMessageBox()
                m.setIcon(QMessageBox.Icon.Information)
                m.setWindowTitle("Eliminar Registro")
                m.setText("Registro eliminado con éxito")
                m.exec()
                self.frg.tblGastos.clearContents()
                self.frg.txt_form_gtos.setText("")
                self.frg.txtTotal_g.setText("")
            else:
                m = QMessageBox()
                m.setIcon(QMessageBox.Icon.Critical)
                m.setWindowTitle("Eliminar Registro")
                m.setText("Error al eliminar el registro")
                m.exec()

    def exp_infoG_excel(self):
        if self.frg.tblGastos.rowCount() > 0:
            file_dialog = QFileDialog()
            file_path, _ = file_dialog.getSaveFileName(self.frg, "Guardar archivo", "", "Archivos Excel (*.xlsx);;Todos los archivos (*)")
            
            if file_path:
                try:
                    workbook = xlsxwriter.Workbook(file_path)
                    worksheet = workbook.add_worksheet()
                    worksheet.write(0, 0, "INFORMACION GASTOS (EGRESOS)")
                    worksheet.write(1, 0, "CONCEPTO: " + self.frg.txt_form_gtos.text())
                    worksheet.write(2, 0, "Total: " + self.frg.txtTotal_g.text())
                    
                    headers = ["ID", "Factura/Recibo","Prov/Emp", "Tipo Gasto","Concepto", "Forma Pago", "Importe Pago", "Fecha","IVA ret","ISR ret"]
                    for col_num, header in enumerate(headers):
                        worksheet.write(4, col_num, header)
                        for row_num in range(self.frg.tblGastos.rowCount()):
                            for col_num in range(self.frg.tblGastos.columnCount()):
                                worksheet.write(row_num + 5, col_num, self.frg.tblGastos.item(row_num, col_num).text())
                    
                    workbook.close()
                    
                    m = QMessageBox()
                    m.setIcon(QMessageBox.Icon.Information)
                    m.setWindowTitle("Exportar a Excel")
                    m.setText("Datos exportados exitosamente a Excel")
                    m.exec()
                except Exception as e:
                    m = QMessageBox()
                    m.setIcon(QMessageBox.Icon.Critical)
                    m.setWindowTitle("Error")
                    m.setText(f"Error al exportar a Excel: {e}")
                    m.exec()
        else:
            m = QMessageBox()
            m.setIcon(QMessageBox.Icon.Warning)
            m.setWindowTitle("Exportar a Excel")
            m.setText("No hay datos para exportar")
            m.exec()
    
    def ex_form_fsch(self):
        self.fsch.close()    
        
    def salir_form_frg(self):
        self.frg.close()

#########################################REPORTE INGRESOS############################################################
    def abrir_form_reporte_ingresos(self):
        self.frexp=uic.loadUi(self.resource_path("gui/formReporteIngresos.ui"))
        self.frexp.setWindowTitle("Reporte de Ingresos")
        self.frexp.show()
        self.frexp.btnBuscar.clicked.connect(self.abrir_form_consultar)
        self.frexp.btnEliminar.clicked.connect(self.eliminar_registroI)
        self.frexp.btnBajar_info.clicked.connect(self.exp_infoI_excel)
        self.frexp.btnSalir.clicked.connect(self.salir_form_reporte_ingresos)
               
    def salir_form_reporte_ingresos(self):
        self.frexp.close()    
    
    def abrir_form_consultar(self):
        self.fcon=uic.loadUi(self.resource_path("gui/formEncontrar_ing.ui"))
        self.fcon.setWindowTitle("Opciones de Consulta")
        self.fcon.show()
        self.fcon.lblCliente.setVisible(True)
        self.fcon.cmbCliente.setVisible(True)
        self.fcon.cmbCliente.setCurrentIndex(0)
        self.fcon.cmb_tipo_ing.setCurrentIndex(0)
        self.frexp.txt_form_flujo.setText("")
        self.frexp.txtTotal.setText("") 
        self.frexp.lbl_form_flujo.setText("Cliente") 
        self.frexp.tblIngresos.clearContents()  
        self.fcon.radioButton_tipo_ing.clicked.connect(self.opciones_consultaI)
        self.fcon.radioButton_cliente.clicked.connect(self.opciones_consultaI)
        self.fcon.radioButton_fechas.clicked.connect(self.opciones_consultaI)
        self.fcon.radioButton_tipo_cartera.clicked.connect(self.opciones_consultaI)
        self.fcon.btnConsultar.clicked.connect(self.mostrar_infoI)   
        self.fcon.btnSalir.clicked.connect(self.salir_form_consultar)
        
    def opciones_consultaI(self):
        #xcliente
        if  self.fcon.radioButton_cliente.isChecked():
            self.fcon.cmbCliente.setCurrentIndex(0)
            self.fcon.lblCliente.setVisible(True)
            self.fcon.cmbCliente.setVisible(True)
            self.fcon.cmb_tipo_ing.setVisible(False)
            self.fcon.lblTipo_ingreso.setVisible(False)
            self.fcon.lblFecha_inicial.setVisible(False)
            self.fcon.lclFecha_final.setVisible(False)
            self.fcon.dateEdit_fecha_ini.setVisible(False)
            self.fcon.dateEdit_fecha_fin.setVisible(False)
            self.fcon.cmb_tipo_cartera.setVisible(False)
            self.fcon.lblTipo_cartera.setVisible(False)
            self.fcon.groupBox_2.setTitle("Cliente")
            self.list_cmb_clientes()   
                     
        elif self.fcon.radioButton_tipo_ing.isChecked():
            self.fcon.cmb_tipo_ing.setCurrentIndex(0)
            self.fcon.cmb_tipo_ing.setVisible(True)
            self.fcon.lblTipo_ingreso.setVisible(True)
            self.fcon.lblTipo_ingreso.setGeometry(270,150,71,16)
            self.fcon.cmb_tipo_ing.setGeometry(270,170,291,30)    
            self.fcon.lblCliente.setVisible(False)
            self.fcon.cmbCliente.setVisible(False)
            self.fcon.lblFecha_inicial.setVisible(False)
            self.fcon.lclFecha_final.setVisible(False)
            self.fcon.dateEdit_fecha_ini.setVisible(False)
            self.fcon.dateEdit_fecha_fin.setVisible(False)
            self.fcon.cmb_tipo_cartera.setVisible(False)
            self.fcon.lblTipo_cartera.setVisible(False)
            self.fcon.groupBox_2.setTitle("Tipo Pago")            
            
        elif self.fcon.radioButton_fechas.isChecked():
             self.fcon.lblFecha_inicial.setVisible(True)
             self.fcon.lclFecha_final.setVisible(True)
             self.fcon.dateEdit_fecha_ini.setVisible(True)
             self.fcon.dateEdit_fecha_fin.setVisible(True)
             self.fcon.lblFecha_inicial.setGeometry(270,140,71,16)
             self.fcon.lclFecha_final.setGeometry(440,140,71,16)
             self.fcon.dateEdit_fecha_ini.setGeometry(270,160,110,30)
             self.fcon.dateEdit_fecha_fin.setGeometry(440,160,110,30)   
             self.fcon.lblCliente.setVisible(False)
             self.fcon.cmbCliente.setVisible(False)
             self.fcon.cmb_tipo_ing.setVisible(False)
             self.fcon.lblTipo_ingreso.setVisible(False)
             self.fcon.cmb_tipo_cartera.setVisible(False)
             self.fcon.lblTipo_cartera.setVisible(False)
             self.fcon.groupBox_2.setTitle("Fechas")
             
        elif self.fcon.radioButton_tipo_cartera.isChecked():
            self.fcon.cmb_tipo_cartera.setCurrentIndex(0)
            self.fcon.cmb_tipo_cartera.setVisible(True)
            self.fcon.lblTipo_cartera.setVisible(True)
            self.fcon.lblTipo_cartera.setGeometry(270,140,71,16)
            self.fcon.cmb_tipo_cartera.setGeometry(270,158,290,30)
            self.fcon.cmb_tipo_ing.setVisible(False)
            self.fcon.lblTipo_ingreso.setVisible(False)
            self.fcon.lblCliente.setVisible(False)
            self.fcon.cmbCliente.setVisible(False)
            self.fcon.lblFecha_inicial.setVisible(False)
            self.fcon.lclFecha_final.setVisible(False)
            self.fcon.dateEdit_fecha_ini.setVisible(False)
            self.fcon.dateEdit_fecha_fin.setVisible(False)
            self.fcon.groupBox_2.setTitle("Tipo Cartera")                 
           
    def list_cmb_clientes(self):    
        search=ClientesData()
        data=search.lista_clientes()
        self.fcon.cmbCliente.clear()
        self.fcon.cmbCliente.addItem("---Selecciona una opcion---")
        for item in data:
            self.fcon.cmbCliente.addItem(item[1])
        
    def mostrar_infoI(self):
        if self.fcon.radioButton_cliente.isChecked():
            if self.fcon.cmbCliente.currentIndex()==0:
                m=QMessageBox()
                m.setIcon(QMessageBox.Icon.Information)
                m.setWindowTitle("Consultar Ingresos")
                m.setText("Selecciona una Opcion")
                m.exec()
            else:
                search=CarteraDataGral()
                data=search.get_info_xcliente(self.fcon.cmbCliente.currentText(),'pago')
                self.frexp.tblIngresos.setRowCount(len(data))
                fila=0
                saldo=0
                if data==[]:
                    m=QMessageBox()
                    m.setIcon(QMessageBox.Icon.Information)
                    m.setWindowTitle("informacion flujo efectivo")
                    m.setText("No hay informacion")
                    m.exec()
                    self.fcon.cmbCliente.setFocus()
                else:
                    for item in data:
                        saldo += float(item[6])
                        self.frexp.txtTotal.setText(f"{saldo:,.2f}")
                        
                    for item in data:
                        self.frexp.tblIngresos.setItem(fila,0,QTableWidgetItem(str(item[0])))
                        self.frexp.tblIngresos.setItem(fila,1,QTableWidgetItem(item[1]))
                        self.frexp.tblIngresos.setItem(fila,2,QTableWidgetItem(item[2]))
                        self.frexp.tblIngresos.setItem(fila,3,QTableWidgetItem(item[3]))
                        self.frexp.tblIngresos.setItem(fila,4,QTableWidgetItem(item[4]))
                        self.frexp.tblIngresos.setItem(fila,5,QTableWidgetItem(item[5]))
                        self.frexp.tblIngresos.setItem(fila,6,QTableWidgetItem(str(item[6])))
                        self.frexp.tblIngresos.setItem(fila,7,QTableWidgetItem(item[7]))
                        fila+=1
                    self.frexp.lbl_form_flujo.setText("Cliente")        
                    self.frexp.txt_form_flujo.setText(self.fcon.cmbCliente.currentText()) 
                    self.fcon.close()
                    
        elif self.fcon.radioButton_tipo_ing.isChecked():
            if self.fcon.cmb_tipo_ing.currentIndex()==0:
                m=QMessageBox()
                m.setIcon(QMessageBox.Icon.Information)
                m.setWindowTitle("Consultar Ingresos")
                m.setText("Selecciona una Opcion")
                m.exec()
            else:
                search=CarteraDataGral()
                data=search.get_info_xtipo(self.fcon.cmb_tipo_ing.currentText())
                self.frexp.tblIngresos.setRowCount(len(data))
                fila=0
                saldo=0
                if data==[]:
                    m=QMessageBox()
                    m.setIcon(QMessageBox.Icon.Information)
                    m.setWindowTitle("informacion flujo efectivo")
                    m.setText("No hay informacion")
                    m.exec()
                    self.fcon.cmb_tipo_ing.setFocus()
                else:
                    for item in data:
                        saldo += float(item[6])
                        self.frexp.txtTotal.setText(f"{saldo:,.2f}")
                        
                    for item in data:
                        self.frexp.tblIngresos.setItem(fila,0,QTableWidgetItem(str(item[0])))
                        self.frexp.tblIngresos.setItem(fila,1,QTableWidgetItem(item[1]))
                        self.frexp.tblIngresos.setItem(fila,2,QTableWidgetItem(item[2]))
                        self.frexp.tblIngresos.setItem(fila,3,QTableWidgetItem(item[3]))
                        self.frexp.tblIngresos.setItem(fila,4,QTableWidgetItem(item[4]))
                        self.frexp.tblIngresos.setItem(fila,5,QTableWidgetItem(item[5]))
                        self.frexp.tblIngresos.setItem(fila,6,QTableWidgetItem(str(item[6])))
                        self.frexp.tblIngresos.setItem(fila,7,QTableWidgetItem(item[7]))
                        fila+=1
                    self.frexp.lbl_form_flujo.setText("Tipo Pago")                
                    self.frexp.txt_form_flujo.setText(self.fcon.cmb_tipo_ing.currentText()) 
                    self.fcon.close()
                    
        elif self.fcon.radioButton_fechas.isChecked():
            fecha_Ini=self.fcon.dateEdit_fecha_ini.date().toString("yyyy-MM-dd")
            fecha_Fin=self.fcon.dateEdit_fecha_fin.date().toString("yyyy-MM-dd")
            
            
            if fecha_Ini > fecha_Fin or fecha_Fin < fecha_Ini:
                m=QMessageBox()
                m.setIcon(QMessageBox.Icon.Information)
                m.setWindowTitle("Consultar Ingresos")
                m.setText("Fechas incorrectas")
                m.exec()
            elif fecha_Ini == fecha_Fin:
                m=QMessageBox()
                m.setIcon(QMessageBox.Icon.Information)
                m.setWindowTitle("Consultar Ingresos")
                m.setText("Fechas iguales")
                m.exec()    
            else:
                search=CarteraDataGral()
                data=search.get_info_xfechas('pago',fecha_Ini,fecha_Fin)
                self.frexp.tblIngresos.setRowCount(len(data))
                fila=0
                saldo=0
                if data==[]:
                    m=QMessageBox()
                    m.setIcon(QMessageBox.Icon.Information)
                    m.setWindowTitle("informacion flujo efectivo")
                    m.setText("No hay informacion")
                    m.exec()
                else:
                    for item in data:
                        saldo += float(item[6])
                        self.frexp.txtTotal.setText(f"{saldo:,.2f}")
                        
                    for item in data:
                        self.frexp.tblIngresos.setItem(fila,0,QTableWidgetItem(str(item[0])))
                        self.frexp.tblIngresos.setItem(fila,1,QTableWidgetItem(item[1]))
                        self.frexp.tblIngresos.setItem(fila,2,QTableWidgetItem(item[2]))
                        self.frexp.tblIngresos.setItem(fila,3,QTableWidgetItem(item[3]))
                        self.frexp.tblIngresos.setItem(fila,4,QTableWidgetItem(item[4]))
                        self.frexp.tblIngresos.setItem(fila,5,QTableWidgetItem(item[5]))
                        self.frexp.tblIngresos.setItem(fila,6,QTableWidgetItem(str(item[6])))
                        self.frexp.tblIngresos.setItem(fila,7,QTableWidgetItem(item[7]))
                        fila+=1
                    self.frexp.lbl_form_flujo.setText("Fechas")                
                    self.frexp.txt_form_flujo.setText(f" entre {fecha_Ini} y {fecha_Fin}") 
                    self.fcon.close()
                                
        elif self.fcon.radioButton_tipo_cartera.isChecked():
            if self.fcon.cmb_tipo_cartera.currentIndex()==0:
                m=QMessageBox()
                m.setIcon(QMessageBox.Icon.Information)
                m.setWindowTitle("Consultar Ingresos")
                m.setText("Selecciona una Opcion")
                m.exec()
            else:
                search=CarteraDataGral()
                data=search.get_info_xtipo_cartera('pago',self.fcon.cmb_tipo_cartera.currentText())
                self.frexp.tblIngresos.setRowCount(len(data))
                fila=0
                saldo=0
                if data==[]:
                    m=QMessageBox()
                    m.setIcon(QMessageBox.Icon.Information)
                    m.setWindowTitle("informacion flujo efectivo")
                    m.setText("No hay informacion")
                    m.exec()
                    self.fcon.cmb_tipo_cartera.setFocus()
                else:
                    
                    for item in data:
                        saldo += float(item[6])
                        self.frexp.txtTotal.setText(f"{saldo:,.2f}")
                        
                    for item in data:
                        self.frexp.tblIngresos.setItem(fila,0,QTableWidgetItem(str(item[0])))
                        self.frexp.tblIngresos.setItem(fila,1,QTableWidgetItem(item[1]))
                        self.frexp.tblIngresos.setItem(fila,2,QTableWidgetItem(item[2]))
                        self.frexp.tblIngresos.setItem(fila,3,QTableWidgetItem(item[3]))
                        self.frexp.tblIngresos.setItem(fila,4,QTableWidgetItem(item[4]))
                        self.frexp.tblIngresos.setItem(fila,5,QTableWidgetItem(item[5]))
                        self.frexp.tblIngresos.setItem(fila,6,QTableWidgetItem(str(item[6])))
                        self.frexp.tblIngresos.setItem(fila,7,QTableWidgetItem(item[7]))
                        fila+=1
                    self.frexp.lbl_form_flujo.setText("Tipo Cartera")                
                    self.frexp.txt_form_flujo.setText(self.fcon.cmb_tipo_cartera.currentText()) 
                    self.fcon.close()                             
        else:
            m=QMessageBox()
            m.setIcon(QMessageBox.Icon.Information)
            m.setWindowTitle("informacion Ingresos")
            m.setText("Selecciona una opcion de busqueda")
            m.exec()
                       
    def eliminar_registroI(self):
        selected_row = self.frexp.tblIngresos.currentRow()
        if selected_row == -1:
            m = QMessageBox()
            m.setIcon(QMessageBox.Icon.Warning)
            m.setWindowTitle("Eliminar Registro")
            m.setText("Seleccione un registro para eliminar")
            m.exec()
            return

        id_registro = self.frexp.tblIngresos.item(selected_row, 0).text()
        m = QMessageBox()
        m.setIcon(QMessageBox.Icon.Warning)
        m.setWindowTitle("Eliminar Registro")
        m.setText(f"¿Está seguro de que desea eliminar el registro con factura {id_registro}?")
        m.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        response = m.exec()

        if response == QMessageBox.StandardButton.Yes:
            objData = CarteraDataGral()
            if objData.eliminar_regx_id(id_registro):
                self.frexp.tblIngresos.removeRow(selected_row)
                m = QMessageBox()
                m.setIcon(QMessageBox.Icon.Information)
                m.setWindowTitle("Eliminar Registro")
                m.setText("Registro eliminado con éxito")
                m.exec()
                self.frexp.tblIngresos.clearContents()
                self.frexp.txt_form_flujo.setText("")
                self.frexp.txtTotal.setText("")
            else:
                m = QMessageBox()
                m.setIcon(QMessageBox.Icon.Critical)
                m.setWindowTitle("Eliminar Registro")
                m.setText("Error al eliminar el registro")
                m.exec()
    
    def exp_infoI_excel(self):
        if self.frexp.tblIngresos.rowCount() > 0:
            file_dialog = QFileDialog()
            file_path, _ = file_dialog.getSaveFileName(self.frexp, "Guardar archivo", "", "Archivos Excel (*.xlsx);;Todos los archivos (*)")
            
            if file_path:
                try:
                    workbook = xlsxwriter.Workbook(file_path)
                    worksheet = workbook.add_worksheet()
                    worksheet.write(0, 0, "INFORMACION INGRESOS (FLUJO EFECTIVO)")
                    worksheet.write(1, 0, "CONCEPTO: " + self.frexp.txt_form_flujo.text())
                    worksheet.write(2, 0, "Total: " + self.frexp.txtTotal.text())
                    
                    headers = ["ID", "Tipo Cartera", "Tipo Pago","Factura", "Forma Pago","Cuenta Deposito", "Importe Pago", "Fecha"]
                    for col_num, header in enumerate(headers):
                        worksheet.write(4, col_num, header)
                        for row_num in range(self.frexp.tblIngresos.rowCount()):
                            for col_num in range(self.frexp.tblIngresos.columnCount()):
                                worksheet.write(row_num + 5, col_num, self.frexp.tblIngresos.item(row_num, col_num).text())
                    
                    workbook.close()
                    
                    m = QMessageBox()
                    m.setIcon(QMessageBox.Icon.Information)
                    m.setWindowTitle("Exportar a Excel")
                    m.setText("Datos exportados exitosamente a Excel")
                    m.exec()
                except Exception as e:
                    m = QMessageBox()
                    m.setIcon(QMessageBox.Icon.Critical)
                    m.setWindowTitle("Error")
                    m.setText(f"Error al exportar a Excel: {e}")
                    m.exec()
        else:
            m = QMessageBox()
            m.setIcon(QMessageBox.Icon.Warning)
            m.setWindowTitle("Exportar a Excel")
            m.setText("No hay datos para exportar")
            m.exec()
              
    def salir_form_consultar(self):    
        self.fcon.close() 

##############################################REGISTRO OTROS INGRESOS###########################################################        

    def form_reg_Ogtos(self):
        self.froig=uic.loadUi(self.resource_path("gui/formRegOIng.ui"))
        self.froig.setWindowTitle("Registro otros Ingresos")
        self.froig.show()
        self.set_cmb_ctaD()
        self.froig.btnRegistrar.clicked.connect(self.registrar_Oingresos)
        self.froig.btnSalir.clicked.connect(self.salir_form_froig)
    
    def set_cmb_ctaD(self):
        obj=ctasbancos.CuentasData()
        datos=obj.lista_ctas()
        for item in datos:
            self.froig.cmb_cuenta.addItem(item[2])          
       
    def registrar_Oingresos(self):
        m = QMessageBox()
        m.setIcon(QMessageBox.Icon.Information)
        m.setWindowTitle("Registro Otros Ingresos")
        m.setStandardButtons(QMessageBox.StandardButton.Ok)

        if self.froig.txt_razon_soc.text() == "":
            m.setText("Captura el nombre del cliente")
            self.froig.txt_razon_soc.setFocus()
        elif self.froig.txt_doc.text() == "":
            m.setText("Captura el documento del ingreso")
            self.froig.txt_doc.setFocus()
        elif self.froig.cmb_tIng.currentIndex()==0:
            m.setText("Selecciona el tipo de ingreso")
            self.froig.cmb_tIng.setFocus()
        elif self.froig.txtDescripcion.toPlainText() == "":
            m.setText("Captura la descripción del ingreso")
            self.froig.txtDescripcion.setFocus()
        elif self.froig.txtImporte.text() == "":
            m.setText("Captura el importe del ingreso")
            self.froig.txtImporte.setFocus()
        elif not self.froig.txtImporte.text().replace('.', '', 1).isnumeric():
            m.setText("Captura solo números en el importe")
            self.froig.txtImporte.setText("")
            self.froig.txtImporte.setFocus()
        elif self.froig.cmb_fpago.currentIndex() == 0:
            m.setText("Selecciona una forma de pago")
            self.froig.cmb_fpago.setFocus()
        elif self.froig.cmb_cuenta.currentIndex() == 0:
            m.setText("Selecciona una cuenta bancaria")
            self.froig.cmb_cuenta.setFocus()
        else:
            regIngreso = Reg_Cartera(
                local_o_area="",
                clienteFact=self.froig.txt_razon_soc.text().upper(),
                tipoCartera="otros ingresos",
                tipoCuota=self.froig.cmb_tIng.currentText(),
                tipo_factura="pago",
                numFact=self.froig.txt_doc.text().upper(),
                importeAdeudo=0,
                importePago=float(self.froig.txtImporte.text()),
                fPago_Cobro=self.froig.boxDate.date().toString("yyyy-MM-dd"),
                ctaBanco=self.froig.cmb_cuenta.currentText(),
                formaPago=self.froig.cmb_fpago.currentText(),
                cheque="",
                numContrato="",
                statusPago="",
                usuario=self.pp.lblName_User.text(),
                fechaReg=current_datetime.strftime("%Y-%m-%d %H:%M:%S"),
                comentarios=self.froig.txtDescripcion.toPlainText()
            )
            objData = RegCarteraData()
            if objData._registrar(info=regIngreso):
                m.setText("Ingreso registrado con éxito")
                self.limpiar_campos_froig()
            else:
                m.setText("Error al registrar el ingreso")
                self.limpiar_campos_froig()
        m.exec()

    def limpiar_campos_froig(self):
        self.froig.txtDescripcion.setText("")
        self.froig.txtImporte.setText("")
        self.froig.cmb_fpago.setCurrentIndex(0)
        self.froig.cmb_cuenta.setCurrentIndex(0)
        self.froig.txt_razon_soc.setText("")
        self.froig.cmb_tIng.setCurrentIndex(0)
        self.froig.txt_doc.setText("")
                    
    def salir_form_froig(self):    
        self.froig.close()
        
########################################ALTA PROVEEDOR/PRESTADOR SERVICIOS##########################################
    def abrir_form_alta_proveedor(self):
        #self.fprov = uic.loadUi(self.resource_path("C:/Users/smart/OneDrive/Escritorio/gac_py_V1.02/gui/formRegProveedor.ui"))
        self.fprov = uic.loadUi(self.resource_path("gui/formRegProveedor.ui"))
        self.fprov.setWindowTitle("Registro de Proveedor")
        self.fprov.show()
        self.fprov.btnRegistrar.clicked.connect(self.registrar_proveedor)
        self.fprov.btnSalir.clicked.connect(self.salir_form_proveedores)
        
    def registrar_proveedor(self):
        m = QMessageBox()
        m.setIcon(QMessageBox.Icon.Information)
        m.setWindowTitle("Registro Proveedor")
        m.setStandardButtons(QMessageBox.StandardButton.Ok)

        if self.fprov.txtRazon_social.text() == "":
            m.setText("Captura nombre del proveedor")
            self.fprov.txtRazon_social.setFocus()
        elif self.fprov.txtRFC.text() == "":
            m.setText("Captura RFC del proveedor")
            self.fprov.txtRFC.setFocus()
        elif self.fprov.txtTipoServicio.text() == "":
            m.setText("Captura  tipo de servicio")
            self.fprov.txtTipoServicio.setFocus()
        elif self.fprov.txtBanco.text()=="":
            m.setText("Captura banco")
            self.fprov.txtBanco.setFocus()            
        elif self.fprov.txtDireccion.text() == "":
            m.setText("Captura dirección del proveedor")
            self.fprov.txtDireccion.setFocus()
        elif self.fprov.txtTelefono.text() == "":
            m.setText("Captura teléfono del proveedor")
            self.fprov.txtTelefono.setFocus()
        elif not self.fprov.txtTelefono.text().isnumeric():
            m.setText("Captura solo números en el teléfono")
            self.fprov.txtTelefono.setText("")
            self.fprov.txtTelefono.setFocus()
        elif len(self.fprov.txtTelefono.text()) < 10:
            m.setText("Captura un teléfono válido")
            self.fprov.txtTelefono.setText("55")
            self.fprov.txtTelefono.setFocus()    
        elif self.fprov.txtEmail.text() == "":
            m.setText("Captura email del proveedor")
            self.fprov.txtEmail.setFocus()
        elif "@" not in self.fprov.txtEmail.text() or "." not in self.fprov.txtEmail.text():
            m.setText("Captura un email válido")
            self.fprov.txtEmail.setFocus()
        else:
            regProveedor = RegProveedor(
                nombre=self.fprov.txtRazon_social.text().upper(),
                rfc=self.fprov.txtRFC.text().upper(),
                nComercial=self.fprov.txtNombre_comercial.text().upper(),
                curp=self.fprov.txtCURP.text().upper(),
                tipoServicio=self.fprov.txtTipoServicio.text(),
                cuentaBanco=self.fprov.txtBanco.text().upper(),
                direccion=self.fprov.txtDireccion.text(),
                telefono=self.fprov.txtTelefono.text(),
                email=self.fprov.txtEmail.text().lower(),
                usuario=self.pp.lblName_User.text(),
                fReg=current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            )
            objData = ProveedoresData()
            if objData.registrar_proveedor(regProveedor):
                m.setText("Proveedor registrado con éxito")
                self.limpiar_campos_fprov()
            else:
                m.setText("Proveedor ya registrado")
                self.limpiar_campos_fprov()
        m.exec()

    def limpiar_campos_fprov(self):
        self.fprov.txtRazon_social.setText("")
        self.fprov.txtRFC.setText("")
        self.fprov.txtNombre_comercial.setText("")
        self.fprov.txtCURP.setText("")
        self.fprov.txtDireccion.setText("")
        self.fprov.txtTelefono.setText("")
        self.fprov.txtEmail.setText("")
        self.fprov.txtTipoServicio.setText("")
        self.fprov.txtBanco.setText("")
    
    def salir_form_proveedores(self):
        self.fprov.close()       

######################################ALTA EMPLEADOS######################################################
    def abrir_form_alta_empleado(self):
        #self.femp = uic.loadUi(self.resource_path("C:/Users/smart/OneDrive/Escritorio/gac_py_V1.02/gui/formEmpleados.ui"))
        self.femp = uic.loadUi(self.resource_path("gui/formEmpleados.ui"))
        self.femp.setWindowTitle("Registro Empleados")
        self.femp.show()
        self.femp.btnGuardar.clicked.connect(self.registrar_empleado)
        self.femp.btnSalir.clicked.connect(self.salir_form_empleados)
          
    def registrar_empleado(self):   
        m = QMessageBox()
        m.setIcon(QMessageBox.Icon.Information)
        m.setWindowTitle("Registro Empleado")
        m.setStandardButtons(QMessageBox.StandardButton.Ok)

        if self.femp.txtNombres.text() == "":
            m.setText("Captura nombre del empleado")
            self.femp.txtNombres.setFocus()
        elif self.femp.txtApellidoP.text()=="":
            m.setText("Captura apellido paterno del empleado")
            self.femp.txtApellidoP.setFocus()
        elif self.femp.txtApellidoM.text() == "":        
            m.setText("Captura apellido materno del empleado")
            self.femp.txtApellidoM.setFocus()
        elif self.femp.txtRFC.text() == "":
            m.setText("Captura RFC del empleado")
            self.femp.txtRFC.setFocus()
        elif self.femp.txtCURP.text() == "":
            m.setText("Captura CURP del empleado")
            self.femp.txtCURP.setFocus()
        elif self.femp.txtCel.text() == "":
            m.setText("Captura teléfono del empleado")
            self.femp.txtCel.setFocus()
        elif not self.femp.txtCel.text().isnumeric():
            m.setText("Captura solo números")
            self.femp.txtCel.setText("55")
            self.femp.txtCel.setFocus()
        elif len (self.femp.txtCel.text()) < 10:
            m.setText("Captura un teléfono válido")
            self.femp.txtCel.setText("55")
            self.femp.txtCel.setFocus()    
        elif self.femp.txtNSS.text()=="":
            m.setText("Captura el numero de seguridad social")
            self.femp.txtNSS.setFocus()
        elif not self.femp.txtNSS.text().isnumeric():
            m.setText("Captura solo números")
            self.femp.txtNSS.setFocus()    
        elif self.femp.cmbPuesto.currentIndex() == 0:
            m.setText("Seleccciona una opcion")
            self.femp.cmbPuesto.setFocus()
        elif self.femp.cmbDepto.currentIndex() == 0:
            m.setText("Seleccciona una opcion")
            self.femp.cmbDepto.setFocus()
        elif self.femp.txtSueldoD.text() == "":
            m.setText("Captura el sueldo del empleado")
            self.femp.txtSueldoD.setFocus()    
        elif not self.femp.txtSueldoD.text().replace(".","",1).isnumeric():
            m.setText("Captura un importe correcto")
            self.femp.txtSueldoD.setText("0.00")
            self.femp.txtSueldoD.setFocus()
        else:
            regEmpleado = RegEmpleado(
                nombres=self.femp.txtNombres.text().upper(),
                apellido_pat=self.femp.txtApellidoP.text().upper(),
                apellido_mat=self.femp.txtApellidoM.text().upper(),
                rfc=self.femp.txtRFC.text().upper(),
                curp=self.femp.txtCURP.text().upper(),
                numss=self.femp.txtNSS.text().upper(),
                f_nacimiento=self.femp.dateBoxFN.date().toString("yyyy-MM-dd"),
                puesto=self.femp.cmbPuesto.currentText(),
                departamento=self.femp.cmbDepto.currentText(),
                sueldo=float(self.femp.txtSueldoD.text()),
                direccion=self.femp.txtDireccion.toPlainText(),
                telefono=self.femp.txtCel.text(),
                email=self.femp.txtEmail.text().lower(),
                f_ingreso=self.femp.dateBoxFI.date().toString("yyyy-MM-dd"),
                f_baja="",
                status=True,
                usuario=self.pp.lblName_User.text(),
                f_reg=current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            )
            objData = RegEmpleadoData()
            if objData.registrar(regEmpleado):
                m.setText("Empleado registrado con éxito")
                self.limpiar_campos_femp()
            else:
                m.setText("Empleado ya registrado")
                self.limpiar_campos_femp()
        m.exec()

    def limpiar_campos_femp(self):
        self.femp.txtNombres.setText("")
        self.femp.txtApellidoM.setText("")
        self.femp.txtApellidoP.setText("")
        self.femp.txtRFC.setText("")
        self.femp.txtCURP.setText("")
        self.femp.txtNSS.setText("")
        self.femp.txtDireccion.setText("")
        self.femp.txtCel.setText("")
        self.femp.txtEmail.setText("")
        self.femp.cmbPuesto.setCurrentIndex(0)
        self.femp.cmbDepto.setCurrentIndex(0)
        self.femp.txtSueldoD.setText("")
    
    def salir_form_empleados(self):
        self.femp.close()
    
#############################ACTUALIZAR CUOTAS  (INCREMENTAR)###########################################
    def form_incre_cuotas(self):
        self.finc=uic.loadUi(self.resource_path("gui/formIncreCuotas.ui"))
        self.finc.setWindowTitle("Actualizar Cuotas")
        self.finc.show()
        self.finc.txt_porcentaje.setText("0.00")    
        self.finc.btnEjecutar.clicked.connect(self.incremento_masivo_cuotas)
        self.finc.btnSalir.clicked.connect(self.salir_form_finc)

    def incremento_masivo_cuotas(self):
        if self.finc.cmb_tcuota.currentIndex()==0:
            m=QMessageBox()
            m.setIcon(QMessageBox.Icon.Information)
            m.setWindowTitle("Incremento Cuotas")
            m.setText("Selecciona una opcion")
            m.exec()
        elif self.finc.txt_porcentaje.text() == "" or float(self.finc.txt_porcentaje.text()) <= 0:
            m=QMessageBox()
            m.setIcon(QMessageBox.Icon.Information)
            m.setWindowTitle("Incremento Cuotas")
            m.setText("Captura un porcentaje")
            self.finc.txt_porcentaje.setFocus()
            m.exec()
        elif not self.finc.txt_porcentaje.text().replace(".","",1).isnumeric():
            m=QMessageBox()
            m.setIcon(QMessageBox.Icon.Information)
            m.setWindowTitle("Incremento Cuotas")
            m.setText("Captura un porcentaje correcto")
            self.finc.txt_porcentaje.setText("0.00")
            self.finc.txt_porcentaje.setFocus()
            m.exec()
        else:
            if self.finc.cmb_tcuota.currentIndex()==1:  
                porcentaje_inc=float(self.finc.txt_porcentaje.text())
                objData = UbicacionesData()
                data = objData.lista_ubicaciones()
                for item in data:
                    cuota = round(float(item[3]),2)
                    cuota_inc = round(cuota + (cuota * porcentaje_inc / 100),2)
                    objData.update_cuotas_locales(item[1], cuota_inc)
                    
                if objData.update_cuotas_locales(item[1],cuota_inc):
                    m = QMessageBox()
                    m.setIcon(QMessageBox.Icon.Information)
                    m.setWindowTitle("Incremento Cuotas")
                    m.setText("Cuotas incrementadas con éxito")
                    m.exec()
                    self.finc.cmb_tcuota.setCurrentIndex(0)
                    self.finc.txt_porcentaje.setText("0.00")    
                else:
                    m = QMessageBox()
                    m.setIcon(QMessageBox.Icon.Critical)
                    m.setWindowTitle("Incremento Cuotas")
                    m.setText("Error al incrementar cuotas")
                    m.exec()
            else:
                porcentaje_inc=float(self.finc.txt_porcentaje.text())
                objData = ListaAreasData()
                data = objData.lista_areasC()
                for item in data:
                    cuota = round(float(item[3]),2)
                    cuota_inc = round(cuota + (cuota * porcentaje_inc / 100),2)
                    objData.update_cuotas_areas(item[1], cuota_inc)
                    
                if objData.update_cuotas_areas(item[1],cuota_inc):
                    m = QMessageBox()
                    m.setIcon(QMessageBox.Icon.Information)
                    m.setWindowTitle("Incremento Cuotas")
                    m.setText("Cuotas incrementadas con éxito")
                    m.exec()
                    self.finc.cmb_tcuota.setCurrentIndex(0)
                    self.finc.txt_porcentaje.setText("0.00")    
                else:
                    m = QMessageBox()
                    m.setIcon(QMessageBox.Icon.Critical)
                    m.setWindowTitle("Incremento Cuotas")
                    m.setText("Error al incrementar cuotas")
                    m.exec()
        
    def salir_form_finc(self):
        self.finc.close()






    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PantallaPrincipal()
    sys.exit(app.exec())    
    
    


    






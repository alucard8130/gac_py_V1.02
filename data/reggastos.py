import conexion_db as con
from model.operaciones import Reg_Gasto


class RegGastoData():
    def _registrar(self, info=Reg_Gasto):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        self.cursor.execute("""INSERT INTO gastos values(null,'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')
        """.format(info._nFact,info._n_prov,info._tipoG,info._descG,info._foPago,info._cheque,info._iPago,info._ivaRet,info._isrRet,info._feGasto,info._usuario,info._feReg))
        self.db.commit()
        if self.cursor.rowcount==1:
            return True
        else:
            return False

class GastosDataGral():
    def get_infox_prov(self,prov):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        query= self.cursor.execute("""
        SELECT id,num_factura,proveedor_name,tipo_gasto,descripcion_gasto,forma_pago,importe_pago,fecha_gasto,iva_ret,isr_ret FROM gastos
        WHERE proveedor_name='{}'""".format(prov))
        serch_info=query.fetchall()
        self.db.close()    
        return(serch_info)
    
    def get_infox_tipoG(self,tipoG):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        query= self.cursor.execute("""
        SELECT id,num_factura,proveedor_name,tipo_gasto,descripcion_gasto,forma_pago,importe_pago,fecha_gasto,iva_ret,isr_ret FROM gastos
        WHERE tipo_gasto='{}'""".format(tipoG))
        serch_info=query.fetchall()
        self.db.close()    
        return(serch_info)
    
    def get_info_xfechas(self,f_Ini,f_Fin):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        query= self.cursor.execute("""
        SELECT id,num_factura,proveedor_name,tipo_gasto,descripcion_gasto,forma_pago,importe_pago,fecha_gasto,iva_ret,isr_ret FROM gastos
        WHERE fecha_gasto BETWEEN '{}' AND '{}'""".format(f_Ini,f_Fin))
        serch_info=query.fetchall()
        self.db.close()    
        return(serch_info)
    
    def get_infox_empleado(self,empleado):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        query= self.cursor.execute("""
        SELECT id,num_factura,proveedor_name,tipo_gasto,descripcion_gasto,forma_pago,importe_pago,fecha_gasto,iva_ret,isr_ret FROM gastos
        WHERE gastos.proveedor_name ='{}'""".format(empleado))
        serch_info=query.fetchall()
        self.db.close()    
        return(serch_info)
    
    def eliminar_regx_id(self, id_registro):
        self.db = con.Conexion().conectarBd()
        self.cursor = self.db.cursor()
        self.cursor.execute("""
        DELETE FROM gastos
        WHERE id = '{}'""".format(id_registro))
        self.db.commit()
        self.db.close()
        return True
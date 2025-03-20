
import conexion_db as con


class CarteraDataCM():
    def buscar_info_ubicacion(self,ubicacion,cliente):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        query= self.cursor.execute("""
        SELECT tipo_cuota,num_fact,imp_adeudo,imp_pago,saldo_adeudo,f_cobro_o_pago,forma_pago,num_cheque,cta_banco,tipo_factura FROM cartera
        WHERE area_o_local='{}' AND cliente_facturacion='{}'
        """.format(ubicacion,cliente)
        )
        serch_info=query.fetchall()
        self.db.close()    
        return(serch_info)
        


class CarteraDataAC():
    def buscar_info_area_x_contrato(self,contrato):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        query= self.cursor.execute("""
        SELECT tipo_cuota,num_fact,imp_adeudo,imp_pago,saldo_adeudo,f_cobro_o_pago,forma_pago,num_cheque,cta_banco,tipo_factura FROM cartera
        WHERE num_contrato='{}'""".format(contrato)
        )
        serch_info=query.fetchall()
        self.db.close()    
        return(serch_info)
                
class CarteraDataGral():
    def get_info_xcliente(self,cliente,tipo_fact):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        query= self.cursor.execute("""
        SELECT tipo_cartera,tipo_cuota,num_fact,forma_pago,cta_banco,imp_pago,f_cobro_o_pago FROM cartera
        WHERE cliente_facturacion='{}' AND tipo_factura='{}'""".format(cliente,tipo_fact))
        serch_info=query.fetchall()
        self.db.close()    
        return(serch_info) 
                   
    def get_info_xtipo(self,tipo):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        query= self.cursor.execute("""
        SELECT tipo_cartera,tipo_cuota,num_fact,forma_pago,cta_banco,imp_pago,f_cobro_o_pago FROM cartera
        WHERE tipo_cuota='{}'""".format(tipo))
        serch_info=query.fetchall()
        self.db.close()    
        return(serch_info)
    
    def get_info_xfechas(self,tipo,fecha_ini,fecha_fin):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        query= self.cursor.execute("""
        SELECT tipo_cartera,tipo_cuota,num_fact,forma_pago,cta_banco,imp_pago,f_cobro_o_pago FROM cartera
        WHERE tipo_factura='{}' AND f_cobro_o_pago BETWEEN '{}' AND '{}'""".format(tipo,fecha_ini,fecha_fin))
        serch_info=query.fetchall()
        self.db.close()    
        return(serch_info)
    
    def get_info_xtipo_cartera(self,tipo_fact,tipo_cartera):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        query= self.cursor.execute("""
        SELECT tipo_cartera,tipo_cuota,num_fact,forma_pago,cta_banco,imp_pago,f_cobro_o_pago FROM cartera
        WHERE tipo_factura='{}' AND tipo_cartera='{}'""".format(tipo_fact,tipo_cartera))
        serch_info=query.fetchall()
        self.db.close()    
        return(serch_info)
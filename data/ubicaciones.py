import conexion_db as con

class UbicacionesData():
    def lista_ubicaciones(self):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        query= self.cursor.execute("SELECT * FROM ubicaciones order by num_local")
        serch_info=query.fetchall()
        self.db.close()    
        return(serch_info)
    
    def update_cuotas_locales(self,local,cuota):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        query= self.cursor.execute("UPDATE ubicaciones SET cuota_mensual='{}' WHERE num_local='{}'".format(cuota,local))
        self.db.commit()
        self.db.close()    
        return(query)    

        
class AreasData():
    def lista_areas_x_contrato(self,contrato):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        query= self.cursor.execute("""SELECT * FROM contratos WHERE num_contrato='{}'""".format(contrato))       
        serch_info=query.fetchall()
        self.db.close()    
        return(serch_info)
                
class ListaAreasData():
    def lista_areasC(self):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        query= self.cursor.execute("SELECT * FROM areas_comunes order by num_area")
        serch_info=query.fetchall()
        self.db.close()    
        return(serch_info)

    def update_cuotas_areas(self,area,cuota):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        query= self.cursor.execute("UPDATE areas_comunes SET cuota_mensual='{}' WHERE num_area='{}'".format(cuota,area))
        self.db.commit()
        self.db.close()    
        return(query)

class ListaCuotasData():
    def lista_cuotas_x_area(self,area):
        self.db = con.Conexion().conectarBd()
        self.cursor= self.db.cursor()
        query= self.cursor.execute("SELECT * FROM areas_comunes WHERE num_area='{}' order by num_area".format(area))
        serch_info=query.fetchall()
        self.db.close()    
        return(serch_info)        

class Repositorio:
    def __init__(self, db, table):
        self.db = db
        self.table = table
        
    def cadastrar(self, campos, valores):
        columns = ','.join(campos)
        values_qtd = ','.join(['%s']*len(valores))
        query = f"INSERT INTO {self.table} ({columns}) VALUES ({values_qtd})"
        return self.db.execute(query, valores)
    
    def listar(self):
        return self.db.execute(f"SELECT * FROM {self.table}", fetch="all")
    
    def buscar(self, id_):
        return self.db.execute(f"SELECT * FROM {self.table} WHERE id = %s", (id_,), fetch="one")
    
    def atualizar(self, id_, campos, valores):
        set_=','.join(f"{i}=$s" for i in campos)
        query = f"UPDATE {self.table} SET {set_} WHERE id = %s"
        return self.db.execute(query , (*valores, id_))
    
    def deletar(self, id_):
        return self.db.execute(f"DELETE FROM {self.table} WHERE id = %s", (id_, ))
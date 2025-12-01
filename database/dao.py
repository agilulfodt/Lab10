from database.DB_connect import DBConnect
from model.hub import Hub
from model.spedizione import Spedizione

class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    # TODO
    @staticmethod
    def read_all_spedizioni():
        """
        legge dal database tutte le spedizioni
        :return: lista di oggetti Spedizione
        """
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute('SELECT * FROM spedizione')
        lista_spedizioni = []
        for row in cursor:
            spedizione = Spedizione(**row)
            lista_spedizioni.append(spedizione)
        cursor.close()
        cnx.close()
        return lista_spedizioni

    @staticmethod
    def read_all_hubs():
        """
        legge dal database tutti gli hubs
        :return: dizionario di oggetti Hub le cui chiavi sono gli id
        """
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute('SELECT * FROM hub')
        dizio_hubs = {}
        for row in cursor:
            hub = Hub(**row)
            dizio_hubs[hub.id] = hub
        cursor.close()
        cnx.close()
        return dizio_hubs


if __name__ == '__main__':
    dao = DAO()
    print(dao.read_all_spedizioni())
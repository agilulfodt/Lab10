from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = []
        self.G = nx.Graph()

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
        guadagno medio per spedizione >= threshold (euro)
        """
        # TODO
        self.G.clear()

        self._nodes = DAO.read_all_hubs()
        self.G.add_nodes_from(self._nodes.values())

        #leggo tutte le spedizioni e le gestisco qui in python
        #le raggruppo per coppie di hub (in un frozenset, visto che il grafo non è orientato) e calcolo il valore medio
        lista_spedizioni = DAO.read_all_spedizioni()
        somme = {}
        conteggi = {}
        for spedizione in lista_spedizioni:
            key = frozenset({self._nodes[spedizione.id_hub_origine], self._nodes[spedizione.id_hub_destinazione]})
            if key not in somme:
                somme[key] = 0.0
                conteggi[key] = 0
            somme[key] += spedizione.valore_merce
            conteggi[key] += 1
        for key in conteggi:
            if somme[key]/conteggi[key] >= threshold:
                node1, node2 = tuple(key)
                self._edges.append((node1, node2, somme[key]/conteggi[key]))

        self.G.add_weighted_edges_from(self._edges)
        print(len(self._edges))

    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        # TODO
        return self.G.number_of_edges()

    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        # TODO
        return self.G.number_of_nodes()

    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        # TODO
        return self._edges


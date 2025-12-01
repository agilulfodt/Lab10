import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_tratte(self, e):
        """
        Funzione che controlla prima se il valore del costo inserito sia valido (es. non deve essere una stringa) e poi
        popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Hub presenti
        * Numero di Tratte
        * Lista di Tratte che superano il costo indicato come soglia
        """
        # TODO
        if self._view.guadagno_medio_minimo.value == "":
            self._view.show_alert("Inserire un valore per il guadagno medio minimo")
            return

        self._model.costruisci_grafo(int(self._view.guadagno_medio_minimo.value))

        numero_hub = self._model.get_num_nodes()
        numero_tratte = self._model.get_num_edges()
        lista_tratte = self._model.get_all_edges()

        self._view.lista_visualizzazione.controls.clear()
        self._view.lista_visualizzazione.controls.append(ft.Text(f"Numero di Hubs: {numero_hub}"))
        self._view.lista_visualizzazione.controls.append(ft.Text(f"Numero di Tratte: {numero_tratte}"))
        count = 0
        for edge in lista_tratte:
            count += 1
            self._view.lista_visualizzazione.controls.append(ft.Text(f"{count}) [{edge[0]} -> {edge[1]}] -- guadagno medio per spedizione: € {edge[2]}"))

        self._view.update()
from abc import ABC, abstractmethod
from typing import Any


class EnglishAbs(ABC):
    @abstractmethod
    def carregar_dados(self, path):
        pass

    @abstractmethod
    def retornar_palavras(self):
        pass

    @abstractmethod
    def retornar_pronuncia_e_traducao(self):
        pass

    @abstractmethod
    def adicionar_nova_palavra(self, p_p_t, data):
        pass

    @abstractmethod
    def editar_palavra(self, data) -> dict:
        pass

    @abstractmethod
    def remover_palavra(self, data) -> dict:
        pass

    @abstractmethod
    def pesquisar_palavra(self, palavra, data) -> dict:
        pass

    @abstractmethod
    def pesquisar_pronuncia(self, pronuncia, data) -> dict:
        pass

    @abstractmethod
    def retornar_palavra_aleatorio(self, data) -> dict:
        pass

    @abstractmethod
    def total_palavras(self, data) -> int:
        pass

    @abstractmethod
    def exportar_para_csv(self, data) -> bool:
        pass

    @abstractmethod
    def exportar_para_pdf(self, data) -> bool:
        pass

    @abstractmethod
    def retornar_por_nivel(self, data) -> dict:
        pass

    @abstractmethod
    def load_english_file(self):
        pass

    @abstractmethod
    def save_edited_video(self):
        pass

    # Dict
    @abstractmethod
    def add_item_dictionary(self):
        pass

    @abstractmethod
    def removal_item_dictionary(self):
        pass

    @abstractmethod
    def get_value_dictionary(self):
        pass

    @abstractmethod
    def get_key_dictionary(self):
        pass

    @abstractmethod
    def get_all_items_dictionary(self):
        pass

    @abstractmethod
    def contar_itens_dict(self):
        pass

    @abstractmethod
    def update_dictionary(self):
        pass

    @abstractmethod
    def clear_dictionary(self):
        pass

    @abstractmethod
    def check_key_dictionary(self):
        pass

    @abstractmethod
    def copy_dictionary(self):
        pass

    @abstractmethod
    def filter_items_dictionary(self):
        pass

    @abstractmethod
    def get_key_by_value_dictionary(self):
        pass

    @abstractmethod
    def calcular_soma_valores_dict(self):
        pass

    @abstractmethod
    def calculate_average_values_dictionary(self):
        pass

    @abstractmethod
    def check_empty_dictionary(self):
        pass

    @abstractmethod
    def join_dictionary(self):
        pass

    @abstractmethod
    def get_order_keys(self):
        pass

    @abstractmethod
    def copy_keys_to_list(self):
        pass
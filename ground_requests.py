# Черкасов Виткор, 30А - когорта - Финальный проект. Инженер по тестированию плюс


import requests
import configuration
import data

def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.order_body)
    
    
def get_order_mean(track):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_INFO_PATH,
            params = {"t": track})
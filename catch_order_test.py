# Черкасов Виткор, 30А - когорта - Финальный проект. Инженер по тестированию плюс

import ground_requests

def get_track_number_order():
    track = ground_requests.post_new_order()
    return track.json()["track"]

def test_make_order_save_status():
    track = get_track_number_order()
    get_response = ground_requests.get_order_mean(track)
    assert get_response.status_code == 200
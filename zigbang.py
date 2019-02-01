import requests
from urllib.parse import urlencode

def get_addr_info(keyword="망원동"):
    url = "https://apis.zigbang.com/search/all?q={}&type=oneroom".format(keyword)
    response = requests.get(url)
    json_obj = response.json()
    return json_obj["items"][0]["lat"], json_obj["items"][0]["lng"]

def get_ids(lat, lng):
    url = "https://api.zigbang.com/v3/items2?lat_south={}&lat_north={}&lng_west={}&lng_east={}\
            &room=[01,02,03,04,05]".format(lat - 0.005, lat + 0.005, lng - 0.005, lng + 0.005)
    params = {
        "lat_south": lat - 0.01,
        "lat_north": lat + 0.01,
        "lng_west": lng - 0.01,
        "lng_east": lng + 0.01,
        "room": "[01,02,03,04,05]",
    }
    params_str = urlencode(params)
    url = "https://api.zigbang.com/v3/items2?" + params_str
    response = requests.get(url)
    json_obj = response.json()
    items = json_obj["list_items"]
    return [item["simple_item"]["item_id"] for item in items]

def get_items(ids):
    url = "https://api.zigbang.com/v3/items?detail=true&item_ids={}".format(str(ids).replace(" ",""))
    response = requests.get(url)
    json_obj = response.json()
    items = json_obj["items"]
    datas = [item["item"] for item in items]
    return datas

def main(addr="망원동"):
    lat, lng = get_addr_info(addr)
    ids = get_ids(lat, lng)
    return get_items(ids)

import vk_api
import datetime # работа с датой и временем
import time
import requests


def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return httpResponse('<pre>' + r.text + '</pre>')


while True:
    vk = vk_api.VkApi(token="4f08f0766cb68d737b4e3df8744df9dd951aac5d1e0fa6c4967347354ce7cd6c0d59ba6f9354b6b90660b")

    delta = datetime.timedelta(hours=3, minutes=0)  # разница от UTC. Можете вписать любое значение вместо 3
    t = (datetime.datetime.now(datetime.timezone.utc) + delta)  # Присваиваем дату и время переменной «t»

    nowtime = t.strftime("%H:%M")  # текущее время
    nowdate = t.strftime("%d.%m.%Y")  # текущая дата

    on = vk.method("friends.getOnline")  # получаем список id друзей онлайн
    counted = len(on)  # считаем кол-во элементов в списке
    
    ch = vk.method("account.getBanned") # получаем список пользователей чс
    kch = len(ch) # считаем кол-во элементов в списке 

    vk.method("status.set", {"text": nowtime + " ● " + nowdate + " ● " + "Друзей онлайн: " + str(counted) + " ● " + "Людей в чс: " + str(kch)})

    time.sleep(600)  # погружаем скрипт в «сон» на 30 секунд

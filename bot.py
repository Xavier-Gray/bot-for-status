import vk_api
import datetime # работа с датой и временем
import time
import requests
import random

def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return httpResponse('<pre>' + r.text + '</pre>')


while True:
    vk = vk_api.VkApi(token="7e9379684914de854c95bde7b6d9fd75a67c1578bc6b736532642992de5c196a07757aa98ae075a19003b")

    delta = datetime.timedelta(hours=3, minutes=0)  # разница от UTC. Можете вписать любое значение вместо 3
    t = (datetime.datetime.now(datetime.timezone.utc) + delta)  # Присваиваем дату и время переменной «t»

    nowtime = t.strftime("%H:%M")  # текущее время
    nowdate = t.strftime("%d.%m.%Y")  # текущая дата

    on = vk.method("friends.getOnline")  # получаем список id друзей онлайн
    onl = len(on)  # считаем кол-во элементов в списке
    #print(str(on))
    ch = vk.method("account.getBanned")  # получаем список пользователей чс
    kch = (ch['count'])  # считаем кол-во элементов в списке
    #print(str(ch))

    ans = ["ответ 1", "ответ 2", "ответ 3"] # варианты фраз
    wr = ans[random.randint(0, len(ans) - 1)] # рандомнаяфраза из списка
    vk.method("status.set", {
        "text": "☀" + nowtime + "💤"+" ● "+ "📅"+ nowdate +"📌"+ " ● " + "👬"+"Друзей онлайн: " + str(onl) + "👫"+" ● " +"🚷"+ "Людей в чс: " + str(kch) +"🚷"+ " ● " + "✨Однажды мы сможем встретиться✨" })

    time.sleep(600)  # погружаем скрипт в «сон» на 30 секунд

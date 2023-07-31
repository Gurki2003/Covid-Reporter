from plyer import notification
import requests
import random 
from time import sleep


from bs4 import BeautifulSoup


def notifyme(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="gs.ico",
        timeout=3
    )


def getdata(url):
    r = requests.get(url, allow_redirects=True)
    return r.text

while True:
    number= random.randint(0,35)
    htmldata = getdata(
        "https://www.mygov.in/corona-data/covid19-statewise-status/")
    soup = BeautifulSoup(htmldata, 'html.parser')
    list_of_states = []

    # states = soup.find('div',class_='header-nav-states menu-row')
    # for state in states.find_all('span'):
    #     list_of_states.append(state.text)

    states = soup.find_all(
        'div', 'field field-name-field-select-state field-type-list-text field-label-above')
    for state in states:
        st = state.find('div', class_='field-item even')
        list_of_states.append(st.text)

    total_confirmed = []

    confirm = soup.find_all(
        'div', class_='field field-name-field-total-confirmed-indians field-type-number-integer field-label-above')
    for conf in confirm:
        tot = conf.find('div', class_='field-item even')
        total_confirmed.append(tot.text)

    # print(total_confirmed)
    # print(len(total_confirmed))
    # print(len(list_of_states))
    # print(list_of_states)

    head="Cases Of Covid :\n"
    data=(f"City : {list_of_states[number]}\nCases: {total_confirmed[number]}")
    notifyme(head,data)
    sleep(10)

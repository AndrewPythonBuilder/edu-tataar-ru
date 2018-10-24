import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
import constants
import datetime


def autoriz_edu(date_d):
    r = datetime.datetime(date_d.year, date_d.month, date_d.day, 00, 00, 00)
    r = time.mktime(r.timetuple())
    ret = []
    session = requests.Session()
    url = 'https://edu.tatar.ru/logon'
    data = {'main_login': '1562002956', 'main_password':'bMhrsnK_'}
    session.post(url, data, headers=dict(referer='https://edu.tatar.ru/user/diary/week?date='+str(r)[:-2]))
    flag = False
    all_about = session.get('https://edu.tatar.ru/user/diary/week?date='+str(r)[:-2]).text
    soup = BeautifulSoup(all_about, "html.parser")
    table = soup.find('tbody')
    try:
        time_table = table.text
        flag = True
    except:
        flag = False

    if flag == True:
        string = (str(time_table).replace('\t', '').replace('\r', '').split('\n'))
        for i in string:
            if i != '' and i!='1' and i!='2' and i!='3' and i!='4' and i!='5' :
                ret.append(i)
        requests.Session().delete('https://edu.tatar.ru/user/diary/week?date='+str(r)[:-2])
        return ret
    else:
        return False

def unix_time(date_d):
    s = autoriz_edu(date_d)
    arg = date_d.day
    flag = False
    z = []
    if s != False:
        for i in s:
            if i == str(arg):
                flag = True
            elif i == str(arg+1):
                flag = False
            elif flag == True:
                z.append(i)
    else:
        z = 'Не удалось'
    return z


def analization(arg):
    z = []
    for i in range(len(arg)-1):
        if arg[i] in constants.lessons:
            if arg[i+1] in constants.lessons:
                z.append(arg[i])
                z.append('None')
            else:
                z.append(arg[i])
                z.append(arg[i+1])
    return z

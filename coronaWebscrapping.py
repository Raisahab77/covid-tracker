from plyer import notification
from bs4 import BeautifulSoup
import requests

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "coronavirusIcon.ico",
        timeout = 10
    )

def getData(url):
    r = requests.get(url)
    return r.text

def caseList():
    data = getData("https://www.mygov.in/hi/covid-19/")
    soup = BeautifulSoup(data,"html.parser")
    numbers = []
    for table in soup.find_all(class_="icount"):
        number = table.get_text()
        numbers.append(number)
    return numbers

if __name__ == "__main__":
    print("1:- Total Active Covid-19 cases")
    print("2:- Total Deaths by Covid-19")
    print("3:- Total recoverd case")
    print("4:- Total covid-19 cases from Starting till now")
    print("5:- All case detail about Covid-19")

    choice = int(input("Enter your Choice :"))
    lst = caseList() 
    if choice==1:
        active_case = lst[0]
        notifyMe("Active Case",f"Total active covid-19 cases are {active_case}")
        print(f"Total active covid-19 cases are {active_case}")

    elif choice==2:
        total_death = lst[3]
        notifyMe("Total Death",f"total death by covid-19 are {total_death}")
        print(f"total death by covid-19 are {total_death}")

    elif choice==3:
        recoverd_case = lst[2]
        notifyMe("Total Recovery",f"Covid-19 recovered cases are {recoverd_case}")
        print(f"Covid-19 recovered cases are {recoverd_case}")

    elif choice==4 :
        total_case = lst[1]
        notifyMe("Total Case",f"Total covid-19 cases are {total_case}")
        print(f"Total covid-19 cases are {total_case}")

    elif choice==5:
    
        output = (f"Here is the Full report on covid-19\nActive Case = {lst[0]}\nTotal Case = {lst[1]}\nTotal Recovered Case = {lst[2]}\nTotal Deaths = {lst[3]}")
        print(output)

    else:
        print("wrong input")
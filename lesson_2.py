
from prettytable import PrettyTable
import requests
import os


'''

array = []
i = 1
d = 1
while i <= 10:
    list = int(input("введіть числа"))
    array.append(list)
    d *= list
    i +=1
print(array)
print("Dobutok=>>> ", d)



list=[]
sum=0
for i in range(10):
    x = randint(0,20)
    list.append(x)
    if x%2 !=0:
        sum=sum+x
print(list)
print(sum)    




URL = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
currency = requests.get(URL)
currency = currency.json()
print("currency ", currency, "\n", type(currency))


URL = "https://api.covid19api.com/summary"
currency = requests.get(URL)
currency = currency.json()
print("currency ", currency, "\n", type(currency))
'''


class Covid:

    def start(self):
        exit = False
        while not exit:
            choice = int(
                input("1. Show COVID19 information\n2. Sort by new confirmed\n3. Get detailed information on the name of the country\n0. Exit\n=:>> "))
            if choice == 1:
                URL = "https://api.covid19api.com/summary"
                self.get_data(URL)
            elif choice == 2:
                URL = "https://api.covid19api.com/summary"
                self.get_sort(URL)
            elif choice == 3:
                URL = "https://api.covid19api.com/summary"
                self.get_one_country(URL)
            elif choice == 0:
                exit = True
            else:
                print("Use --help for reading manual")

    def get_data(self, URL):
        URL = "https://api.covid19api.com/summary"
        covid = requests.get(URL)
        covid = covid.json()

        table = PrettyTable()
        table.field_names = ["Country: ", "NewConfirmed: ", "TotalConfirmed: ", "NewDeaths: ",
                             "TotalDeaths: ", "NewRecovered: ", "TotalRecovered: "]

        for item in covid["Countries"]:
            table.add_row([item["Country"], item["NewConfirmed"], item["TotalConfirmed"],
                           item["NewDeaths"], item["TotalDeaths"], item["NewRecovered"], item["TotalRecovered"]])

        print(table)

    def get_sort(self, URL):

        def newConfirmend(covid):
            return covid["NewConfirmed"]

        URL = "https://api.covid19api.com/summary"
        covid = requests.get(URL)
        covid = covid.json()["Countries"]

        table = PrettyTable()
        table.field_names = ["Country: ", "NewConfirmed: ", "TotalConfirmed: ", "NewDeaths: ",
                             "TotalDeaths: ", "NewRecovered: ", "TotalRecovered: "]
        new_list = sorted(covid, key=newConfirmend, reverse=True)

        for item in new_list:

            table.add_row([item["Country"],  item["NewConfirmed"], item["TotalConfirmed"],
                           item["NewDeaths"], item["TotalDeaths"], item["NewRecovered"], item["TotalRecovered"]])
        print(table)

    def get_one_country(self, URL):
        URL = "https://api.covid19api.com/summary"
        covid = requests.get(URL)
        covid = covid.json()
        find = False
        country = input("Enter country: ")
        table = PrettyTable()
        table.field_names = ["Country: ", "NewConfirmed: ", "TotalConfirmed: ", "NewDeaths: ",
                             "TotalDeaths: ", "NewRecovered: ", "TotalRecovered: "]

        for item in covid["Countries"]:
            if item["Country"] == country.capitalize():
                table.add_row([item["Country"], item["NewConfirmed"], item["TotalConfirmed"],
                               item["NewDeaths"], item["TotalDeaths"], item["NewRecovered"], item["TotalRecovered"]])
                print(table)               
                find = True
                break
        if not find:
            print("Name is not defined!!!")
           
            


covid_19 = Covid()
covid_19.start()

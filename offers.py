from bs4 import BeautifulSoup
import requests

class Offer:
    def __init__(self, data, section):
            self.title = data.find('h3').text
            self.isPromoted = (data.find(class_='announcements-list-work-box-promo') is not None)
            self.desc = data.find('p').text
            self.date = data.findAll('span')[-1].text[5:10]
            if (section == 328 or section == 102):
                self.date = data.findAll('span')[-2].text[5:10]
            else:
                self.date = data.findAll('span')[-1].text[5:10]
            #print(data)
            #print(f"{self.title} {self.isPromoted} {self.date}")

def getOffers(count, section):
    site = "https://ddwloclawek.pl/pl/_ajax/getMore.php"
    offers = []
    for i in range(0, count, 10):
        #print("Pobieranie..(%.f%%) [%d/%d]"% ( i/float(count)*100, i, count) )
        try:
            data = {'tryb': 'getOgloszenie', 'ile': i, 'dzial': section}
            req = requests.post(site, data)
        except ValueError:
            print("Connection error")
            exit(1)

        html = BeautifulSoup(req.text, 'html.parser').findAll(class_='oglWyk')
        if len(html) == 0:
            print(f"Pobrano {len(offers)} ofert z działu #{section}.")
            return offers
        for offer in html:
            of = Offer(offer, section)
            offers.append(of)
            #print (of.date)
            if (len(offers) == count):
                print(f"Pobrano: {len(offers)} ofert z działu #{section}.")
                return offers


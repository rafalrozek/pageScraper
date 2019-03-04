from bs4 import BeautifulSoup
import requests

class Offer:
    def __init__(self, data):
        self.title = data.findAll('h3')[0].text
        self.isPromoted = (data.find(class_='announcements-list-work-box-promo') is not None)
        self.desc = data.findAll('p')[0].text
        if (self.isPromoted):
            id = data.findAll('span')[2].text
            self.date = data.findAll('span')[1].text[5:10]
        else:
            id = data.findAll('span')[1].text
            self.date = data.findAll('span')[0].text[5:10]
        self.id = int(id[1:])

def getOffers(count, section):
    site = "https://ddwloclawek.pl/pl/_ajax/getMore.php"
    offers = []
    for i in range(0, count, 10):
        #print("Pobieranie..(%.f%%) [%d/%d]"% ( i/float(count)*100, i, count) )
        try:
            data = {'tryb': 'getOgloszenie', 'ile': i, 'dzial': section}
            req = requests.post(site, data)
        except ValueError:
            print ("Connection error")
            exit(1)

        html = BeautifulSoup(req.text, 'html.parser').findAll(class_='oglWyk')
        if len(html) == 0:
            print(f"Pobrano {len(offers)} ofert z działu #{section}.")
            return offers
        for offer in html:
            of = Offer(offer)
            offers.append(of)
            #print (of.date)
            if (len(offers) == count):
                print(f"Pobrano {len(offers)} ofert z działu #{section}.")
                return offers


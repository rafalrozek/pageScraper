import matplotlib.pyplot as plt
import numpy as np
from offers import getOffers
from datetime import datetime, timedelta

print("Pobieranie danych..")
offers = getOffers(10, 102)
offers2 = getOffers(10, 328)
offers3 = getOffers(10, 102)

#generate data
xt = [(datetime.today() - timedelta(days=x)).strftime('%m-%d') for x in range(30, -1, -1)]
x = np.array([x for x in range(0, 31)]).astype(np.int)
y = np.array([len(list(filter(lambda p: p.date == d, offers))) for d in xt]).astype(int)

countOffers2 = [len(list(filter(lambda p: p.date == d, offers2))) for d in xt]
countOffers3 = [len(list(filter(lambda p: p.date == d, offers3))) for d in xt]


print(xt)
print (type(xt))
#generate plots
f, (ax, bx) = plt.subplots(2,1,sharey='col')

ax.plot(x, y, 'bp-')
ax.set_xticklabels(labels = xt)
ax.grid()

bx.plot(x, y, 'rp-')
bx.set_xticklabels(labels = xt)
bx.grid()

f.suptitle('Offers by category in last 31 days', fontsize=24)
f.set_size_inches(20, 12)


plt.xlabel('Days', fontsize=14)
plt.title = 'dd'
plt.ylabel('Offers', fontsize=14)
plt.subplots_adjust(hspace=0.75)
#plt.subplots(sharex='all')
plt.savefig("cat-102.png")



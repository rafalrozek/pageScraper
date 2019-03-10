import matplotlib.pyplot as plt
import numpy as np
from offers import getOffers
from datetime import datetime, timedelta

print("Pobieranie danych...")
offers = getOffers(300, 102)
offers2 = getOffers(300, 328)
offers3 = getOffers(300, 500)

#generate data
xt = [(datetime.today() - timedelta(days=x)).strftime('%m-%d') for x in range(30, -1, -1)]
x = np.array([x for x in range(0, 31)]).astype(np.int)


countOffers = [len(list(filter(lambda p: p.date == d, offers))) for d in xt]
countOffers2 = [len(list(filter(lambda p: p.date == d, offers2))) for d in xt]
countOffers3 = [len(list(filter(lambda p: p.date == d, offers3))) for d in xt]




#generate plots
f, (ax, bx, cx) = plt.subplots(3, 1, sharey='col')

ax.plot(xt, countOffers, 'bp-')
ax.set_title('Category #102')
ax.grid()

bx.plot(xt, countOffers2, 'rp-')
bx.set_title('Category #328')
bx.grid()

cx.plot(xt, countOffers3, 'gp-')
cx.set_title('Category #500')
cx.grid()

f.suptitle('Offers by category in last 31 days', fontsize=24)
f.set_size_inches(20, 12)
f.text(0.06, 0.5, 'Offers', ha='center', va='center', rotation='vertical', fontsize=20)
f.text(0.5, 0.03, 'Days', ha='center', va='center', rotation='horizontal', fontsize=20)


plt.subplots_adjust(hspace=0.5)
plt.savefig("offers.png")



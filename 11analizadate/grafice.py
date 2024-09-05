import pandas as pd
import matplotlib.pyplot as plt

data = {'An': [2010, 2011, 2012, 2013, 2014],
        'Vanzari': [500, 600, 700, 800, 900]}

df = pd.DataFrame(data)

df.plot(x='An', y='Vanzari', marker='o', linestyle='dashdot', color='b',
        label='Vanzari')

plt.xlabel('An')
plt.ylabel('Vanzari')
plt.title('Grafic linie - Vanzari in functie de an')
plt.legend()
plt.grid(True)
plt.show()

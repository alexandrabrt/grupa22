import pandas as pd
import matplotlib.pyplot as plt

data = {"Nota_matematica": [7.5, 8.0, 6.5, 9.0, 8.5],
        'Nota_engleza': [8.5, 7.0, 9.5, 8.0, 7.5]}

df = pd.DataFrame(data)

df.plot.scatter(x='Nota_matematica', y='Nota_engleza', color='green', marker='o')

plt.xlabel('Nota matematica')
plt.ylabel('Note engleza')
plt.title('Scatter plot - Relatia dintre notele la matematica si engleza')
plt.show()


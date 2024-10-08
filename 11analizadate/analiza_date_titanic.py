import seaborn as sns
import matplotlib.pyplot as plt

titanic_data = sns.load_dataset('titanic')
print(titanic_data.head())
# print(titanic_data)

sns.countplot(x='class', hue='survived', data=titanic_data)
plt.title("Analiza supravietuire in functie de clasa")
plt.show()

sns.histplot(x='age', hue='survived', data=titanic_data, kde=True)
plt.title('Analiza supravietuire in functie de varsta')
plt.show()

sns.countplot(x='sex', hue='survived', data=titanic_data)
plt.title('Analiza supravietuire in functie de sex')
plt.show()

sns.countplot(x='embarked', hue='survived', data=titanic_data)
plt.title('Analiza supravietuire in functie de portul de imbarcare')
plt.show()

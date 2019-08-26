import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Base_CSV_Test.csv", encoding="UTF-8", sep=";", header=0)
print(df.head())
print(df.describe())
print(df["ID Chamado"].plot.hist(bins=30, edgecolor='black'))
plt.show(df["ID Chamado"].plot.hist(bins=30, edgecolor='black'))
df = pd.read_csv("Dados_Teste.csv")
plt.show(df["preco"].plot.hist(bins=30, edgecolor='black'))
plt.show(df["bairro"].value_counts().plot.bar())
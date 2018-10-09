#1. primeira ação é explorar os dados da base de dados. Quais dados são?
from sklearn.datasets import load_boston

boston = load_boston()
#itens da base
boston.keys()

print(boston.DESCR)


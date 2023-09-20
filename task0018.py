'''В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. 
Сможете ли вы это сделать без get_dummies?
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
'''

import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создаем пустой DataFrame для хранения one-hot кодировки
one_hot_data = pd.DataFrame()

# Получаем уникальные значения из столбца 'whoAmI'
unique_values = data['whoAmI'].unique()

# Проходим по каждому уникальному значению и создаем новый столбец в one-hot DataFrame.
for value in unique_values:
    one_hot_data[f'is_{value}'] = (data['whoAmI'] == value).astype(int)

# Выводим преобразованный DataFrame
print (one_hot_data.head())
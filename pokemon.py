import numpy as np
import pandas as pd

pokemon = pd.read_csv('pokemon_data.csv')

print(pokemon)
print(pokemon.columns)

#acess coollum 1 of series data
print(pokemon['Type 1'])
#short hand way of referencing a colum 
print(pokemon.Defense)

#create new collum for attack to sp atk ratio
pokemon['Attack Ratio'] = pokemon['Attack'] / pokemon['Sp. Atk']
print (pokemon['Attack Ratio'])





poke = pokemon.set_index('Name')
#looking at axess specific index cell lookig for (row,col)
print (poke.loc['Pikachu', 'Type 1'])

#acess a range of rows 
print(poke.loc[['Bulbasaur', 'Squirtle', 'Charmander']])

# wnat print every row  in certian way
for index, row in poke.iterrows() :
    print(index, ' - ', row['Type 1'])
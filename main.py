import pandas as pd  # Importing pandas, numpy library to analyse data
import numpy as np
from textinfo import intro_legend, gen_data_legend, specific_data, error_message

def get_data():
    global df
    # Gather data from csv file, create variables to access statistical infromation from data frame
    df = pd.read_csv('PYTHON/NOTES/Machine Learning/Pandas/Pokemon/pokemonstats.csv')
    print('Data collected succesfully.')

get_data()
statistics = df.describe()
datas_types = df.dtypes
intro_legend()
programflag = True  # Encyclopedia program loops
while programflag == True:
    choice = input('Enter what you would like to view: ')
    if choice == '1':
        gen_data_legend()
        gen_data_choice = input('Enter your choice: ')
        if gen_data_choice == '1a':
            print(df.mean(numeric_only=True))
        elif gen_data_choice == '1b':
            print(df.median(numeric_only=True))
        elif gen_data_choice == '2':
            print(df.max(numeric_only=True))
        elif gen_data_choice == '3':
            print(df.min(numeric_only=True))
        elif gen_data_choice == '4a':
            print(statistics)
        elif gen_data_choice == '4b':
            print(datas_types)
        else:
            print('Error: Invalid input. Please refer to text above.')
        print('')
    elif choice == '2':
        specific_data()
        pokemon = input('Name of Pokemon: ')
        pokemon_games = df.loc[df['Name'].str.contains(pokemon)]
        print(pokemon_games)
        print('')
    else:
        error_message()
    quit_choice = input('Quit? ')
    if quit_choice == 'Yes':
        programflag = False
        print('Thanks for playing!')
    print('')

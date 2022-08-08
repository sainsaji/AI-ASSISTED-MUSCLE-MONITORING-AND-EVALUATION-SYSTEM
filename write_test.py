import pygsheets
import pandas as pd
import matplotlib.pyplot as plt
import random
from datetime import date
#authorization
gc = pygsheets.authorize(service_file='./key/key.json')

# Create empty dataframe
df = pd.DataFrame()

# Create a column
df['newdata'] = ['John', 'Steve', 'Sarah']

mario_game= {
    'Level':[],
    'x_val' :[],
    'y_val':[],
                }
game_data= {
    'game_id':[],
    'level':[],
    'attempt':[],
    'score' :[],
    'max_custom_value':[],
    'date':[]
                }
# for i in range(0,10):
#     mario_game['Level'].append("Low")
#     mario_game['x_val'].append(i*4)
#     mario_game['y_val'].append(i)

ds = pd.DataFrame(game_data)

# plt.plot(mario_game['x_val'],mario_game['y_val'])
# plt.show()

#open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
sh = gc.open('test_sheet')

#select the first sheet 
wks = sh[1]

#update the first sheet with df, starting at cell B2. 
wks.set_dataframe(ds,(1,1))

#getting the last row
row_count = len(wks.get_all_records()) + 2
print(row_count)

#appending to table

def writer(game_id,level,attempt,score,max_custom_value,date):
    data1=[game_id,level,attempt,score,max_custom_value,date]
    wks.append_table(data1,start='2')

# for i in range(10):
#     writer(
#     game_id=1,
#     level = "low",
#     attempt = i,
#     max_custom_value=random.randint(10,30),
#     score = random.randint
#     (50,100),
#     date = "June")

game_list = [1,2,3,4]
level_list = ["low","medium","high"]

for x in range(3):
    for y in range(0,5):
        for i in range(1,5):
            writer(
            game_id=y,
            level = level_list[x],
            attempt = i,
            max_custom_value=random.randint(10,30),
            score = random.randint
            (50,100),
            date = "June")

# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1X3bS6xLLxEdU7OVlNpyU96mpcM7HJLEm
"""

"""Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_84agEqWUeaGqKNU5TQcyFBLlO8imlhP
"""

import pandas as pd
baza={
    "FISH":["Zaripov Xabibullox ","Akbaraliyev Muhammadkarim","Nazirov Jasurbek","Sultanov Fazliddin","Ibrohimov Ozodbek","Sodiqjonov Dilmurodjon","Mahmudov Asliddin","Muhammadov Ozodbek","Aliyev Vali","Hoshimov Bekmurod"],
"Manzili ":["Fargʻona tumani","Fargʻona tumani","Fargʻona tumani","Chortoq tumani","Fargʻona tumani","Oltiariq tumani","Kitob tumani","Toshloq tumani","Uychi tumani","Beshariq tumani"],
"Yoshi":["20","19","19","19","19","20","19","19","27","29"],
"Ish joyi":[ "TATUFF","TATUFF","TATUFF","TATUFF","TATUFF","TATUFF","TATUFF","TATUFF","DXM","FNQZ"],
"Jinsi":["Erkak","Erkak","Erkak","Erkak","Erkak","Erkak","Erkak","Erkak","Erkak","Erkak"]
}
db=pd.DataFrame(baza)
print(db)

filtr=db[db['Ish joyi']=="FNQZ"]
print(filtr)

filtr=db[db['Yoshi']>"23"]
print(filtr)

filtr=db[db['Manzili ']=="Chortoq tumani"]
print(filtr)
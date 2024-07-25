import pandas as pd
import numpy as np

gss=pd.read_csv('tennisdata.csv',index_col=0)
gss.head()
def number(A,b):
    yes=0
    no=0
    for i in A :
        if i=="Yes":
            yes+=1
        else :
            no+=1
    if b=="Yes":
        return yes/len(A)
    elif b == "No":
        return no/len(A)
    elif b== "t_yes":
        return yes
    elif b=='t_no':
        return no
"""
yes=number(gss['PlayTennis'],"Yes")
no = number(gss['PlayTennis'],"No")
print(yes)
print(" ")
print(no)
"""
def outlook(A,B):
    tab_res = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
    total_yes = 0
    total_no = 0
    j=0
    t = (gss['PlayTennis'])
    for i in A:
        j+=1
        
        if i == "Sunny":
            tab_res[0][2] =  tab_res[0][2] + 1
            if yon(t,j) == "Yes":
                tab_res[0][0] =  tab_res[0][0] + 1
                total_yes +=1
            else:
                tab_res[0][1] =  tab_res[0][1] + 1
                total_no +=1
        if i == "Overcast":
            tab_res[1][2] = tab_res[1][2] + 1
            if yon(t,j) == "Yes":
                tab_res[1][0] = tab_res[1][0] + 1
                total_yes +=1
            else:
                tab_res[1][1] = tab_res[1][1] + 1
                total_no +=1
        if i== "Rain":
            tab_res[2][2] = tab_res[2][2] + 1
            if yon(t,j) == "Yes":
                tab_res[2][0] = tab_res[2][0] + 1
                total_yes +=1
            else:
                tab_res[2][1] = tab_res[2][1] + 1
                total_no +=1
    j=0
    for i in 3:
        for j in 3:
            if j == 0 : tab_res[i][j]/=total_yes
            if j == 1 : tab_res[i][j]/=total_no
            if j == 3 : tab_res[i][j]/=total_yes+total_no

def yon(A,p):
    j=0
    for i in A:
        j+=1
        if j == p:
            return i
def temperature(A):
    tab_res = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    total_yes = 0
    total_no = 0
    j=0
    t=(gss['PlayTennis'])
    for i in A:
        j+=1
        if i == "Hot":
            tab_res[0][2] = tab_res[0][2] + 1
            if yon(t,j) == "Yes":
                tab_res[0][0] = tab_res[0][0] + 1
                total_yes += 1
            else:
                tab_res[0][1] = tab_res[0][1] + 1
                total_no += 1
        if i == "Mild":
            tab_res[1][2] = tab_res[1][2] + 1
            if yon(t,j) == "Yes":
                tab_res[1][0] = tab_res[1][0] + 1
                total_yes += 1
            else:
                tab_res[1][1] = tab_res[1][1] + 1
                total_no += 1
        if i == "Cool":
            tab_res[2][2] = tab_res[2][2] + 1
            if yon(t,j) == "Yes":
                tab_res[2][0] = tab_res[2][0] + 1
                total_yes += 1
            else:
                tab_res[2][1] = tab_res[2][1] + 1
                total_no += 1

    for l in range(3):
        for k in range(3):
            if k == 0: tab_res[l][k] /= total_yes
            if k == 1: tab_res[l][k] /= total_no
            if k == 2: tab_res[l][k] /= total_yes + total_no
    print(tab_res)


def humidity(A):
    tab_res = [[0, 0, 0], [0, 0, 0]]
    total_yes = 0
    total_no = 0
    j=0
    t=(gss['PlayTennis'])
    for i in A:
        j+=1
        if i == "High":
            tab_res[0][2] = tab_res[0][2] + 1
            if yon(t,j) == "Yes":
                tab_res[0][0] = tab_res[0][0] + 1
                total_yes += 1
            else:
                tab_res[0][1] = tab_res[0][1] + 1
                total_no += 1
        if i == "Normal":
            tab_res[1][2] = tab_res[1][2] + 1
            if yon(t,j) == "Yes":
                tab_res[1][0] = tab_res[1][0] + 1
                total_yes += 1
            else:
                tab_res[1][1] = tab_res[1][1] + 1
                total_no += 1

    for l in range(2):
        for k in range(3):
            if k == 0: tab_res[l][k] /= number(t,"t_yes")
            if k == 1: tab_res[l][k] /= number(t,"t_no")
            if k == 2: tab_res[l][k] /= len(A)
    print(tab_res)

def wind(A):
    tab_res = [[0, 0, 0], [0, 0, 0]]
    total_yes = 0
    total_no = 0
    j=0
    t=(gss['PlayTennis'])
    for i in A:
        j+=1
        if i == "TRUE":
            tab_res[0][2] = tab_res[0][2] + 1
            if yon(t,j) == "Yes":
                tab_res[0][0] = tab_res[0][0] + 1
                total_yes += 1
            else:
                tab_res[0][1] = tab_res[0][1] + 1
                total_no += 1
        if i == "FALSE":
            tab_res[1][2] = tab_res[1][2] + 1
            if yon(t,j) == "Yes":
                tab_res[1][0] = tab_res[1][0] + 1
                total_yes += 1
            else:
                tab_res[1][1] = tab_res[1][1] + 1
                total_no += 1

    for l in range(2):
        for k in range(3):
            if k == 0: tab_res[l][k] /= total_yes
            if k == 1: tab_res[l][k] /= total_no
            if k == 2: tab_res[l][k] /= total_yes + total_no
    print(tab_res)

play = (gss['PlayTennis'])
yes=number(play,"No")
print(yes)
temp=(gss['Temperature'])
temperature(temp)
hum=(gss['Humidity'])
w=(gss['Windy'])
humidity(hum)
#wind(w)

def nb_yon(A,o,b):
    p=0
    total_yes=0
    total_no=0
    play=(gss['PlayTennis'])
    for i in A:
        p+=1
        if i == o:
            if yon(play,p) == "Yes":
                total_yes+=1
            else :
                total_no+=1
    if b=="Yes":
        return total_yes/number(play,"t_yes")
    else:
        return total_no / number(play, "t_no")

def t_x(A,nom):
    c=0
    for i in A :
        if i == nom:
            c+=1
    return c/len(A)

def prob(o,t,h,w):
    yes = number(gss['PlayTennis'], "Yes")
    no = number(gss['PlayTennis'], "No")
    out = (gss['Outlook'])
    temp = (gss['Temperature'])
    hum = (gss['Humidity'])
    win = (gss['Windy'])
    p_yes= nb_yon(out,o,"Yes")*nb_yon(temp,t,"Yes")*nb_yon(hum,h,"Yes")*nb_yon(win,w,"Yes")*yes
    p_no=nb_yon(out,o,"No")*nb_yon(temp,t,"No")*nb_yon(hum,h,"No")*nb_yon(win,w,"No")*no
    p_x=t_x(out,o)*t_x(hum,h)*t_x(temp,t)*t_x(win,w)
    px_yes=p_yes/p_x
    px_no=p_no/p_x
    if px_yes>px_no:
        print("Oui, vous pouvez jouer au tennis.")
        return px_yes
    else :
        print("Non, vous ne pouvez pas jouer au tennis.")
        return px_no

ol=input("Quel temps fait-il (Sunny ,Overcast,Rain) ? ")
Tmpt=input("Quelle température fait-il (Hot, Mild, Cool)? ")
H=input("Quelle est l'humidité (High , Normal) ? ")
W=input("Quelle est la vitesse du vent (TRUE, FALSE) ? ")

probabilite=prob(ol,Tmpt,H,W)
print(probabilite)
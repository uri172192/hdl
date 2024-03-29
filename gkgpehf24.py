import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd
from math import pi

st.set_page_config(page_title="GK EHF DATA", page_icon="favicon-32x32.png", layout="wide")


#st.markdown("<h1 style='text-align: center;'>Goalkeeper EHF Champions League Data -- Group Phase</h1>", unsafe_allow_html=True)
st.title("🥅 Goalkeeper EHF Champions League Data 🤾🏿‍♂️")
left_co, cent_co, right_co = st.columns(3)
with left_co:
    st.subheader("📋 Group Phase 23/24 📋")
with cent_co:
    image = Image.open('logohdl.png')
    st.image(image)

df = pd.read_excel("dfgkgp.xlsx")

# Crear el expander
expander = st.expander("➕ **EHF GK TEAMS DATA CONSULTORY** 🥅🤾🏿‍♂")

# Dentro del expander, agregar el código para seleccionar un jugador
with expander:
    gkteam = st.selectbox('Select your team:',
                        (df['Team']),
                        index=None,
                        placeholder="Select EHF team...")
    #st.write('EHF Team selected:', gkteam)

    # Filtrar el DataFrame según el equipo seleccionado
    equipo_df = df[df['Team'] == gkteam]

    # Mostrar el DataFrame filtrado si se seleccionó un equipo
    if not equipo_df.empty:
        #st.write(f'GK Data EHF Team Selected: {gkteam}:')
        #st.write(equipo_df)
        # Redondear los valores a 2 decimales
        equipo_df_rounded = equipo_df.round(2)
        
        st.write(equipo_df_rounded)
    
    else:
        st.warning('Please, select an EHF team.')



# Crear el expander
expander = st.expander("➕ **EHF GK INDIVIDUAL DATA CONSULTORY** 🥅🤾🏻‍♂️")

# Dentro del expander, agregar el código para seleccionar un jugador
with expander:
    gk = st.selectbox('Select EHF GK:', 
                      (df['Name']), 
                      index=None, 
                      placeholder='Type GK name...')
    gk_selected = df[df['Name'] == gk]

    if not gk_selected.empty:
        #st.write(f'GK Data EHF Team {gk}:')
        #st.write(gk_selected)
        # Redondear los valores a 2 decimales
        gk_selected_rounded = gk_selected.round(2)
        
        #st.write(f'GK Data EHF Team {gk}:')
        st.write(gk_selected_rounded)
    else:
        st.warning('Please, write a GK Name.')

 
# Set data
df = pd.DataFrame({
'group': ['A','B','C','D'],
'var1': [38, 1.5, 30, 4],
'var2': [29, 10, 9, 34],
'var3': [8, 39, 23, 24],
'var4': [7, 31, 33, 14],
'var5': [28, 15, 32, 14]
})
 
# ------- PART 1: Create background
 
# number of variable
categories=list(df)[1:]
N = len(categories)
 
# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
 
# Initialise the spider plot
ax = plt.subplot(111, polar=True)
 
# If you want the first axis to be on top:
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)
 
# Draw one axe per variable + add labels
plt.xticks(angles[:-1], categories)
 
# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks([10,20,30], ["10","20","30"], color="grey", size=7)
plt.ylim(0,40)
 

# ------- PART 2: Add plots
 
# Plot each individual = each line of the data
# I don't make a loop, because plotting more than 3 groups makes the chart unreadable
 
# Ind1
values=df.loc[0].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="group A")
ax.fill(angles, values, 'b', alpha=0.1)
 
# Ind2
values=df.loc[1].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="group B")
ax.fill(angles, values, 'r', alpha=0.1)
 
# Add legend
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

# Show the graph
plt.show()



# Mostrar el DataFrame completo + Search Bar:
# Redondear los valores a 2 decimales
df_rounded = df.round(2)
st.write('🗃️**EHF 23/24 Group Phase GK Data:**', df_rounded)


image = Image.open('logohdl.png')

st.caption("🔎Source: EHF")
expander = st.expander(" ➕ **LEGEND**")
expander.write("**SA%** = Saves %")
expander.write("**GC** = Goals Conceded")
expander.write("**NºMSA** = Number of Saves made by X distance")
expander.write("**NºMSO** = Number of Shots received by X distance")
expander.write("**WSA** = Number of saves made from wing shots")
expander.write("**WSO** = Number of wing shots received")


#with right_co:
    #image1 = Image.open('ehflogo.png')
    #st.image(image1)
    

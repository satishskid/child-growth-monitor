# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# # Load your datasets (ensure these are available in your environment)
# height_df_girl = pd.read_excel('height_df_girl.xlsx')
# bmi_df_girl = pd.read_excel('bmi_df_girl.xlsx')
# weight_df_girl = pd.read_excel('weight_df_girl.xlsx')
# height_df_boy = pd.read_excel('height_df_boy.xlsx')
# bmi_df_boy = pd.read_excel('bmi_df_boy.xlsx')
# weight_df_boy = pd.read_excel('weight_df_boy.xlsx')

# # Load growth standards for boys
# bh = pd.read_excel("HFA_Boys.xlsx")
# bh['age'] = bh['Month']
# bh = bh.drop("Month", axis=1)

# bh_girls = pd.read_excel("HFA_Girls.xlsx")
# bh_girls['age'] = bh_girls['Month']
# bh_girls = bh_girls.drop("Month", axis=1)

# # Set up the Streamlit app
# st.title("Child Growth Analysis")

# # Show the datasets


# st.header("Height Data - Boys")
# st.dataframe(height_df_boy)


# # Plot growth standards and height for boys
# st.header("Height for Age - Boys")
# plt.figure(figsize=(10, 6))
# plt.plot(bh['age'], bh['SD4neg'], label='-4 SD', color='blue', linestyle='--')
# plt.plot(bh['age'], bh['SD3neg'], label='-3 SD', color='cyan', linestyle='--')
# plt.plot(bh['age'], bh['SD2neg'], label='-2 SD', color='green', linestyle='--')
# plt.plot(bh['age'], bh['SD1neg'], label='-1 SD', color='lime', linestyle='--')
# plt.plot(bh['age'], bh['SD0'], label='Median', color='black', linestyle='-')
# plt.plot(bh['age'], bh['SD1'], label='+1 SD', color='orange', linestyle='--')
# plt.plot(bh['age'], bh['SD2'], label='+2 SD', color='red', linestyle='--')
# plt.plot(bh['age'], bh['SD3'], label='+3 SD', color='magenta', linestyle='--')
# plt.plot(bh['age'], bh['SD4'], label='+4 SD', color='purple', linestyle='--')

# # Scatter plot for boys' height data
# plt.scatter(height_df_boy['age'], height_df_boy['height'], color='red', label='Height for Boys', marker='*', s=100)

# plt.xlabel("Age of boys")
# plt.ylabel("Z-scores")
# plt.title("Height for Age - Boys")
# plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
# plt.grid(True)

# # Render the plot in Streamlit
# st.pyplot(plt)


# st.header("Height Data - Girls")
# st.dataframe(height_df_girl)



# # Plot growth standards and height for girls
# st.header("Height for Age - Girls")
# plt.figure(figsize=(10, 6))
# plt.plot(bh_girls['age'], bh_girls['SD4neg'], label='-4 SD', color='blue', linestyle='--')
# plt.plot(bh_girls['age'], bh_girls['SD3neg'], label='-3 SD', color='cyan', linestyle='--')
# plt.plot(bh_girls['age'], bh_girls['SD2neg'], label='-2 SD', color='green', linestyle='--')
# plt.plot(bh_girls['age'], bh_girls['SD1neg'], label='-1 SD', color='lime', linestyle='--')
# plt.plot(bh_girls['age'], bh_girls['SD0'], label='Median', color='black', linestyle='-')
# plt.plot(bh_girls['age'], bh_girls['SD1'], label='+1 SD', color='orange', linestyle='--')
# plt.plot(bh_girls['age'], bh_girls['SD2'], label='+2 SD', color='red', linestyle='--')
# plt.plot(bh_girls['age'], bh_girls['SD3'], label='+3 SD', color='magenta', linestyle='--')
# plt.plot(bh_girls['age'], bh_girls['SD4'], label='+4 SD', color='purple', linestyle='--')

# # Scatter plot for girls' height data
# plt.scatter(height_df_girl['age'], height_df_girl['height'], color='pink', label='Height for Girls', marker='*', s=100)

# plt.xlabel("Age of girls")
# plt.ylabel("Z-scores")
# plt.title("Height for Age - Girls")
# plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
# plt.grid(True)

# # Render the plot in Streamlit
# st.pyplot(plt)

# # Load the datasets
# weight_df_boy = pd.read_excel('weight_df_boy.xlsx')  # Boys' weight data
# bw_boys = pd.read_excel('WFA_Boys.xlsx')  # Weight-for-Age standards for boys

# # Preprocessing growth standards
# bw_boys['age'] = bw_boys['Month']
# bw_boys = bw_boys.drop("Month", axis=1)

# # Set up the Streamlit app
# st.title("Weight for Age - Boys")

# # Show the dataset
# st.header("Weight Data - Boys")
# st.dataframe(weight_df_boy)

# # Plot weight-for-age standards and boys' weight data
# st.header("Weight for Age - Boys Visualization")
# plt.figure(figsize=(10, 6))

# # Plot the standard deviation bands
# plt.plot(bw_boys['age'], bw_boys['SD4neg'], label='-4 SD', color='blue', linestyle='--')
# plt.plot(bw_boys['age'], bw_boys['SD3neg'], label='-3 SD', color='cyan', linestyle='--')
# plt.plot(bw_boys['age'], bw_boys['SD2neg'], label='-2 SD', color='green', linestyle='--')
# plt.plot(bw_boys['age'], bw_boys['SD1neg'], label='-1 SD', color='lime', linestyle='--')
# plt.plot(bw_boys['age'], bw_boys['SD0'], label='Median', color='black', linestyle='-')
# plt.plot(bw_boys['age'], bw_boys['SD1'], label='+1 SD', color='orange', linestyle='--')
# plt.plot(bw_boys['age'], bw_boys['SD2'], label='+2 SD', color='red', linestyle='--')
# plt.plot(bw_boys['age'], bw_boys['SD3'], label='+3 SD', color='magenta', linestyle='--')
# plt.plot(bw_boys['age'], bw_boys['SD4'], label='+4 SD', color='purple', linestyle='--')

# # Scatter plot for boys' weight data
# plt.scatter(weight_df_boy['age'], weight_df_boy['weight'], color='brown', label='Weight for Boys', marker='o', s=100)

# # Set plot labels and title
# plt.xlabel("Age of Boys (Months)")
# plt.ylabel("Weight (kg)")
# plt.title("Weight for Age - Boys")
# plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
# plt.grid(True)

# # Render the plot in Streamlit
# st.pyplot(plt)

# weight_df_girl = pd.read_excel('weight_df_girl.xlsx')  # Girls' weight data
# bw_girls = pd.read_excel('WFA_Girls.xlsx')  # Weight-for-Age standards for girls

# # Preprocessing growth standards
# bw_girls['age'] = bw_girls['Month']
# bw_girls = bw_girls.drop("Month", axis=1)

# # Set up the Streamlit app
# st.title("Weight for Age - Girls")

# # Show the dataset
# st.header("Weight Data - Girls")
# st.dataframe(weight_df_girl)

# # Plot weight-for-age standards and girls' weight data
# st.header("Weight for Age - Girls Visualization")
# plt.figure(figsize=(10, 6))

# # Plot the standard deviation bands
# plt.plot(bw_girls['age'], bw_girls['SD4neg'], label='-4 SD', color='blue', linestyle='--')
# plt.plot(bw_girls['age'], bw_girls['SD3neg'], label='-3 SD', color='cyan', linestyle='--')
# plt.plot(bw_girls['age'], bw_girls['SD2neg'], label='-2 SD', color='green', linestyle='--')
# plt.plot(bw_girls['age'], bw_girls['SD1neg'], label='-1 SD', color='lime', linestyle='--')
# plt.plot(bw_girls['age'], bw_girls['SD0'], label='Median', color='black', linestyle='-')
# plt.plot(bw_girls['age'], bw_girls['SD1'], label='+1 SD', color='orange', linestyle='--')
# plt.plot(bw_girls['age'], bw_girls['SD2'], label='+2 SD', color='red', linestyle='--')
# plt.plot(bw_girls['age'], bw_girls['SD3'], label='+3 SD', color='magenta', linestyle='--')
# plt.plot(bw_girls['age'], bw_girls['SD4'], label='+4 SD', color='purple', linestyle='--')

# # Scatter plot for girls' weight data
# plt.scatter(weight_df_girl['age'], weight_df_girl['weight'], color='brown', label='Weight for Girls', marker='o', s=100)

# # Set plot labels and title
# plt.xlabel("Age of Girls (Months)")
# plt.ylabel("Weight (kg)")
# plt.title("Weight for Age - Girls")
# plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
# plt.grid(True)

# # Render the plot in Streamlit
# st.pyplot(plt)


# bmi_df_girl = pd.read_excel('bmi_df_girl.xlsx')  # Girls' BMI data
# bmi_girls = pd.read_excel('BFA_Girls.xlsx')  # BMI-for-Age standards for girls

# # Preprocessing growth standards
# bmi_girls['age'] = bmi_girls['Month']
# bmi_girls = bmi_girls.drop("Month", axis=1)

# # Set up the Streamlit app
# st.title("BMI for Age - Girls")

# # Show the dataset
# st.header("BMI Data - Girls")
# st.dataframe(bmi_df_girl)

# # Plot BMI-for-age standards and girls' BMI data
# st.header("BMI for Age - Girls Visualization")
# plt.figure(figsize=(10, 6))

# # Plot the standard deviation bands
# plt.plot(bmi_girls['age'], bmi_girls['SD4neg'], label='-4 SD', color='blue', linestyle='--')
# plt.plot(bmi_girls['age'], bmi_girls['SD3neg'], label='-3 SD', color='cyan', linestyle='--')
# plt.plot(bmi_girls['age'], bmi_girls['SD2neg'], label='-2 SD', color='green', linestyle='--')
# plt.plot(bmi_girls['age'], bmi_girls['SD1neg'], label='-1 SD', color='lime', linestyle='--')
# plt.plot(bmi_girls['age'], bmi_girls['SD0'], label='Median', color='black', linestyle='-')
# plt.plot(bmi_girls['age'], bmi_girls['SD1'], label='+1 SD', color='orange', linestyle='--')
# plt.plot(bmi_girls['age'], bmi_girls['SD2'], label='+2 SD', color='red', linestyle='--')
# plt.plot(bmi_girls['age'], bmi_girls['SD3'], label='+3 SD', color='magenta', linestyle='--')
# plt.plot(bmi_girls['age'], bmi_girls['SD4'], label='+4 SD', color='purple', linestyle='--')

# # Scatter plot for girls' BMI data
# plt.scatter(bmi_df_girl['age'], bmi_df_girl['BMI'], color='brown', label='BMI for Girls', marker='o', s=100)

# # Set plot labels and title
# plt.xlabel("Age of Girls (Months)")
# plt.ylabel("BMI (kg/m²)")
# plt.title("BMI for Age - Girls")
# plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
# plt.grid(True)

# # Render the plot in Streamlit
# st.pyplot(plt)
# bmi_df_boy = pd.read_excel('bmi_df_boy.xlsx')  # Boys' BMI data
# bmi_boys = pd.read_excel('BFA_Boys.xlsx')  # BMI-for-Age standards for boys

# # Preprocessing growth standards
# bmi_boys['age'] = bmi_boys['Month']
# bmi_boys = bmi_boys.drop("Month", axis=1)

# # Set up the Streamlit app
# st.title("BMI for Age - Boys")

# # Show the dataset
# st.header("BMI Data - Boys")
# st.dataframe(bmi_df_boy)

# # Plot BMI-for-age standards and boys' BMI data
# st.header("BMI for Age - Boys Visualization")
# plt.figure(figsize=(10, 6))

# # Plot the standard deviation bands
# plt.plot(bmi_boys['age'], bmi_boys['SD4neg'], label='-4 SD', color='blue', linestyle='--')
# plt.plot(bmi_boys['age'], bmi_boys['SD3neg'], label='-3 SD', color='cyan', linestyle='--')
# plt.plot(bmi_boys['age'], bmi_boys['SD2neg'], label='-2 SD', color='green', linestyle='--')
# plt.plot(bmi_boys['age'], bmi_boys['SD1neg'], label='-1 SD', color='lime', linestyle='--')
# plt.plot(bmi_boys['age'], bmi_boys['SD0'], label='Median', color='black', linestyle='-')
# plt.plot(bmi_boys['age'], bmi_boys['SD1'], label='+1 SD', color='orange', linestyle='--')
# plt.plot(bmi_boys['age'], bmi_boys['SD2'], label='+2 SD', color='red', linestyle='--')
# plt.plot(bmi_boys['age'], bmi_boys['SD3'], label='+3 SD', color='magenta', linestyle='--')
# plt.plot(bmi_boys['age'], bmi_boys['SD4'], label='+4 SD', color='purple', linestyle='--')

# # Scatter plot for boys' BMI data
# plt.scatter(bmi_df_boy['age'], bmi_df_boy['BMI'], color='brown', label='BMI for Boys', marker='o', s=100)

# # Set plot labels and title
# plt.xlabel("Age of Boys (Months)")
# plt.ylabel("BMI (kg/m²)")
# plt.title("BMI for Age - Boys")
# plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
# plt.grid(True)

# # Render the plot in Streamlit
# st.pyplot(plt)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load your datasets
height_df_girl = pd.read_excel('height_df_girl.xlsx')
bmi_df_girl = pd.read_excel('bmi_df_girl.xlsx')
weight_df_girl = pd.read_excel('weight_df_girl.xlsx')
height_df_boy = pd.read_excel('height_df_boy.xlsx')
bmi_df_boy = pd.read_excel('bmi_df_boy.xlsx')
weight_df_boy = pd.read_excel('weight_df_boy.xlsx')

# Load growth standards for boys and girls
bh_boys = pd.read_excel("HFA_Boys.xlsx")
bh_boys['age'] = bh_boys['Month']
bh_boys = bh_boys.drop("Month", axis=1)

bh_girls = pd.read_excel("HFA_Girls.xlsx")
bh_girls['age'] = bh_girls['Month']
bh_girls = bh_girls.drop("Month", axis=1)

bw_boys = pd.read_excel('WFA_Boys.xlsx')
bw_boys['age'] = bw_boys['Month']
bw_boys = bw_boys.drop("Month", axis=1)

bw_girls = pd.read_excel('WFA_Girls.xlsx')
bw_girls['age'] = bw_girls['Month']
bw_girls = bw_girls.drop("Month", axis=1)

bmi_boys = pd.read_excel('BFA_Boys.xlsx')
bmi_boys['age'] = bmi_boys['Month']
bmi_boys = bmi_boys.drop("Month", axis=1)

bmi_girls = pd.read_excel('BFA_Girls.xlsx')
bmi_girls['age'] = bmi_girls['Month']
bmi_girls = bmi_girls.drop("Month", axis=1)

# Set up the Streamlit app
st.title("Child Growth Analysis")

# Boys' height visualization
st.header("Height Data - Boys")
st.dataframe(height_df_boy)

st.header("Height for Age - Boys")
plt.figure(figsize=(10, 6))
for sd, color in zip(['SD4neg', 'SD3neg', 'SD2neg', 'SD1neg', 'SD0', 'SD1', 'SD2', 'SD3', 'SD4'], 
                     ['blue', 'cyan', 'green', 'lime', 'black', 'orange', 'red', 'magenta', 'purple']):
    plt.plot(bh_boys['age'], bh_boys[sd], label=f'{sd} SD', color=color, linestyle='--')

plt.scatter(height_df_boy['age'], height_df_boy['height'], color='red', label='Height for Boys', marker='*', s=100)
plt.xlabel("Age of Boys (Months)")
plt.ylabel("Z-scores")
plt.title("Height for Age - Boys")
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(True)
st.pyplot(plt)

# Girls' height visualization
st.header("Height Data - Girls")
st.dataframe(height_df_girl)

st.header("Height for Age - Girls")
plt.figure(figsize=(10, 6))
for sd, color in zip(['SD4neg', 'SD3neg', 'SD2neg', 'SD1neg', 'SD0', 'SD1', 'SD2', 'SD3', 'SD4'], 
                     ['blue', 'cyan', 'green', 'lime', 'black', 'orange', 'red', 'magenta', 'purple']):
    plt.plot(bh_girls['age'], bh_girls[sd], label=f'{sd} SD', color=color, linestyle='--')

plt.scatter(height_df_girl['age'], height_df_girl['height'], color='pink', label='Height for Girls', marker='*', s=100)
plt.xlabel("Age of Girls (Months)")
plt.ylabel("Z-scores")
plt.title("Height for Age - Girls")
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(True)
st.pyplot(plt)

# Boys' weight visualization
st.header("Weight Data - Boys")
st.dataframe(weight_df_boy)

st.header("Weight for Age - Boys Visualization")
plt.figure(figsize=(10, 6))
for sd, color in zip(['SD4neg', 'SD3neg', 'SD2neg', 'SD1neg', 'SD0', 'SD1', 'SD2', 'SD3', 'SD4'], 
                     ['blue', 'cyan', 'green', 'lime', 'black', 'orange', 'red', 'magenta', 'purple']):
    plt.plot(bw_boys['age'], bw_boys[sd], label=f'{sd} SD', color=color, linestyle='--')

plt.scatter(weight_df_boy['age'], weight_df_boy['weight'], color='brown', label='Weight for Boys', marker='o', s=100)
plt.xlabel("Age of Boys (Months)")
plt.ylabel("Weight (kg)")
plt.title("Weight for Age - Boys")
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(True)
st.pyplot(plt)

# Girls' weight visualization
st.header("Weight Data - Girls")
st.dataframe(weight_df_girl)

st.header("Weight for Age - Girls Visualization")
plt.figure(figsize=(10, 6))
for sd, color in zip(['SD4neg', 'SD3neg', 'SD2neg', 'SD1neg', 'SD0', 'SD1', 'SD2', 'SD3', 'SD4'], 
                     ['blue', 'cyan', 'green', 'lime', 'black', 'orange', 'red', 'magenta', 'purple']):
    plt.plot(bw_girls['age'], bw_girls[sd], label=f'{sd} SD', color=color, linestyle='--')

plt.scatter(weight_df_girl['age'], weight_df_girl['weight'], color='brown', label='Weight for Girls', marker='o', s=100)
plt.xlabel("Age of Girls (Months)")
plt.ylabel("Weight (kg)")
plt.title("Weight for Age - Girls")
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(True)
st.pyplot(plt)

# Boys' BMI visualization
st.header("BMI Data - Boys")
st.dataframe(bmi_df_boy)

st.header("BMI for Age - Boys Visualization")
plt.figure(figsize=(10, 6))
for sd, color in zip(['SD4neg', 'SD3neg', 'SD2neg', 'SD1neg', 'SD0', 'SD1', 'SD2', 'SD3', 'SD4'], 
                     ['blue', 'cyan', 'green', 'lime', 'black', 'orange', 'red', 'magenta', 'purple']):
    plt.plot(bmi_boys['age'], bmi_boys[sd], label=f'{sd} SD', color=color, linestyle='--')

plt.scatter(bmi_df_boy['age'], bmi_df_boy['BMI'], color='brown', label='BMI for Boys', marker='o', s=100)
plt.xlabel("Age of Boys (Months)")
plt.ylabel("BMI (kg/m²)")
plt.title("BMI for Age - Boys")
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(True)
st.pyplot(plt)

# Girls' BMI visualization
st.header("BMI Data - Girls")
st.dataframe(bmi_df_girl)

st.header("BMI for Age - Girls Visualization")
plt.figure(figsize=(10, 6))
for sd, color in zip(['SD4neg', 'SD3neg', 'SD2neg', 'SD1neg', 'SD0', 'SD1', 'SD2', 'SD3', 'SD4'], 
                     ['blue', 'cyan', 'green', 'lime', 'black', 'orange', 'red', 'magenta', 'purple']):
    plt.plot(bmi_girls['age'], bmi_girls[sd], label=f'{sd} SD', color=color, linestyle='--')

plt.scatter(bmi_df_girl['age'], bmi_df_girl['BMI'], color='brown', label='BMI for Girls', marker='o', s=100)
plt.xlabel("Age of Girls (Months)")
plt.ylabel("BMI (kg/m²)")
plt.title("BMI for Age - Girls")
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(True)
st.pyplot(plt)

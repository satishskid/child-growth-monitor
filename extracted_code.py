import pandas as pd
import json
import requests

def find(df_boy,df_girl):
    bh = pd.read_excel("HFA_Boys.xlsx")
    bh['age']= bh['Month']
    bh = bh.drop("Month",axis = 1)
    print(bh)

    print(df_boy)

    height_df_boy = pd.DataFrame()
    height_df_boy['age'] = df_boy['age']
    height_df_boy['id'] = df_boy['id']
    height_df_boy['height'] = df_boy['height']
    merged_bh = pd.merge(height_df_boy, bh, left_on='age', right_on='age', how='left')
    merged_bh.set_index(df_boy.index, inplace=True)
    # print(merged_bh)
    # Calculate L * M * S and create a new column in df_boy
    merged_bh['HZ'] = ((merged_bh['height']/merged_bh['M'])**merged_bh['L'] -1)/(merged_bh['L'] * merged_bh['S'])
    # print(merged_df_boy)
    # print(merged_df_boy['HZ'])
    # Now you can use merged_df_boy to see the updated DataFrame
    height_df_boy = merged_bh

    # Show the updated df_boy with the new column
    print(height_df_boy)

    weight_df_boy = pd.DataFrame()
    weight_df_boy[['age','id','weight']] = df_boy[['age','id','weight']]
    print(weight_df_boy)

    bw = pd.read_excel("WFA_Boys.xlsx")
    bw['age']=bw['Month']
    bw = bw.drop('Month',axis=1)
    print(bw)

    merged_bw = pd.DataFrame()
    # print(merged_bw)
    merged_bw = pd.merge(weight_df_boy, bw, left_on='age', right_on='age', how='left')
    merged_bw.set_index(df_boy.index, inplace=True)
    # print(merged_bw)
    # Calculate L * M * S and create a new column in df_boy
    merged_bw['WZ'] = ((merged_bw['weight']/merged_bw['M'])**merged_bw['L'] -1)/(merged_bw['L'] * merged_bw['S'])
    # print(merged_df_boy)
    # print(merged_df_boy['WZ'])
    # Now you can use merged_df_boy to see the updated DataFrame
    weight_df_boy = merged_bw

    # Show the updated df_boy with the new column
    print(weight_df_boy)

    bb = pd.read_excel("BFA_Boys.xlsx")
    bb['age']=bb['Month']
    bb = bb.drop('Month',axis=1)
    print(bb)

    bmi_df_boy = pd.DataFrame()
    bmi_df_boy[['age','id','BMI']] = df_boy[['age','id','BMI']]
    print(bmi_df_boy)

    merged_bb = pd.DataFrame()
    # print(merged_bb)
    merged_bb = pd.merge(bmi_df_boy, bb, left_on='age', right_on='age', how='left')
    merged_bb.set_index(df_boy.index, inplace=True)
    # print(merged_bb)
    # Calculate L * M * S and create a new column in df_boy
    merged_bb['BZ'] = ((merged_bb['BMI']/merged_bb['M'])**merged_bb['L'] -1)/(merged_bb['L'] * merged_bb['S'])
    # print(merged_bb)
    # print(merged_bb['BZ'])
    # Now you can use merged_df_boy to see the updated DataFrame
    bmi_df_boy = merged_bb

    # Show the updated df_boy with the new column
    print(bmi_df_boy)

    ## for girls

    gh = pd.read_excel("HFA_girls.xlsx")
    gh['age']= gh['Month']
    gh = gh.drop("Month",axis = 1)
    print(gh)

    height_df_girl = pd.DataFrame()
    height_df_girl['age'] = df_girl['age']
    height_df_girl['id'] = df_girl['id']
    height_df_girl['height'] = df_girl['height']
    merged_gh = pd.merge(height_df_girl, gh, left_on='age', right_on='age', how='left')
    merged_gh.set_index(df_girl.index, inplace=True)
    # print(merged_gh)
    # Calculate L * M * S and create a new column in df_girl
    merged_gh['HZ'] = ((merged_gh['height']/merged_gh['M'])**merged_gh['L'] -1)/(merged_gh['L'] * merged_gh['S'])
    # print(merged_df_girl)
    # print(merged_df_girl['HZ'])
    # Now you can use merged_df_girl to see the updated DataFrame
    height_df_girl = merged_gh
    # Show the updated df_girl with the new column
    print(height_df_girl)

    weight_df_girl = pd.DataFrame()
    weight_df_girl[['age','id','weight']] = df_girl[['age','id','weight']]
    print(weight_df_girl)

    gw = pd.read_excel("WFA_girls.xlsx")
    gw['age']=gw['Month']
    gw = gw.drop('Month',axis=1)
    print(gw)

    merged_gw = pd.DataFrame()
    # print(merged_gw)
    merged_gw = pd.merge(weight_df_girl, gw, left_on='age', right_on='age', how='left')
    merged_gw.set_index(df_girl.index, inplace=True)
    # print(merged_gw)
    # Calculate L * M * S and create a new column in df_girl
    merged_gw['WZ'] = ((merged_gw['weight']/merged_gw['M'])**merged_gw['L'] -1)/(merged_gw['L'] * merged_gw['S'])
    # print(merged_df_girl)
    # print(merged_df_girl['WZ'])
    # Now you can use merged_df_girl to see the updated DataFrame
    weight_df_girl = merged_gw
    # Show the updated df_girl with the new column
    print(weight_df_girl)

    gb = pd.read_excel("BFA_girls.xlsx")
    gb['age']=gb['Month']
    gb = gb.drop('Month',axis=1)
    print(gb)

    bmi_df_girl = pd.DataFrame()
    bmi_df_girl[['age','id','BMI']] = df_girl[['age','id','BMI']]
    print(bmi_df_girl)

    merged_gb = pd.DataFrame()
    # print(merged_gb)
    merged_gb = pd.merge(bmi_df_girl, gb, left_on='age', right_on='age', how='left')
    merged_gb.set_index(df_girl.index, inplace=True)
    # print(merged_gb)
    # Calculate L * M * S and create a new column in df_girl
    merged_gb['BZ'] = ((merged_gb['BMI']/merged_gb['M'])**merged_gb['L'] -1)/(merged_gb['L'] * merged_gb['S'])
    # print(merged_gb)
    # print(merged_gb['BZ'])
    # Now you can use merged_df_girl to see the updated DataFrame
    bmi_df_girl = merged_gb
    # Show the updated df_girl with the new column

    print(height_df_girl)
    print(bmi_df_girl)
    print(weight_df_girl)

    print(height_df_boy)
    print(bmi_df_boy)
    print(weight_df_boy)

    height_df_girl.to_excel('height_df_girl.xlsx', index=True, index_label='Name')
    bmi_df_girl.to_excel('bmi_df_girl.xlsx', index=True, index_label='Name')
    weight_df_girl.to_excel('weight_df_girl.xlsx', index=True, index_label='Name')
    height_df_boy.to_excel('height_df_boy.xlsx', index=True, index_label='Name')
    bmi_df_boy.to_excel('bmi_df_boy.xlsx', index=True, index_label='Name')
    weight_df_boy.to_excel('weight_df_boy.xlsx', index=True, index_label='Name')


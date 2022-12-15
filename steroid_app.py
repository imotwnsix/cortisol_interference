import streamlit as st
import math
import datetime

st.title("藥物濃度計算器")
st.write("""皮質素(cortisol)的檢驗多為免疫分析法。
在服用外源性類固醇的情況下，可能因為交叉反應導致 cortisol 的結果假性偏高。
以現行檢驗技術而言，檢驗誤差一般而言不至於影響醫療絕測。
然而，針對本計算器用來粗估使用口服皮質醇，對於血液 cortisol 的干擾程度。""")

st.write("""在本計算器中，口服藥物使用one compartment model, first order kinetic作為預測模型。
plasma cortisol 的檢驗使用 The Elecsys Cortisol II assay 作為參考。
在此試劑中，交叉反應較明顯的藥物為 prednisolone 和 methylpredisolone。
注意到，交叉反應的程度因為試劑不同，不得直接轉換。""")

st.write("""本計算器之藥物動力學參數參考：""")
st.write("""Czock, D et al, (2005). Pharmacokinetics and pharmacodynamics of systemically administered glucocorticoids. Clinical pharmacokinetics, 44(1), 61-98.
""")        


# 參數區塊
drug = st.selectbox("請選擇使用類固醇", ["Prednisolone (PO)", "Methylprednisolone (PO)"])
dose = st.number_input("請輸入服用劑量 (mg)：")
t_draw = st.time_input("請輸入採血時間：", datetime.time(8,0))
administration = st.selectbox("請選擇給藥頻次：", ["single dose", "QD", "BID", "TID"])
if administration == "single dose":
    t_medicine = [st.time_input("請輸入服藥時間：", datetime.time(9,0) )]
else:
    time_trans = {"QD": [datetime.time(9,0)], 
                  "BID":[datetime.time(9,0), datetime.time(17,0)],
                  "TID":[datetime.time(9,0), datetime.time(13,0), datetime.time(17,0)]}
    t_medicine = time_trans[administration]

def hour_series(t_draw, t_med):
    series = []
    draw_minutes = t_draw.hour * 60 + t_draw.minute
    for t in t_med:
        med_minutes = t.hour * 60 + t.minute
        diff = (draw_minutes - med_minutes) % 1440
        diff = round(diff / 60, 1)
        series.append(diff)
    return series

def single_plasma_con(dos, t, ka, k, v_over_f): # in mg/L
    return dos * ka * (math.exp(-1 * k * t) - math.exp(-1 * ka * t)) / (ka-k) / v_over_f

def cross_reaction(dos, t, ka, k, v_over_f, cross_reactivity): # in mcg/dL
    return dos * ka * (math.exp(-1 * k * t) - math.exp(-1 * ka * t)) / (ka-k) / v_over_f * cross_reactivity

def pk(conc): # (ka, k, v_over_f, cross_reactivity)
    if drug == "Methylprednisolone (PO)":
        return (1.7, 0.27, 100, 14.70)
    elif conc <= 20:
        return (1.8, 0.28, 42, 7.32)
    elif conc <= 60:
        return (2.2, 0.25, 64, 7.32)
    else:
        return (2.2, 0.19, 98, 7.32)


def multi_con(series, pk_para, dos):
    c = 0
    for t in hour_series(t_draw, t_medicine):
        c = c + single_plasma_con(dos, t, *pk_para)
    return c

def multi_cross(series, pk_para, dos):
    c = 0
    for t in series:
        c = c + cross_reaction(dos, t, *pk_para)
    return c

series = hour_series(t_draw, t_medicine)

if st.button("確認"):
    st.write(f"藥物在血中的濃度預估為{ round(multi_con(series, pk(dose)[:-1], dose), 2) }")
    st.write(f"藥物造成的交叉反應預估為{ round(multi_cross(series, pk(dose), dose), 2) }")

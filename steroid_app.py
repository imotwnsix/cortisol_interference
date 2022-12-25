import streamlit as st
import math
import datetime
from streamlit_option_menu import option_menu

# sidebar menu
selected = option_menu(menu_title = None,
options = ["Calculator", "Background", "Limitation", "Reference"],
icons = ["calculator", "lightbulb", "exclamation-triangle", "file-earmark-text"],
orientation = "horizontal",
) 

# block "Calculator"
if selected == "Calculator":
  st.title("Cortisol Interference Calculator")
  st.write("## 皮質素干擾計算器")
  st.write("請輸入患者服用類固醇藥物的基本資訊，本計算器會預估藥物對 cortisol 檢驗的干擾程度。")

  # 參數區塊
  drug = st.selectbox("請選擇使用類固醇", ["Prednisolone (PO)"])
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
      if conc <= 20:
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


# block "Background"
if selected == "Background":
  st.title("Cortisol Interference Calculator")
  st.write("## 背景")
  st.write("""**本計算器用來評估類固醇藥物對於皮質素(cortisol)檢驗結果的干擾程度。**

Cortisol 的臨床檢驗多使用免疫分析法。
皮質素的結構與類固醇藥物結構類似，
因此，在服用類固醇藥物的情況下，可能因為交叉反應導致檢驗結果假性偏高。
以 Roche Elecsys Cortisol II Assay 為例，最容易產生干擾的藥物為 prednisolone 和 methylprednisolone。
檢驗干擾是否影響判讀與決策，隨臨床情境而異。
大致與藥物劑量、服用方法和病人原始cortisol濃度有關。

本計算器使用藥物動力學模型，推估藥物對血中 cortisol 的干擾程度。臨床醫師可以藉由計算結果，評估抽血結果的可信度。""")

# block "Limitation"
if selected == "Limitation":
  st.title("Cortisol Interference Calculator")
  st.write("## 限制")
  st.write("""正確地理解檢驗方法有助於正確的臨床解讀。

 1. 預測濃度不宜當作真值
    - 檢驗的交叉反應是由血液中藥物濃度得出。
    - 本計算器預估之交叉反應**不宜**用來推測真實的藥物與皮質素濃度。正確的理解，是**此濃度預估了檢驗項目的干擾程度**。使用者應綜合皮質素結果與臨床情境，決定檢驗數值之可信度。
    - 真正的血中藥物濃度仍應由直接檢驗測得，請用真正的直接測量
 2. 交叉反應參數隨試驗廠牌有所差異
    - 不同廠牌試劑因為設計之抗體不同，對於各物質有不同交叉反應。確切交叉反應應採用
    - 本計算器計算結果為 The Elecsys Cortisol II assay 的交叉反應(現今林口長庚紀念醫院採用廠牌)，**對於他牌皮質素檢驗僅能作為參考**。
 3. 類固醇藥物動力學可能隨濃度有差異
    - 本計算機中 prednisolone, methylprednisolone 之藥物動力學模型與參數隨著濃度不同有所差異。其中，Methylprednisolone在高劑量之脈衝療法(High-dose pulse therapy)下，藥物動力學模型異於一般典型劑量。
    - 本計算器尚未涵蓋脈衝療法下的交叉反應模型，因此，交叉反應的預測結果並不適用。但是，此類患者交叉反應預期非常顯著，**臨床人員應有所認知並避免在療程中進行檢驗**。""")

# block "Reference"
if selected == "Reference":
  st.title("Cortisol Interference Calculator")
  st.write("## 參考資料")
  st.write(""" 1. Czock, D et al, (2005). Pharmacokinetics and pharmacodynamics of systemically administered glucocorticoids. Clinical pharmacokinetics, 44(1), 61-98.
 2. Roche Diagnostics. Cortisol: Method Sheet. (https://pim-eservices.roche.com)""")

# pharmacokinetics
## background
本計算器用來評估

皮質素(cortisol)的檢驗多為免疫分析法。
在服用外源性類固醇的情況下，可能因為交叉反應導致 cortisol 的結果假性偏高。
以現行檢驗技術而言，檢驗誤差一般而言不至於影響醫療絕測。
然而，針對本計算器用來粗估使用口服皮質醇，對於血液 cortisol 的干擾程度。

在本計算器中，口服藥物使用one compartment model, first order kinetic作為預測模型。

## limitation
正確地理解檢驗方法有助於正確的臨床解讀。

 1. 預測濃度不宜當作真值
    - 檢驗的交叉反應是由血液中藥物濃度得出。
 2. 交叉反應參數隨試驗廠牌有所差異
 3. 類固醇藥物動力學可能隨濃度有差異

同一個檢驗項目的交叉反應會隨試劑廠牌有所差異，
檢驗方法
plasma cortisol 的檢驗使用 The Elecsys Cortisol II assay 作為參考。
在此試劑中，交叉反應較明顯的藥物為 prednisolone 和 methylpredisolone。
注意到交叉反應的程度因為試劑不同，不得直接轉換。

本計算器得出數值對於

## Reference
 1. Czock, D et al, (2005). Pharmacokinetics and pharmacodynamics of systemically administered glucocorticoids. Clinical pharmacokinetics, 44(1), 61-98.
 2. Roche Diagnostics. Cortisol: Method Sheet. [link](https://pim-eservices.roche.com)

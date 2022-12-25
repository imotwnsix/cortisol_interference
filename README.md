# pharmacokinetics
## Background
**本計算器用來評估類固醇藥物對於皮質素(cortisol)檢驗結果的干擾程度。**

Cortisol 的臨床檢驗多使用免疫分析法。
皮質素的結構與類固醇藥物結構類似，
因此，在服用類固醇藥物的情況下，可能因為交叉反應導致檢驗結果假性偏高。
以 Roche Elecsys Cortisol II Assay 為例，最容易產生干擾的藥物為 prednisolone 和 methylprednisolone。
檢驗干擾是否影響判讀與決策，隨臨床情境而異。
大致與藥物劑量、服用方法和病人原始cortisol濃度有關。

本計算器使用藥物動力學模型，推估藥物對血中 cortisol 的干擾程度。臨床醫師可以藉由計算結果，評估抽血結果的可信度。

## Limitation
正確地理解檢驗方法有助於正確的臨床解讀。

 1. 預測濃度不宜當作真值
    - 檢驗的交叉反應是由血液中藥物濃度得出。
    - 本計算器預估之交叉反應**不宜**用來推測真實的藥物與皮質素濃度。正確的理解，是**此濃度預估了檢驗項目的干擾程度**。使用者應綜合皮質素結果與臨床情境，決定檢驗數值之可信度。
    - 真正的血中藥物濃度仍應由直接檢驗測得，請用真正的直接測量
 2. 交叉反應參數隨試驗廠牌有所差異
    - 不同廠牌試劑因為設計之抗體不同，對於各物質有不同交叉反應。確切交叉反應應採用
    - 本計算器計算結果為 The Elecsys Cortisol II assay 的交叉反應(現今林口長庚紀念醫院採用廠牌)，**對於他牌皮質素檢驗僅能作為參考**。
 3. 類固醇藥物動力學可能隨濃度有差異
    - 本計算機中 prednisolone, methylprednisolone 之藥物動力學模型與參數隨著濃度不同有所差異。其中，Methylprednisolone在高劑量之脈衝療法(High-dose pulse therapy)下，藥物動力學模型異於一般典型劑量。
    - 本計算器尚未涵蓋脈衝療法下的交叉反應模型，因此，交叉反應的預測結果並不適用。但是，此類患者交叉反應預期非常顯著，**臨床人員應有所認知並避免在療程中進行檢驗**。

同一個檢驗項目的交叉反應會隨試劑廠牌有所差異，
檢驗方法
plasma cortisol 的檢驗使用 The Elecsys Cortisol II assay 作為參考。
在此試劑中，交叉反應較明顯的藥物為 prednisolone 和 methylpredisolone。
注意到交叉反應的程度因為試劑不同，不得直接轉換。

## Reference
 1. Czock, D et al, (2005). Pharmacokinetics and pharmacodynamics of systemically administered glucocorticoids. Clinical pharmacokinetics, 44(1), 61-98.
 2. Roche Diagnostics. Cortisol: Method Sheet. (https://pim-eservices.roche.com)

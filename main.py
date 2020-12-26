import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("Streamlit 超入門") #タイトル

st.write("DataFrame") #出力=print()のイメージ

#df = pd.DataFrame({
#    "1列目":[1, 2, 3, 4],
#    "2列目":[10, 20, 30, 40]
#})
#表にはデフォルトで並べ替え機能ついている＝動的な表

#st.write(df) #※表は.writeでも表示できるが.細かい設定できるdataframeをつかう
#st.dataframe(df.style.highlight_max(axis=0))
#.highlight_max(axis=0)とは列または行で最大のものをハイライト、axis=0なら列、1なら行

#.tableでは並び替えない静的な表を表示する
#st.table(df.style.highlight_max(axis=0))

#streamlitのリファレンスdisplaydataにより詳しく書いてある


##チャート作成
#df = pd.DataFrame(
#    np.random.rand(20,3),#縦20横3のランダムな行列
#    columns=["a", "b", "c"]#カラム名abcにした
#)
#st.line_chart(df) #折れ線グラフ作成
#st.area_chart(df) #エリアチャート 
#st.bar_chart(df) #棒チャート

"""
##マップ描画
df = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69, 139.70],#5050で割ると誤差少なく、139.70は新宿付近
    columns=["lat", "lon"]#緯度経度
)
st.map(df)

"""
"""
##画像表示
img = Image.open("19926751.jpg")
st.image(img, caption="angela", use_column_width=True)
#use_column_widthカラムの大きさに併せる
"""


""" #チェックボックスによるメディアの表示可否
if st.checkbox("show Image"): #checkboxはチェックされたかでTrueかFalseを返す
    img = Image.open("19926751.jpg")
    st.image(img, caption="angela", use_column_width=True) """


""" #セレクトボックス
option = st.selectbox(
    "あなたが好きな数字を教えてください、",
    list(range(1,11))
)
"あなたの好きな数字は", option , "です。" """


""" #テキスト入力
option = st.text_input("あなたの趣味を教えてください")
"あなたの趣味は", option, "です。" """


""" #スライダー
condition = st.slider("あなたの今の調子は？", 0, 100, 50) #最小値最大値スタート値
"コンディション:", condition """

##レイアウト

""" #サイドバー
option = st.sidebar.text_input("あなたの趣味を教えてください")
"あなたの趣味は", option, "です。"  """

""" #2カラムにする
left_column, right_column = st.beta_columns(2)#３カラムなら33
button = left_column.button("右カラムに文字を表示")
if button: #ボタンがtrueなら
    right_column.write("ここは右カラムです")

#エキスパンダー
expander1 = st.beta_expander("問い合わせ")
expander1.write("問い合わせ内容を核")
expander2 = st.beta_expander("問い合わせ")
expander2.write("問い合わせ内容を核")
expander3 = st.beta_expander("問い合わせ")
expander3.write("問い合わせ内容を核") """

#プログレスバー=メーターっぽいやつ）の表示
st.write("プログレスバーの表示")
"start"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}") #fストリングス、文字部分
    bar.progress(i + 1) #バー部分
    time.sleep(0.1) #バーが進む速さ調整

"DOne" #for文が終わったら表示
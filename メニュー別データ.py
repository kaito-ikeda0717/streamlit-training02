import streamlit as st
import pandas as pd
import altair as alt

def drink_kind():
    #エクセルデータの読み込み
    drink_data = pd.read_excel("./data/sales_data/2022sales_data.xlsx", sheet_name="drink",
                               engine="openpyxl", index_col=0)
    
    #行と列を逆にする
    transpose_drink_data = drink_data.T
    #カラムの作成
    col_1, col_2 = st.columns(2)
    with col_1:
        #ラジオボタン作成
        selected_drink = st.radio("メニューを選択してください",
                                 transpose_drink_data.columns.unique(),
                                 key="test9")
    with col_2:
        #データフレーム作成
        data = pd.DataFrame({
                        "営業月": transpose_drink_data.index.unique(),
                        "売上数": transpose_drink_data[selected_drink]
                        })
        st.subheader(selected_drink)
        #棒グラフの描画
        st.altair_chart(alt.Chart(data).mark_bar().encode(
            x=alt.X("営業月", sort=None),
            y="売上数",
            ),
            use_container_width=True)
        
    
if st.checkbox("ドリンク品別売上"):
    drink_kind()


def multiselect_drink():
    #タイトル
    st.markdown(" #### ドリンクメニュー売上数比較")
    #エクセルデータの読み込み
    drink_data = pd.read_excel("./data/sales_data/2022sales_data.xlsx", sheet_name="drink",
                            engine="openpyxl", index_col=0)

    #行と列を入れ替える
    transposed_drink_data = drink_data.T
    #マルチセレクトの作成
    multiselected_list = st.multiselect(
        "確認したいドリンクメニューを選んでください (複数選択可) ",
        transposed_drink_data.columns.unique(),
        "生大"
        )
    st.write(transposed_drink_data[multiselected_list])
    if not multiselected_list:
        st.error("表示するメニューが選択されていません。")
    else:
        st.line_chart(transposed_drink_data[multiselected_list])

if st.checkbox("ドリンク品別売上 (マルチセレクト)"):
    multiselect_drink()


def meat_kind():
    #エクセルデータの読み込み
    meat_data = pd.read_excel("./data/sales_data/2022sales_data.xlsx", sheet_name="meat",
                               engine="openpyxl", index_col=0)
    
    #行と列を逆にする
    transpose_meat_data = meat_data.T
    #カラムの作成
    col_1, col_2 = st.columns(2)
    with col_1:
        #ラジオボタン作成
        selected_meat = st.radio("メニューを選択してください",
                                 transpose_meat_data.columns.unique(),
                                 key="test10")
    with col_2:
        #データフレーム作成
        data = pd.DataFrame({
                        "営業月": transpose_meat_data.index.unique(),
                        "売上数": transpose_meat_data[selected_meat]
                        })
        st.subheader(selected_meat)
        #棒グラフの描画
        st.altair_chart(alt.Chart(data).mark_bar().encode(
            x=alt.X("営業月", sort=None),
            y="売上数",
            ),
            use_container_width=True)
        
    
if st.checkbox("肉類の品別売上"):
    meat_kind()


def multiselect_meat():
    #タイトル
    st.markdown(" #### 肉類メニュー売上数比較")
    #エクセルデータの読み込み
    meat_data = pd.read_excel("./data/sales_data/2022sales_data.xlsx", sheet_name="meat",
                            engine="openpyxl", index_col=0)

    #行と列を入れ替える
    transposed_meat_data = meat_data.T
    #マルチセレクトの作成
    multiselected_list = st.multiselect(
        "確認したい肉類メニューを選んでください (複数選択可) ",
        transposed_meat_data.columns.unique(),
        "トモサンカク"
        )
    st.write(transposed_meat_data[multiselected_list])
    if not multiselected_list:
        st.error("表示するメニューが選択されていません。")
    else:
        st.line_chart(transposed_meat_data[multiselected_list])

if st.checkbox("肉類品別売上 (マルチセレクト)"):
    multiselect_meat()


def sidemenu_kind():
    #エクセルデータの読み込み
    sidemenu_data = pd.read_excel("./data/sales_data/2022sales_data.xlsx", sheet_name="sidemenu",
                               engine="openpyxl", index_col=0)
    
    #行と列を逆にする
    transpose_sidemenu_data = sidemenu_data.T
    #カラムの作成
    col_1, col_2 = st.columns(2)
    with col_1:
        #ラジオボタン作成
        selected_sidemenu = st.radio("メニューを選択してください",
                                 transpose_sidemenu_data.columns.unique(),
                                 key="test11")
    with col_2:
        #データフレーム作成
        data = pd.DataFrame({
                        "営業月": transpose_sidemenu_data.index.unique(),
                        "売上数": transpose_sidemenu_data[selected_sidemenu]
                        })
        st.subheader(selected_sidemenu)
        #棒グラフの描画
        st.altair_chart(alt.Chart(data).mark_bar().encode(
            x=alt.X("営業月", sort=None),
            y="売上数",
            ),
            use_container_width=True)
        
    
if st.checkbox("サイドメニューの品別売上"):
    sidemenu_kind()


def multiselect_sidemenu():
    #タイトル
    st.markdown(" #### サイドメニュー売上数比較")
    #エクセルデータの読み込み
    sidemenu_data = pd.read_excel("./data/sales_data/2022sales_data.xlsx", sheet_name="sidemenu",
                            engine="openpyxl", index_col=0)

    #行と列を入れ替える
    transposed_sidemenu_data = sidemenu_data.T
    #マルチセレクトの作成
    multiselected_list = st.multiselect(
        "確認したいサイドメニューを選んでください (複数選択可) ",
        transposed_sidemenu_data.columns.unique(),
        []
        )
    st.write(transposed_sidemenu_data[multiselected_list])
    if not multiselected_list:
        st.error("表示するメニューが選択されていません。")
    else:
        st.line_chart(transposed_sidemenu_data[multiselected_list])

if st.checkbox("サイドメニュー品別売上 (マルチセレクト)"):
    multiselect_sidemenu()

#コメント
with st.form(key="sales_kind_comment"):
    #textbox
    comment = st.text_input("コメントを記入してください")
    submit_btn = st.form_submit_button("登録")
    if submit_btn: #ボタンをクリックしたらコメントを登録する
        with open("./data/sales_data/sales_kind_comment.txt", "a") as f:
            f.write(f"{comment}")
    with open("./data/sales_data/sales_kind_comment.txt", "r") as f:
        sales_comment = f.read()
        sales_comment

st.markdown(":red[今回は練習用にデータベースの代わりにtxtファイルを使用しています。]")
st.markdown(":red[また今回はコメント登録後の取り消し機能も実装していません。]")
st.markdown(":red[sales_kind_comment.txtを直接編集することは可能です。]")

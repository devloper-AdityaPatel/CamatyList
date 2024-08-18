import streamlit as st

import pandas as pd


# importing datetime module for now()
import datetime
 
# using now() to get current time
current_time = datetime.datetime.now()
link = f"https://docs.google.com/spreadsheets/d//edit?usp=sharing"
payment = 'PaymentDetails' # replace with your own sheet name
bid = 'BiddingDetails' # replace with your own sheet name
sheet_id = '1opM13tmLsWh-luEha3jGbkXxgIr-yD2k_RSLdb61r8s' # replace with your sheet's ID
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={payment}"
url1 = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={bid}"

st.title("AiQUA Softech Enterprise")
tabList = ["Home","About Camaty","Camaty Incharge Details"]
st.tabs(tabList)

st.markdown(" ")
st.markdown(" ")

st.markdown(":rainbow[Hola!]")
st.markdown("Welcome Members!")
st.markdown("Here you can get all The details about camaty related to past payments")
st.markdown("bidder winner etc.")

st.divider()
st.markdown("Net value : 112000/-")
st.markdown("Total members : 16")

#Website title
st.title("Camaty Details")
#camaty tables fetch
df = pd.read_csv(url)
df1 = pd.read_csv(url1)
df1 = df1.iloc[:,0:6]

#camaty tables placed
st.subheader("Payment Details",divider=True)
st.markdown("Previous months payment details are here.")
st.dataframe(df,hide_index=True,height=600)
st.subheader("Past Bidding Details",divider=True)
st.markdown("Previous months bidding details are here.")
st.dataframe(df1,hide_index=True,width=1000)
st.bar_chart(df1,x="bidder name",y="Net",x_label= "Bidder Name",y_label="Net amount")
st.text("Camaty Incharge : Sudhir Prasad")
st.text("Contact Number : +91 9821288621 , +91 9968111235")
st.markdown(":rainbow[*Devloped and Managed by : Aditya Patel*]")
st.caption(":rainbow[*e-mail : adityapatel.devloper@gmail.com   Phone : +91 9968111235*]")
st.caption(":violet[AiQUA Technologies]")

st.caption(current_time)

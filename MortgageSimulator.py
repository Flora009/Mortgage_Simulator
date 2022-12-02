# -*- coding: utf-8 -*-


import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import numpy_financial as npf

st.set_page_config(
    page_title="Mortgage Loan Simulator")

st.title("Mortgage Loan Simulator")

st.header("**Mortgage Details**")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Home Value")
    home_value = st.number_input("Enter your home value($): ", min_value=0.0, format='%f')
    
    st.subheader("Loan Interest Rate")
    interest_rate = st.number_input("Enter your home loan interest rate(%): ", min_value=0.0, format='%f')

with col2:
    st.subheader("Down Payment Percent")
    down_payment_percent = st.number_input("Enter your down payment percent(%): ", min_value=0.0, format='%f')
    
    st.subheader("Target Payment Period (Years)")
    payment_years = st.number_input("Enter your target payment period (years): ", min_value=3, format='%d')
    

down_payment = home_value* (down_payment_percent / 100)
loan_amount = home_value - down_payment
payment_months = payment_years*12
interest_rate = interest_rate / 100
periodic_interest_rate = (1+interest_rate)**(1/12) - 1
monthly_installment = -1*npf.pmt(periodic_interest_rate , payment_months, loan_amount)

st.subheader("**Down Payment:** $" + str(round(down_payment,2)))
st.subheader("**Loan Amount:** $" + str(round(loan_amount, 2)))
st.subheader("**Monthly Installment:** $" + str(round(monthly_installment, 2)))

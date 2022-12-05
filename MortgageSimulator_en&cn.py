# -*- coding: utf-8 -*-


import streamlit as st


import numpy as np
import numpy_financial as npf

st.set_page_config(
    page_title="Mortgage Loan Calculator|贷款计算器")

st.title("Mortgage Loan Simulator|贷款计算器")

st.header("**Mortgage Details|贷款详情**")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Home Value|房屋价值")
    home_value = st.number_input("Enter your home value($): |输入房屋价值", min_value=0.0, format='%f')
    
    st.subheader("Loan Interest Rate|房贷利率")
    interest_rate = st.number_input("Enter your home loan interest rate(%): |输入房贷利率", min_value=0.0, format='%f')

with col2:
    st.subheader("Down Payment Percent|首付比例")
    down_payment_percent = st.number_input("Enter your down payment percent(%):|输入首付比例 ", min_value=0.0, format='%f')
    
    st.subheader("Target Payment Period (Years)|贷款年限")
    payment_years = st.number_input("Enter your target payment period (years): |输入贷款年限", min_value=3, format='%d')
    

down_payment = home_value* (down_payment_percent / 100)
loan_amount = home_value - down_payment
payment_months = payment_years*12
interest_rate = interest_rate / 100
periodic_interest_rate = (1+interest_rate)**(1/12) - 1
monthly_installment = -1*npf.pmt(periodic_interest_rate , payment_months, loan_amount)

st.subheader("**Down Payment|首付金额:** $" + str(round(down_payment,2)))
st.subheader("**Loan Amount|贷款金额:** $" + str(round(loan_amount, 2)))
st.subheader("**Monthly Installment|每月还款金额:** $" + str(round(monthly_installment, 2)))

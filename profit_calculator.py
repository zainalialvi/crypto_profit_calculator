import streamlit as st

st.title('Crypto Profit Calculator by ZainAliAlvi 💰 ')

investment_amount = st.number_input('💵 Your investment amount', min_value=0.0, step=1.0)
initial_price = st.number_input('📉 Coin initial price (buy price)', min_value=0.0, step=0.1)
last_price = st.number_input('📈 Coin last price (sell price)', min_value=0.0, step=0.1)

if st.button('Calculate'):
    if initial_price > 0:
        coins_bought = investment_amount / initial_price
        total_earnings = coins_bought * last_price
        profit = total_earnings - investment_amount

        st.header(f"Total earnings: ${total_earnings:.4f}")
        st.header(f"Profit: ${profit:.4f}")
    else:
        st.error("The initial price must be greater than 0.")

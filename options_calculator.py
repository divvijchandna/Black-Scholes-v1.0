import streamlit as st
from black_scholes import BlackScholes

def app():
    st.title("Options Pricing Calculator")

    col1, col2 = st.columns(2)

    # Inputs
    with col1:
        stock_price = st.number_input("Spot Price", value=140.0)
        risk_free_interest_rate = st.number_input("Risk-Free Interest Rate", value=0.05)

    with col2:
        strike_price = st.number_input("Strike Price", value=150.0)
        volatility = st.number_input("Volatility (annual)", min_value=0.01, value=0.3)
        
    time_to_expiration = st.number_input("Time to Expiration (years)", value=0.5)

    # Create an instance of the Option class
    option = BlackScholes(stock_price, strike_price, risk_free_interest_rate, time_to_expiration, volatility)

    if st.button("Submit"):
        # Calculate and display the call and put option prices when the button is clicked
        call_price = option.call_option_price()
        put_price = option.put_option_price()

        col3, col4 = st.columns(2)
        with col3:
            st.warning(f"Call Option Price: {call_price:.2f}")
        with col4:
            st.info(f"Put Option Price: {put_price:.2f}")
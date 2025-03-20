import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from black_scholes import BlackScholes
import numpy as np

# Function to generate heatmaps
def generate_call_put_heatmaps(min_volatility, max_volatility, min_spot_price, max_spot_price, 
                               risk_free_interest_rate, strike_price, time_to_expiration):
    
    col3, col4 = st.columns(2)

    # Plot data points in the Spot Prices and Volatilities range
    spot_prices = np.linspace(min_spot_price, max_spot_price, 11)
    volatilities = np.linspace(min_volatility, max_volatility, 11)

    call_prices = np.zeros((len(volatilities), len(spot_prices)))
    put_prices = np.zeros((len(volatilities), len(spot_prices)))

    # Calculate all call and put prices to plot
    for i, vol in enumerate(volatilities):
        for j, spot in enumerate(spot_prices):
            option = BlackScholes(spot, strike_price, risk_free_interest_rate, time_to_expiration, vol)
            call_prices[i, j] = option.call_option_price()
            put_prices[i, j] = option.put_option_price()
    
    # Call Plot
    fig1, ax1 = plt.subplots(figsize=(8, 6))
    heatmap1 = sns.heatmap(call_prices, xticklabels=np.round(spot_prices, 2), yticklabels=np.round(volatilities, 2),
                           cmap="viridis", ax=ax1, cbar=True, annot=True, fmt=".2f", annot_kws={"size": 8})
    heatmap1.figure.axes[-1].tick_params(labelsize=8)
    ax1.tick_params(axis='x', labelsize=8, labelrotation=0)
    ax1.tick_params(axis='y', labelsize=8, labelrotation=0)
    ax1.set_title("Call Option Prices Heatmap")
    ax1.set_xlabel("Spot Price")
    ax1.set_ylabel("Volatility")

    # Put Plot
    fig2, ax2 = plt.subplots(figsize=(8, 6))
    heatmap2 = sns.heatmap(put_prices, xticklabels=np.round(spot_prices, 2), yticklabels=np.round(volatilities, 2),
                           cmap="viridis", ax=ax2, cbar=True, annot=True, fmt=".2f", annot_kws={"size": 8})
    heatmap2.figure.axes[-1].tick_params(labelsize=8)
    ax2.tick_params(axis='x', labelsize=8, labelrotation=0)
    ax2.tick_params(axis='y', labelsize=8, labelrotation=0)
    ax2.set_title("Put Option Prices Heatmap")
    ax2.set_xlabel("Spot Price")
    ax2.set_ylabel("Volatility")

    with col3:
        st.pyplot(fig1)

    with col4:
        st.pyplot(fig2)

# Function to generate profit/loss heatmaps
def generate_profit_loss_heatmaps( min_volatility, max_volatility, min_spot_price, max_spot_price, risk_free_interest_rate, 
                                  strike_price, time_to_expiration, purchase_price_call, purchase_price_put):
    
    col5, col6 = st.columns(2)

    # Generate Spot Prices and Volatilities
    spot_prices = np.linspace(min_spot_price, max_spot_price, 11)
    volatilities = np.linspace(min_volatility, max_volatility, 11)

    # Initialize matrices for profit/loss calculations
    call_profit_loss = np.zeros((len(volatilities), len(spot_prices)))
    put_profit_loss = np.zeros((len(volatilities), len(spot_prices)))

    # Calculate profit/loss for each combination of Spot Price and Volatility
    for i, vol in enumerate(volatilities):
        for j, spot in enumerate(spot_prices):

            option = BlackScholes(spot, strike_price, risk_free_interest_rate, time_to_expiration, vol)

            # For Call Option
            call_price = option.call_option_price()
            call_profit_loss[i, j] = max(purchase_price_call - strike_price - call_price, 0 - call_price)

            # For Put Option
            put_price = option.put_option_price()
            put_profit_loss[i, j] = max(strike_price - purchase_price_put - put_price, 0 - put_price)

    # def get_text_color(value):
    #     if value > 0:
    #         return "green"
    #     elif value < 0:
    #         return "red"
    #     else:
    #         return "white"

    # Call Profit/Loss Heatmap
    fig1, ax1 = plt.subplots(figsize=(8, 6))
    sns.heatmap(call_profit_loss, xticklabels=np.round(spot_prices, 2), yticklabels=np.round(volatilities, 2),
                cmap="coolwarm", ax=ax1, cbar=True, annot=True, fmt=".2f", annot_kws={"size": 8})
    
    # for i in range(call_profit_loss.shape[0]):
    #     for j in range(call_profit_loss.shape[1]):
    #         text_color = get_text_color(call_profit_loss[i, j])
    #         ax1.text(j + 0.5, i + 0.5, f"{call_profit_loss[i, j]:.2f}",
    #                  color=text_color, ha='center', va='center')

    ax1.set_title("Call Option Profit/Loss Heatmap")
    ax1.set_xlabel("Spot Price")
    ax1.set_ylabel("Volatility")

    # Put Profit/Loss Heatmap
    fig2, ax2 = plt.subplots(figsize=(8, 6))
    sns.heatmap(put_profit_loss, xticklabels=np.round(spot_prices, 2), yticklabels=np.round(volatilities, 2),
                cmap="coolwarm", ax=ax2, cbar=True, annot=True, fmt=".2f", annot_kws={"size": 8})

    # for i in range(put_profit_loss.shape[0]):
    #     for j in range(put_profit_loss.shape[1]):
    #         text_color = get_text_color(put_profit_loss[i, j])
    #         ax2.text(j + 0.5, i + 0.5, f"{put_profit_loss[i, j]:.2f}",
    #                  color=text_color, ha='center', va='center')

    ax2.set_title("Put Option Profit/Loss Heatmap")
    ax2.set_xlabel("Spot Price")
    ax2.set_ylabel("Volatility")

    with col5:
        st.pyplot(fig1)

    with col6:
        st.pyplot(fig2)


# Main Streamlit App
def app():
    st.title("Inputs")

    col1, col2 = st.columns(2)

    # Inputs
    with col1:
        min_volatility = st.slider("Minimum Volatility", min_value=0.01, max_value=1.00, value=0.01)
        min_spot_price = st.number_input("Minimum Spot Price", value=100.0)
        risk_free_interest_rate = st.number_input("Risk-Free Interest Rate", value=0.02)
        purchase_price_call = st.number_input("Spot Price at Expiry (Call)", value=135.0)

    with col2:
        max_volatility = st.slider("Maximum Volatility", min_value=0.01, max_value=1.00, value=1.00)
        max_spot_price = st.number_input("Maximum Spot Price", value=200.0)
        time_to_expiration = st.number_input("Time to Expiration (years)", value=1)
        purchase_price_put = st.number_input("Spot Price at Expiry (Put)", value=65.0)

    strike_price = st.number_input("Strike Price", value=150.0)

    # Submit Button
    if st.button("Generate Heatmaps"):
        # Call the heatmap generation function on button click
        st.title("Call and Put Heatmap")
        generate_call_put_heatmaps(
            min_volatility, max_volatility, min_spot_price, max_spot_price,
            risk_free_interest_rate, strike_price, time_to_expiration)
        
        generate_profit_loss_heatmaps(min_volatility, max_volatility, min_spot_price, max_spot_price,
            risk_free_interest_rate, strike_price, time_to_expiration, purchase_price_call, purchase_price_put)

# Run the app
if __name__ == "__main__":
    app()

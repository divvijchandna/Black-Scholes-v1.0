# Black-Scholes-v1.0  
**Options Pricing Calculator using the Black-Scholes Model**

## 📜 Overview  
Black-Scholes-v1.0 is a Python-based application that calculates and visualizes the prices of financial options using the Black-Scholes model. It provides an intuitive interface for users to input parameters and retrieve pricing results efficiently.

## 🛠 Features  
- Calculate option prices for **call** and **put** options.  
- Input key parameters such as strike price, spot price, volatility, time to maturity, and risk-free interest rate.  
- Visualize option pricing trends and profit/loss.  
- Streamlined, user-friendly interface powered by Streamlit.  

## 🚀 Getting Started  
Follow these steps to run the application locally.

### Prerequisites  
- Python 3.8 or higher  
- Virtual environment setup (recommended)

### Installation  
1. Clone the repository:  
    ```bash
    git clone https://github.com/your_username/Black-Scholes-v1.0.git
    cd Black-Scholes-v1.0

2. Create a virtual environment and activate it:
    ```bash
    python -m venv .venv
    .venv\Scripts\activate  # On Windows

3. Install required dependencies:
    ```bash
    pip install -r requirements.txt

4. Run the application:
    ```bash
    streamlit run app.py
    
## 📊 How It Works  
The Black-Scholes model calculates the theoretical price of options using the following formula:  
$C = S\Phi(d_1) - Ke^{-rt}\Phi(d_2)$  
where:  
- \( C \): Price of the call option  
- \( S \): Current spot price of the underlying asset  
- \( K \): Strike price of the option  
- \( t \): Time to maturity (in years)  
- \( r \): Risk-free interest rate  
- $(\Phi(d))$: Cumulative distribution function of the standard normal distribution  

### Intermediate Variables:
- \( d_1 = \frac{\ln(S/K) + (r + \sigma^2/2)t}{\sigma \sqrt{t}} \)  
- \( d_2 = d_1 - \sigma \sqrt{t} \)  

The app simplifies these calculations, allowing users to input parameters like the spot price, strike price, volatility (\( \sigma \)), risk-free rate, and time to maturity. It then computes and displays the option price in a user-friendly interface.

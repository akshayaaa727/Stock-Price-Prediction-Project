# 📈 LSTM Stock Price Prediction App

This project uses an LSTM (Long Short-Term Memory) neural network to predict future stock prices based on past trends. It includes technical indicators like RSI and Moving Averages as features and is deployed as a live, interactive web app using Streamlit.

## 🚀 Live Demo

**[Click here to view the live application!](https://stock-price-prediction-project-fqhnkc7kffgtcg4hftzh7m.streamlit.app/)**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://stock-price-prediction-project-fqhnkc7kffgtcg4hftzh7m.streamlit.app/)



---

## 📋 Features

* **Time-Series Prediction:** Uses a Keras/TensorFlow LSTM model to forecast stock prices.
* **Feature Engineering:** Enhances the model's accuracy by using the **20-day Moving Average (MA)** and the **Relative Strength Index (RSI)** as input features.
* **Interactive Visualization:** Displays the *Actual* vs. *Predicted* prices on an interactive Plotly chart.
* **Model Details:** Shows the complete architecture of the trained neural network.

---

## 🛠️ Technologies Used

* **Python:** The core programming language.
* **TensorFlow / Keras:** For building and training the LSTM neural network.
* **Streamlit:** To build and deploy the interactive web dashboard.
* **Pandas:** For data manipulation and processing.
* **Plotly:** For creating interactive, web-based charts.
* **yfinance:** To fetch historical stock data from the Yahoo Finance API.
* **TA-Lib:** For calculating technical analysis indicators (RSI, MA).
* **Scikit-learn (MinMaxScaler):** For normalizing data before feeding it to the model.

---

## 📁 Repository Contents

* **`app.py`**: The main Python script that runs the Streamlit web application.
* **`requirements.txt`**: A list of all Python libraries required for the app to run on Streamlit Cloud.
* **`stock_lstm_model.h5`**: The pre-trained LSTM model file. *(Handled by Git LFS or GDrive download)*
* **`stock_scaler.gz`**: The saved `MinMaxScaler` object used to normalize the data.
* **`predictions.csv`**: A CSV file containing the test data (actual vs. predicted) used to generate the chart.
* **`stockprice_prediction.ipynb`**: The Jupyter/Colab notebook used for the original data exploration and model training.

---

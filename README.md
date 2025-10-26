# Stock Price Prediction Project

This project uses an LSTM neural network to predict stock prices and displays the results in an interactive Streamlit dashboard.

## Files Included:
* **stockprice_prediction.ipynb**: The Google Colab notebook used for data processing, model training, and evaluation.
* **app.py**: The Python script for the Streamlit dashboard.
* **stock_lstm_model.h5**: The pre-trained Keras model.
* **stock_scaler.gz**: The pre-fit scikit-learn scaler.
* **predictions.csv**: The test data (Actual vs. Predicted) used by the dashboard.

## How to Run the Dashboard

1.  **Prerequisites:** You must have `python3` and `pip3` installed on your computer.

2.  **Install Libraries:** Open your terminal and install the required libraries:
    ```bash
    pip3 install streamlit tensorflow plotly pandas
    ```

3.  **Run the App:**
    * In your terminal, navigate to this project folder.
    * Run the following command:
    ```bash
    python3 -m streamlit run app.py
    ```

4.  The dashboard will automatically open in your web browser.

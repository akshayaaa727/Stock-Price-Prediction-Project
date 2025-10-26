import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from tensorflow.keras.models import load_model
import os

# --- Page Configuration ---
st.set_page_config(
    page_title="Stock Prediction Dashboard",
    page_icon="📈",
    layout="wide"
)

# --- Caching ---
@st.cache_data
def load_data(path):
    return pd.read_csv(path)

@st.cache_resource
def load_keras_model(path):
    return load_model(path)

st.title("📈 LSTM Stock Price Prediction Dashboard")
st.write("This dashboard is running locally on your computer.")

# --- Load Files ---
# These files must be in the SAME folder as this app.py file
try:
    results_df = load_data('predictions.csv')
    model = load_keras_model('stock_lstm_model.h5')
    
    st.success("Loaded prediction data and model successfully!")
    
    # --- Display Interactive Prediction Plot ---
    st.header("Actual vs. Predicted Prices")
    st.write("Use the controls to pan and zoom.")
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        y=results_df['Actual'],
        name='Actual Price',
        line=dict(color='blue', width=2)
    ))
    fig.add_trace(go.Scatter(
        y=results_df['Predicted'],
        name='Predicted Price',
        line=dict(color='red', width=2, dash='dot')
    ))
    fig.update_layout(
        xaxis_title="Time (Days in Test Set)",
        yaxis_title="Stock Price ($)",
        hovermode="x unified"
    )
    st.plotly_chart(fig, use_container_width=True)

    # --- Display Model Summary & Data ---
    col1, col2 = st.columns(2)
    with col1:
        st.header("Model Details")
        stringlist = []
        model.summary(print_fn=lambda x: stringlist.append(x))
        model_summary = "\n".join(stringlist)
        st.text(model_summary)
        
    with col2:
        st.header("Raw Prediction Data")
        st.dataframe(results_df.tail(15))

except FileNotFoundError:
    st.error("ERROR: Could not find 'predictions.csv' or 'stock_lstm_model.h5'.")
    st.write("Please make sure those files are in the same folder as 'app.py'.")
except Exception as e:
    st.error(f"An error occurred: {e}")
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "06a7f4e9-e15f-4735-8e74-c1d519f24cb1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: streamlit in c:\\users\\palan\\anaconda3\\lib\\site-packages (1.43.2)\n",
      "Requirement already satisfied: altair<6,>=4.0 in c:\\users\\palan\\anaconda3\\lib\\site-packages (from streamlit) (5.0.1)\n",
      "Requirement already satisfied: blinker<2,>=1.0.0 in c:\\users\\palan\\anaconda3\\lib\\site-packages (from streamlit) (1.6.2)\n",
      "Requirement already satisfied: cachetools<6,>=4.0 in c:\\users\\palan\\anaconda3\\lib\\site-packages (from streamlit) (5.3.3)\n",
      "Requirement already satisfied: click<9,>=7.0 in c:\\users\\palan\\anaconda3\\lib\\site-packages (from streamlit) (8.1.7)\n",
      "Requirement already satisfied: numpy<3,>=1.23 in c:\\users\\palan\\appdata\\roaming\\python\\python312\\site-packages (from streamlit) (1.26.4)\n",
      "Requirement already satisfied: packaging<25,>=20 in c:\\users\\palan\\anaconda3\\lib\\site-packages (from streamlit) (24.2)\n",
      "Requirement already satisfied: pandas<3,>=1.4.0 in c:\\users\\palan\\anaconda3\\lib\\site-packages (from streamlit) (2.3.3)\n",
      "Requirement already satisfied: pillow<12,>=7.1.0 in c:\\users\\palan\\anaconda3\\lib\\site-packages (from streamlit) (11.3.0)\n",
      "Requirement already satisfied: protobuf<6,>=3.20 in c:\\users\\palan\\anaconda3\\lib\\site-packages (from streamlit) (5.29.5)\n",
      "Requirement already satisfied: pyarrow>=7.0 in c:\\users\\palan\\anaconda3\\lib\\site-packages (from streamlit) (16.1.0)\n",
      "Requirement already satisfied: requests<3,>=2.27 in c:\\users\\palan\\anaconda3\\lib\\site-packages (from streamlit) (2.32.3)\n",
      "Requirement already satisfied: tenacity<10,>=8.1.0 in c:\\users\\palan\\anaconda3\\lib\\site-packages (from streamlit) (8.2.3)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in c:\\users\\palan\\anaconda3\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.4.0 in c:\\users\\palan\\anaconda3\\lib\\site-packages (from streamlit) (4.12.2)\n",
      "Requirement already satisfied: watchdog<7,>=2.1.5 in c:\\users\\palan\\anaconda3\\lib\\site-packages (from streamlit) (4.0.1)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in c:\\users\\palan\\anaconda3\\lib\\site-packages (from streamlit) (3.1.43)\n",
      "Requirement already satisfied: pydeck<1,>=0.8.0b4 in c:\\users\\palan\\anaconda3\\lib\\site-packages (from streamlit) (0.8.0)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in c:\\users\\palan\\anaconda3\\lib\\site-packages (from streamlit) (6.4.1)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\palan\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (3.1.4)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\users\\palan\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (4.23.0)\n",
      "Requirement already satisfied: toolz in c:\\users\\palan\\anaconda3\\lib\\site-packages (from altair<6,>=4.0->streamlit) (0.12.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\palan\\anaconda3\\lib\\site-packages (from click<9,>=7.0->streamlit) (0.4.6)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in c:\\users\\palan\\anaconda3\\lib\\site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.7)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\palan\\anaconda3\\lib\\site-packages (from pandas<3,>=1.4.0->streamlit) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\palan\\anaconda3\\lib\\site-packages (from pandas<3,>=1.4.0->streamlit) (2025.2)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\users\\palan\\anaconda3\\lib\\site-packages (from pandas<3,>=1.4.0->streamlit) (2025.2)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\palan\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\palan\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\palan\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.2.3)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\palan\\anaconda3\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2025.11.12)\n",
      "Requirement already satisfied: smmap<5,>=3.0.1 in c:\\users\\palan\\anaconda3\\lib\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\palan\\anaconda3\\lib\\site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.3)\n",
      "Requirement already satisfied: attrs>=22.2.0 in c:\\users\\palan\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (23.1.0)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in c:\\users\\palan\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.7.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in c:\\users\\palan\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.30.2)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in c:\\users\\palan\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.10.6)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\palan\\anaconda3\\lib\\site-packages (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit) (1.17.0)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: Ignoring invalid distribution ~atplotlib (C:\\Users\\palan\\anaconda3\\Lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution ~atplotlib (C:\\Users\\palan\\anaconda3\\Lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution ~atplotlib (C:\\Users\\palan\\anaconda3\\Lib\\site-packages)\n"
     ]
    }
   ],
   "source": [
    "!pip install streamlit\n",
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import joblib\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "6f538919-a6f3-437a-be5b-d1b62e989368",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-12-03 22:39:11.684 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "# Load model\n",
    "model = joblib.load(\"C:/Users/palan/Downloads/random_forest_model.pkl\")\n",
    "\n",
    "st.title(\"🛒 Retail Sales Prediction App\")\n",
    "st.write(\"Enter the inputs below to predict sales.\")\n",
    "\n",
    "year = st.number_input(\"Year\", min_value=2000, max_value=2030, value=2024)\n",
    "month = st.number_input(\"Month\", min_value=1, max_value=12, value=1)\n",
    "day = st.number_input(\"Day\", min_value=1, max_value=31, value=1)\n",
    "dayofweek = st.number_input(\"Day of Week (0 = Monday, 6 = Sunday)\", min_value=0, max_value=6)\n",
    "\n",
    "lag_1 = st.number_input(\"Sales 1 day before\", value=2000)\n",
    "lag_7 = st.number_input(\"Sales 7 days before\", value=2200)\n",
    "lag_30 = st.number_input(\"Sales 30 days before\", value=2500)\n",
    "\n",
    "ma_7 = st.number_input(\"7-day moving avg\", value=2300)\n",
    "ma_30 = st.number_input(\"30-day moving avg\", value=2400)\n",
    "\n",
    "input_data = np.array([[year, month, day, dayofweek, lag_1, lag_7, lag_30, ma_7, ma_30]])\n",
    "\n",
    "if st.button(\"Predict Sales\"):\n",
    "    prediction = model.predict(input_data)[0]\n",
    "    st.success(f\"Predicted Sales: ₹{round(prediction, 2)}\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

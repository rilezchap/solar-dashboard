# Streamlit Financial Dashboard

This project is a Streamlit application that provides a financial analysis tool for solar energy systems. Users can input their state and roof size in kW to receive detailed financial insights, including upfront costs, annual generation, project IRR, payback period, and a 25-year cash flow table.

## Project Structure

```
streamlit-financial-dashboard
├── src
│   ├── app.py                # Main entry point for the Streamlit dashboard
│   └── financial_model.py     # Contains financial model functions for calculations
├── requirements.txt           # Lists project dependencies
└── README.md                  # Documentation for the project
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd streamlit-financial-dashboard
   ```

2. **Create a virtual environment** (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit application:
   ```
   streamlit run src/app.py
   ```

2. Open your web browser and navigate to `http://localhost:8501` to access the dashboard.

## Dashboard Functionality

- **Input Fields**: Users can enter their state name and roof size in kW.
- **Calculations**: The dashboard computes:
  - Upfront price of the solar system
  - Annual generation of electricity (in kWh)
  - Internal Rate of Return (IRR) for the project
  - Payback period for the investment
  - A detailed 25-year cash flow table

This tool aims to assist users in making informed decisions regarding solar energy investments by providing clear financial projections and insights.
import streamlit as st
import pandas as pd
# Import state_prices along with other functions
from financial_model import get_price, calc_system_cost, calc_itc, calc_revenue, calc_om_costs, generate_cashflows, calc_irr, calc_payback_period, state_prices

# Streamlit app title
st.title("Solar Financial Dashboard")

# User inputs
state = st.selectbox("Select your state:", list(state_prices.keys()))
roof_size_kw = st.number_input("Enter roof size (kW):", min_value=0.0)

# Constants
cost_per_watt = 2.5  # Example cost per watt
itc_rate = 0.3  # Example ITC rate
annual_generation_kwh = 1500  # Example annual generation per kW
years = 25  # Duration for cash flow analysis
om_cost_per_kw = 15  # Example O&M cost per kW

if st.button("Calculate"):
    # Initialize variables
    irr = None
    payback_period = None
    cash_flows = None

    # Calculations
    price_per_kwh = get_price(state)
    system_cost = calc_system_cost(roof_size_kw, cost_per_watt)
    itc = calc_itc(system_cost, itc_rate)
    revenues = calc_revenue(price_per_kwh, roof_size_kw, annual_generation_kwh, years, 0.02)  # Assuming 2% increase in price
    om_costs = calc_om_costs(roof_size_kw, years, om_cost_per_kw)
    cash_flows = generate_cashflows(system_cost, itc, revenues, om_costs)
    irr = calc_irr(cash_flows)
    payback_period = calc_payback_period(cash_flows)

    # Display results
    st.subheader("Results")
    st.write(f"Upfront System Price: ${system_cost:,.2f}")
    st.write(f"Annual Generation (kWh): {annual_generation_kwh * roof_size_kw:.2f}")
    st.write(f"Project IRR: {irr * 100:.2f}%")
    st.write(f"Payback Period: {payback_period} years" if payback_period is not None else "Payback Period: Not reached")

    # Cash flow table
    cash_flow_df = pd.DataFrame({
        "Year": range(0, years + 1),
        "Cash Flow": cash_flows
    })
    st.subheader("25-Year Cash Flow Table")
    st.table(cash_flow_df)

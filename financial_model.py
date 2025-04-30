import numpy_financial as npf

#electricity price by state
state_prices = { 
"Alabama": 0.1491,
    "Alaska": 0.2238,
    "Arizona": 0.1520,
    "Arkansas": 0.1174,
    "California": 0.3055,
    "Colorado": 0.1516,
    "Connecticut": 0.2816,
    "Delaware": 0.1668,
    "D.C.": 0.1883,
    "Florida": 0.1420,
    "Georgia": 0.1349,
    "Hawaii": 0.4234,
    "Idaho": 0.1097,
    "Illinois": 0.1599,
    "Indiana": 0.1442,
    "Iowa": 0.1243,
    "Kansas": 0.1385,
    "Kentucky": 0.1328,
    "Louisiana": 0.1170,
    "Maine": 0.2629,
    "Maryland": 0.1815,
    "Massachusetts": 0.3122,
    "Michigan": 0.1841,
    "Minnesota": 0.1405,
    "Mississippi": 0.1344,
    "Missouri": 0.1157,
    "Montana": 0.1187,
    "Nebraska": 0.1078,
    "Nevada": 0.1488,
    "New Hampshire": 0.2362,
    "New Jersey": 0.1949,
    "New Mexico": 0.1426,
    "New York": 0.2437,
    "North Carolina": 0.1349,
    "North Dakota": 0.1021,
    "Ohio": 0.1598,
    "Oklahoma": 0.1152,
    "Oregon": 0.1412,
    "Pennsylvania": 0.1760,
    "Rhode Island": 0.2531,
    "South Carolina": 0.1387,
    "South Dakota": 0.1242,
    "Tennessee": 0.1304,
    "Texas": 0.1532,
    "Utah": 0.1102,
    "Vermont": 0.2229,
    "Virginia": 0.1446,
    "Washington": 0.1183,
    "West Virginia": 0.1451,
    "Wisconsin": 0.1631,
    "Wyoming": 0.1178
}

#calculation functions 
def get_price(state):
    """
    Get the price of electricity for a given state.
    """
    if not isinstance(state, str):
        raise TypeError("State must be a string.")
    if state not in state_prices:
        raise ValueError(f"State '{state}' not found in the price list.")
    return state_prices[state]

def calc_system_cost(roof_size_kw, cost_per_watt):
    """
    Calculate the system cost based on roof kW size and cost per watt.
    """
    if not isinstance(roof_size_kw, (int, float)) or roof_size_kw <= 0:
        raise ValueError("Roof size (kW) must be a positive number.")
    if not isinstance(cost_per_watt, (int, float)) or cost_per_watt <= 0:
        raise ValueError("Cost per watt must be a positive number.")
    return roof_size_kw * 1000 * cost_per_watt

def calc_itc(system_cost, itc_rate):
    """
    Calculate the ITC based on rate and system cost.
    """
    if not isinstance(system_cost, (int, float)) or system_cost < 0:
        raise ValueError("System cost must be a non-negative number.")
    if not isinstance(itc_rate, (int, float)) or not (0 <= itc_rate <= 1):
        raise ValueError("ITC rate must be a number between 0 and 1.")
    return system_cost * itc_rate

def calc_revenue(initial_price, roof_size_kw, generation, years, inc_rate):
    """
    Calculate the revenue from selling electricity.
    """
    if not isinstance(initial_price, (int, float)) or initial_price < 0:
        raise ValueError("Initial price must be a non-negative number.")
    if not isinstance(roof_size_kw, (int, float)) or roof_size_kw < 0:
        raise ValueError("Roof size (kW) must be a non-negative number.")
    
    revenues = []
    price = initial_price
    for year in range(years):
        revenues.append(price * generation * roof_size_kw)
        price *= (1 + inc_rate)
    return revenues

def calc_om_costs(roof_size_kw, years, cost_per_kw):
    """
    Calculate the costs associated with the system.
    """
    if not isinstance(roof_size_kw, (int, float)) or roof_size_kw <= 0:
        raise ValueError("Roof size (kW) must be a positive number.")
    
    annual_cost = cost_per_kw * roof_size_kw
    return [annual_cost for i in range(years)]
    
def generate_cashflows(system_cost, itc, revenues, o_and_m):
    """
    Generate cash flows for the system.
    """
    if not isinstance(system_cost, (int, float)) or system_cost < 0:
        raise ValueError("System cost must be a non-negative number.")
    if not isinstance(itc, (int, float)) or itc < 0:
        raise ValueError("ITC must be a non-negative number.")
    if not isinstance(revenues, list) or not all(isinstance(r, (int, float)) for r in revenues):
        raise TypeError("Revenues must be a list of numbers.")
    if not isinstance(o_and_m, list) or not all(isinstance(o, (int, float)) for o in o_and_m):
        raise TypeError("O&M costs must be a list of numbers.")
    if len(revenues) != len(o_and_m):
        raise ValueError("Revenues and O&M lists must have the same length.")
    
    cashflows = []
    year0 = -(system_cost - itc)
    cashflows.append(year0)
    for i in range(len(revenues)):
        cashflows.append(revenues[i] - o_and_m[i])
    return cashflows

#final calculations to display 
def calc_irr(cash_flows):
    """
    Calculate the Internal Rate of Return (IRR).
    """
    if not isinstance(cash_flows, list) or not all(isinstance(cf, (int, float)) for cf in cash_flows):
        raise TypeError("Cash flows must be a list of numbers.")
    if len(cash_flows) == 0:
        raise ValueError("Cash flows list cannot be empty.")
    
    try:
        return npf.irr(cash_flows)
    except Exception as e:
        raise ValueError(f"Failed to calculate IRR: {e}")

def calc_payback_period(cash_flows):
    """
    Calculate the payback period.
    """
    if not isinstance(cash_flows, list) or not all(isinstance(cf, (int, float)) for cf in cash_flows):
        raise TypeError("Cash flows must be a list of numbers.")
    if len(cash_flows) == 0:
        raise ValueError("Cash flows list cannot be empty.")
    
    cumulative = 0
    for year, cashflow in enumerate(cash_flows):
        cumulative += cashflow
        if cumulative >= 0:
            return year  # Payback year
    return None  # Payback period not reached

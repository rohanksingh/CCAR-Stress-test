# Example Stress test scenarios under CCAR

# Define macroeconomic variables for baseline and stress scenarios 

import pandas as pd 

scenarios = {
    'baseline': {
        'GDP_growth': [2.0, 2.1, 2.2],
        'unemployment_rate': [4.0, 3.9, 3.8],
        'interest_rate': [2.5, 2.6, 2.7]
    },
    'stress': {
        'GDP_growth': [-3.0, -1.0, 0.5],
        'unemployment_rate': [8.0, 7.5, 6.9],
        'interest_rate': [0.5, 1.0, 1.5]
    }
}


# Convert to Dataframe

scenarios_df= pd.DataFrame(scenarios)
print(scenarios_df)

 # Project Financial under each scenarios 

# Example function to project finacial outcomes under each scenario

def project_financials(initial_capital, scenario):
    projected_capital= initial_capital
    for year in range(3):

        gdp_growth= scenario['GDP_growth'][year]
        unemployment_rate= scenario['unemployment_rate'][year]
        interest_rate= scenario['interest_rate'][year]


    # Simplified example of projecting losses and revenue

        projected_losses= projected_capital*(0.1-gdp_growth/100 + unemployment_rate/100)
        projected_revenue= projected_capital*(0.05 + interest_rate/100)

        projected_capital= projected_capital - projected_losses + projected_revenue

    return projected_capital


if __name__ == "__main__":
# Initial capital 
    initial_capital = 1000

# Project financials under baseline and stress scenarios 

    baseline_capital= project_financials(initial_capital, scenarios['baseline'])
    stress_capital= project_financials(initial_capital, scenarios['stress'])

    print(f'Projected capital under Baseline Scenario: {baseline_capital}')
    print(f'Projected Capital under Stress Scenarios: {stress_capital}')

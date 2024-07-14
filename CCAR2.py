# Access Capital Adequacy 

# Define regulatory capital requirements

from CCAR import scenarios , project_financials

# Initial capital
initial_capital = 1000

# Project financials under baseline and stress scenarios
baseline_capital = project_financials(initial_capital, scenarios['baseline'])
stress_capital = project_financials(initial_capital, scenarios['stress'])

minimum_capital_requirements =800

# Check if projected capital meets the requirements 

baseline_adequacy= baseline_capital >= minimum_capital_requirements
stress_adequacy = stress_capital >= minimum_capital_requirements

print(f'Baseline Scenario Capital Adequacy: {baseline_adequacy}')
print(f'Stress Scenario Capital Adequacy: {stress_adequacy}')

def calculate_simple_interest(principal, time, gender, senior_citizen):
    rate = 8 if gender == "female" and senior_citizen else 6 if gender == "female" else 7 if senior_citizen else 5
    return (principal * rate * time) / 100

# Example usage
principal_amount = 10000
time_period = 2
customer_gender = "female"
is_senior_citizen = True

simple_interest = calculate_simple_interest(principal_amount, time_period, customer_gender, is_senior_citizen)
total_amount = principal_amount + simple_interest

print("Principal Amount:", principal_amount)
print("Simple Interest:", simple_interest)
print("Total Amount:", total_amount)

# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment= 2684.11
total_paid = 0.0
extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000
months = 0
while principal > 0:
    if payment > principal:
        payment = principal * (1+rate/12)
    months += 1
    principal = principal * (1+rate/12) - payment
    total_paid  = total_paid + payment

    if extra_payment_start_month <= months and months <= extra_payment_end_month:
        principal -= extra_payment
        total_paid = total_paid + extra_payment
    print(f'Month: {months:5d}  Total Paid: {total_paid:10.2f}  Pricipal: {principal:10.2f}')
    #print(months, round(total_paid,2), round(principal,2), payment)
print('Total paid', round(total_paid,2))
print(months)



balance_paid = input('How much have you paid?: ')

balance_paid = float(balance_paid)
balance_due = 65000

if balance_paid == balance_due:
    points  = balance_paid * .01
if balance_paid >= balance_due:
    points = balance_paid * .1
if balance_paid <= balance_due:
    points = balance_paid * .001
if balance_paid == 0:
    points = 0


print('You have', points, 'points')






print('Welcome to the tip calculator')
total_bill = float(input('What was the total bill? $'))
tip = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
bill_with_tip = tip / 100 * total_bill + total_bill
split_num = int(input('How many people to split the bill? '))
each_person_pays = (total_bill / split_num) * (1 + (tip / 100))
final_bill_with_tip = '{:.2f}'.format(bill_with_tip)

print(f'Each person pays ${each_person_pays:.2f} from a total of {final_bill_with_tip}')
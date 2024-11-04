loyalty_customer = False
total_bill = 124

if loyalty_customer and total_bill > 100:
    #give 20% discount
    print('Congratulations, you have 20% discount ...')
    total_bill = total_bill - (float(total_bill)/ 100) * 20
elif total_bill > 100:
    #give 10% discount
    print('Congratulations, you have 10% discount ...')
    total_bill = total_bill - (float(total_bill)/ 100) * 10
else:
    #sorry no discount, 5% service charge applied.
    print('Sorry, no discount ...')

print('Total Bill: ', float(total_bill))

#match statement

http_status_code = 404

match http_status_code:
    case 200:
        print('OK')
    case 404:
        print('Not Found')
    case 500:
        print('Internal Server Error')
    case _: //default case
        print('Unknown Error')
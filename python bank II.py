import time
import os
os.system('cls' if os.name == 'nt' else 'clear')

accounts = {
  'Alice': 500.00,
  'Bob': 1000.00,
  'Charlie': 1500.00
}

services = {
  1: 'Alice',
  2: 'Bob',
  3: 'Charlie',
  4: 'Exit'
}

print("------=== YOU'RE WELCOME TO PYTHON BANK! ===------")
time.sleep(2)

while True:
  for number, name in services.items():
    print(f'press {number} for {name}')
  try:
    user = int(input('select user: '))
    time.sleep(2)
    print('Processing, please wait.......')
    time.sleep(1.5)
    if user in services:
      if user == 4:
        print('Operation Cancelled successfully!')
        time.sleep(2)
        print('Ejecting card, please wait............')
        time.sleep(2)
        print('Card ejected successsfully!')
        time.sleep(0.5)
        print('Thank you for banking with us, do have a nice day!')
        break

      account_name = services[user]
      print(f'Welcome {account_name}!, your current balance: ${accounts[account_name]:.2f}')
      amount = float(input('Enter amount to withdraw: $'))
      print('Processing............')
      time.sleep(1)
      if amount <= 0:
        raise ValueError('Invalid Input: Withdrawal amount must be greater than 0')
      elif amount > accounts[account_name]:
        raise Exception('Insufficient Fund!')
      else:
        accounts[account_name] -= amount
        print(f'Withdrawal Successful! New balance: ${accounts[account_name]:.2f}')
        time.sleep(2)
    else:
      print('Error: Invalid Input!')
      time.sleep(1.5)
  except ValueError:
    print(f'Error: Invalid input! please enter a valid number!')
  except Exception as e:
    print(f'Error: {e}')


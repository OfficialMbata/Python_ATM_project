import time
import os
os.system('cls' if os.name == 'nt' else 'clear')

accounts = {
  'Ayo': {'balance': 20000.00, 'pin': None, 'history': []},
  'Princess': {'balance': 5000.00, 'pin': None, 'history': []},
  'Deborah': {'balance': 40000.00, 'pin': None, 'history': []},
  'Blessing': {'balance': 90000.00, 'pin': None, 'history': []},
  'Jasmine': {'balance': 30000.00, 'pin': None, 'history': []}
}

services = {
  1: 'Ayo',
  2: 'Princess',
  3: 'Deborah',
  4: 'Blessing',
  5: 'Jasmine',
  6: 'Exit'
}

our_services = {
  1: 'Check balance',
  2: 'Deposit',
  3: 'Withdraw',
  4: 'Transfer',
  5: 'Transaction History',
  6: 'Back to menu'
}

def welcome_message():
  """
  This displays a welcome message to the user.
  """
  print("------=== YOU'RE WELCOME TO PYTHON BANK! ===------")
  print('\n')
  time.sleep(3)

welcome_message()

def service()-> int:
    """
    This displays the service UI unto the customers.
    Quick tip:
      using numbers to match to the corresponding user
    """
    try:
      
      for number, name in services.items():
        print(f'Press {number} for {name}')
      time.sleep(2.5)

      user_input = int(input('Select user: '))
      print('\n')
      return user_input
    
    except ValueError:
      print(f'Eror: Invalid input! Enter a valid number')
      time.sleep(3)

def our_service():
  """
  A menu to help guide the user on the operations they wish to carry out.
  """
  try:
    for number, name in our_services.items():
      print(f'press {number} to {name}')
    time.sleep(2.5)

    user_choice = int(input('Enter your prefered option: '))
    print('\n')
    return user_choice

  except ValueError:
    print(f'Error: Invalid input!. Enter a valid number')


def deposit_function(name):
  """
  This function allows the user add money to his/her existing account
  """
  try:
    deposit = float(input('Enter amount to deposit: $'))

    if deposit <= 0:
      print(f'Error: Deposit amount must be greater than zero(0)')
      return False

    else:
      accounts[name]['balance'] = accounts[name]['balance'] + deposit

      accounts[name]['history'].append(f'Amount deposited: ${deposit:,.2f}, New balance: ${accounts[name]['balance']:,.2f}')
      return accounts[name]['balance'], True
  
  except ValueError:
    print(f'Error: Invalid input!. Enter a valid number')
    return False


def withdraw_function(name):
  """
  This function allows the user remove money fron his/her existing account
  """
  try:
    withdraw = float(input("Enter the amount to withdraw: $"))
    print('\n')

    if withdraw <= 0:
      print(f'Error: Invalid input. Enter a number greater than zero(0)')
      return False

    elif withdraw > accounts[name]['balance']:
      print('Error: Insufficient Funds')
      return False

    else:
      accounts[name]['balance'] = accounts[name]['balance'] - withdraw

      accounts[name]['history'].append(f'Amount withdrawn: ${withdraw:,.2f}, New balance: ${accounts[name]['balance']:,.2f}')
      return accounts[name]['balance'], True
  except ValueError:
    print('Error: Invalid Input')


def transfer_function(name):
  """
  This function allows the user to send money from his/her account to another account other than his
  """
  try: 
    receiver_name = input('Enter the recipient name?: ')

    if receiver_name in accounts:
      receiver_account = accounts[receiver_name]
    
      transfer_amount = float(input("Enter the amount you wish to transfer: $"))

      receiver_account['balance'] += transfer_amount
      receiver_account['history'].append(f'CR: ${transfer_amount:,.2f}, New balance: ${receiver_account["balance"]:,.2f}')

      accounts[name]['balance'] -= transfer_amount 
      accounts[name]['history'].append(f'DR: ${transfer_amount:,.2f}, New balance: ${accounts[name]["balance"]:,.2f}')
      return receiver_account, accounts[name]['balance'], True

    else:
      print(f'Error: Invalid username, Account not found')
      return False

  except ValueError:
    print(f'Error: Invalid input')


# the ochestrator function
def run_atm_simulator():
  while True: 
    # calling the next UI display
    user_input = service()
    # assigning conditions
    if user_input in services:
      if user_input == 6:
        print('Operation Cancelled successfully!')
        time.sleep(2)
        print('Ejecting card, please wait............')
        time.sleep(2)
        print('Card ejected successsfully!')
        time.sleep(0.5)
        print('Thank you for banking with us, do have a nice day!')
        break

      account_name = services[user_input]
      print(f'Welcome {account_name}!')
      time.sleep(2.5)

      # the inner loop
      while True:
        user_choice = our_service()

        # this section handles the check balance option
        if user_choice == 1:
          print(f'Processing, please wait.....')
          time.sleep(2)
          print(f'Balance: ${accounts[account_name]['balance']:,.2f}')
          time.sleep(3)

        # this section handles the deposit option
        elif user_choice == 2:
          print(f'Processing, please wait......')
          time.sleep(2)
          successful = deposit_function(account_name)
          if successful:
            print(f'Status: Transaction successful!')
            time.sleep(3)
          else:
            print(f'Status: Transcation failed!')
          time.sleep(3)

        #  this section handles the withdraw option
        elif user_choice == 3:
          print(f'Processing, please wait......')
          time.sleep(2)
          successful = withdraw_function(account_name)
          if successful:
            print(f'Status: Transaction successful!')
            time.sleep(3)
          else:
            print(f'Status: Transcation failed!')
          time.sleep(3)

        # this section handles the transfer option
        elif user_choice == 4:
          print(f'Processing, please wait......')
          time.sleep(2)
          successful = transfer_function(account_name)
          if successful:
            print(f'Status: Transaction successful!')
            time.sleep(3)
          else:
            print(f'Status: Transcation failed!')
          time.sleep(3)

        # this section handles the transcaction history option
        elif user_choice == 5:
          print(f'Processing, please wait......')
          time.sleep(2)
          history = accounts[account_name]['history']

          if not history:
            print(f'No transactions yet')

          else:
            for transaction in history:
              print(transaction)

          input('\n Press enter to return to main menu')

        # this section handles the back to menu option
        elif user_choice == 6:
          print(f'Processing, please wait......')
          time.sleep(2)
          print(f'Returning to main menu......')
          time.sleep(2)
          break

        elif user_input is not None:
          lowest_value = min(services.keys())
          highest_value = max(services.keys())
          print(f'Invalid input! please select a number between {lowest_value} and {highest_value}')
          time.sleep(2)

        
    elif user_input is not None:
      lowest_value = min(services.keys())
      highest_value = max(services.keys())
      print(f'Invalid input! please select a number between {lowest_value} and {highest_value}')
      time.sleep(2)


run_atm_simulator()

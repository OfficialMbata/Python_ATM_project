import os
os.system('cls' if os.name == 'nt' else 'clear')
import time

balance = 500.00
print("----===You're welcome to python bank===----")
time.sleep(1)

try:
  print(f"your current balance is: ${balance:.2f}")
  amount = float(input("Enter amount to withdraw: $"))
  print("processing.............")
  time.sleep(1)
  if amount <= 0:
    raise ValueError("Withdrawal amount must be greater than 0")
  elif amount > balance:
    raise Exception("Insufficient Funds!")
  else:
    balance -= amount
    print(f"Withdrawal successful! New balance is: ${balance:.2f}")
except ValueError as ve:
  print(f'Error: {ve}')
except Exception as e:
  print(f'Error: {e}')

finally:
  print("Ejecting card, please wait...........")
  time.sleep(2)
  print("Card ejected successfully!")

print("Thank you for banking with us, do have a nice day!")

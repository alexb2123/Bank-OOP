import random



class Bank:
    accounts = {}

    def __init__(self):
        pass


    def user_choice(self):
        while True:
            user_input = input('Hello, would you like to create a new account, access an existing one,'
                               ' print all the bank accounts or exit? ')
            if user_input == 'create new account':
                self.create_account()
            elif user_input == 'access existing account':
                self.access_account()
            elif user_input == 'print bank accounts':
                self.print_dict()
            elif user_input == 'exit':
                print('Good bye!')
                break
            else:
                print('invalid entry')
                break

    def create_account(self):
        user_name = input('Enter your name: ')
        balance = float(input('Enter your deposit amount: '))
        account_number = random.randrange(10000,99999,1)
        self.accounts[account_number] = BankAccount(account_number, user_name, balance)
        print(account_number)


    def access_account(self):
     #validate_user
        validate_account_number = int(input('Enter your account number: '))
        validate_name = input('Enter your name: ')
        account_by_number = self.accounts.get(validate_account_number)
        if account_by_number.user_name == validate_name:
            self.user_options(validate_account_number)
        else:
            print('not valid')


    def user_options(self,validate_account_number):
      decide_on_options =int(input('What do you want to do: \n'
                                 '1) withdraw \n'
                                 '2) deposit \n'
                                 '3) display available balance\n'
                                   '4) exit\n'))

      if decide_on_options == 1:
          withdrawal_amount = int(input('Enter your withdrawal amount: '))
          self.accounts[validate_account_number].balance -= withdrawal_amount
          print(self.accounts[validate_account_number].balance)
          print('\n'
                '\n')
          self.user_options(validate_account_number)
      elif decide_on_options == 2:
          deposit_amount = int(input('Enter your deposit amount: '))
          self.accounts[validate_account_number].balance += deposit_amount
          print(self.accounts[validate_account_number].balance)
          print('\n'
                '\n')
          self.user_options(validate_account_number)
      elif decide_on_options == 3:
          print(self.accounts[validate_account_number].balance)
          print('\n'
                '\n')
          self.user_options(validate_account_number)
      elif decide_on_options == 4:
          self.user_choice()
      else:
          print('Invalid entry')
          self.user_options()


    def print_dict(self):
        for account in self.accounts:
            print(self.accounts[account])

class BankAccount:
    def __init__(self, account_number, user_name, balance):
        self.account_number = account_number
        self.user_name = user_name
        self.balance = balance

    def __str__(self):
        return (str(self.account_number) + " " + self.user_name + " " + str(self.balance))


if __name__ == "__main__":
    BOA = Bank()
    BOA.user_choice()
    BOA.print_dict()
    BOA.access_account()
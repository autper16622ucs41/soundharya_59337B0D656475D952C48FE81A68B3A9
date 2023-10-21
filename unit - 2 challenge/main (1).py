  def display_balance(self):
    print("Account balance for {} (Account #{}): ₹{}".format(
        self._account_holder_name, self._account_number,
        self.__account_balance))
  # Create an instance of the BankAccount class
  account = BankAccount(account_number="123456789",
                      account_holder_name="Hari Prabu",
                      initial_balance=5000.0)
  # Test deposit and withdrawal functionality
  account.display_balance()
  account.deposit(500.0)
  account.withdraw(200.0)
  account.withdraw(20000.0)
  account.display_balance()
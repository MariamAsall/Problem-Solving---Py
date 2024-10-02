class BankAccount:
    def __init__ (self, salary):
        self.__salary= salary
    
    def get_salary(self):
        return self.__salary
    def set_salary(self, new_salary):
        self.__salary = new_salary
    
    def compute_profit_percentage(self, profit):
        try:
            return (profit / self.__salary) * 100
        
        except ZeroDivisionError :
            print("Error : Cannot Divide by Zero.")
        except OverflowError:
            print("Error : Overflow occured during compuration.")
        except TypeError:
            print("Error : Invalid Input Type.")
        except Exception as E:
            print("Un Excepted Error Occured:", E)
try: 
    initial_salary = float(input("Enter initial salary: "))
    account = BankAccount(initial_salary)
    profit_amount = float(input("Enter Profit amount: "))
    profit = account.compute_profit_percentage(profit_amount)
    print("Profit Percentage based on profit amount: ", profit)

except OverflowError:
    print("Overflow Error.")
except ValueError as e:
    print("Value Error:", e)
except Exception as e:
    print("Un Excepected Error Occured:", e)

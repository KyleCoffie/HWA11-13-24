class BudgetCategory:
    def __init__(self,name,budget):
        self.__name = name# Need to set self.name = to name to use later
        self.__budget = budget #500
        self.expenses_total = 0# used to save the cost of expenses
     
    def get_name(self):# these is a getter...
        return self.__name 
   
    def get_budget(self):
        return self.__budget
    
    def set_name(self,new_name):
        self.__name = new_name
        
    def set_budget(self,new_budget):
        self.__budget = new_budget
        
    def add_budget(self,cost):
        if cost > 0:# this is where we added 100 to
            self.set_budget(self.get_budget() + cost)#set_budget is new budget and the new budget is the original budget + the 100
            print(f"Added: {cost}")
        else:
            print("Amount could not be added")
            
    def expenses(self,cost):
        if cost < self.get_budget() - self.expenses_total:# cost is less than the set_budget - self.expenses... thats 500 - 300
            self.expenses_total += cost #Sets it equal to the 300 the expenses
            print(f"{cost} has been subtracted from the budget ")
        else:
            print("Insufficient funds")
            
    def display_budget_details(self):
        print(f"Reciept: {self.__name} Budget: {self.__budget} Remaining budget after expenses {self.__budget - self.expenses_total} ")
        
    

food_category = BudgetCategory("Food", 500)# 500 is get_budget Food is the name parameter 500 is thethe amoount
food_category.add_budget(100)#
food_category.expenses(300)#cost
food_category.display_budget_details()
from abc import ABC , abstractmethod 
class product (ABC) :
    def __init__ (self , name , price , description):
        self.__name = name 
        self.price = price 
        self.description= description
        
    @abstractmethod
    def details (self):
        pass
    
class grossries (product): 
    def __init__ (self , name , price , description, brand , expierydate , weight):
        super().__init__(  name , price , description)
        self.brand = brand 
        self.expierydate = expierydate
        self.weight= weight
    
    def details (self):
        print (f"grossries : {self.name} ({self.brand})")
        print (f"price: ${self.price}")
        print (f"decription : {self.description}")
        print (f"expierydate : {self.expierydate} month")
        print (f"weight : {self.weight}")

class electronics (product):
     def __init__ (self , name , price , description,brand , warrintydate):
        super().__init__( name , price , description)
        self.brand = brand 
        self.warrintydate =  warrintydate
        
     def details (self):
        print (f"electronics : {self.name} ({self.brand})")
        print (f"description : {self.description}")
        print (f"price: ${self.price}")
        print (f"warrintydate : {self.warrintydate} month")
    
class clothes (product):
     def __init__ (self , name , price , sizechart , brand , description , privicypolicy,material):
        super.__init__ (name , description , price)
        self.sizechart = sizechart 
        self.brand= brand 
        self.description= description
        self.privicypolicy =privicypolicy
        self.material=material
        
     def details (self):
         print (f"clothes : {self.name} ({self.brand})")
         print (f"description : {self.description}")
         print (f"price: ${self.price}")
         print (f"sizechart : {self.sizechart}")
         print (f"privicypolicy : {self.privicypolicy}")
         print(f"Size: {self.size}, Material: {self.material}")

class customer:
    def __init__(name, address , email):
        self.name = name 
        self.address = address 
        self.email= email
        self.cart = shoppingcart()
    def add_to_cart  (self  , product,quantity=1):
        self.cart.add (quantity , product)
    def viwe_items (self):
        self.cart.view ()
            
    def checkout (self):
        self.cart.checkout(self)
class shoppingcart :
    def __init__ (self):
        self.item = {}
    def add (self , product , quantity):
        if product in self.item :
            self.items [product] += quantity
        else :
            self.items [product]  = quantity
    def view (self):
        if not self.item :
            print ("your cart is empty")
            return
        for product, quantity in self.items.items():
            product.display_details()
            print(f"Quantity: {quantity}")
        
    def checkout(self, customer):  # Create an order
        if not self.items:
            print("you didn't choose itmes yet")
            return
        
        order = order (customer , self.items)
        order.calculate_total()
        order.display_deatails()
        self.item = {}
        print ("thans for ordring")
        
class order: 
    def __init__ (self , customer , itmes ):
        self.customer =customer
        self.itmes = items
        self.total = 0 
    def calculate_total (self):
        for product , quantity in self.items.items() :
            self.total += product.price *quantity
            
    def display_datails(self):
        print("Order Details:")
        print(f"Customer: {self.customer.name}")
        for product , quantity in self.items.items :
            print (f"quantity :{quantity}")
        print(f"Total: ${self.total}")
        
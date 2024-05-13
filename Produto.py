class Product:
  
 # Metodo Construtor 
  
  def __init__(self,id,name,price,description):
   self.id = id
   self.name = name
   self.price = price
   self.description = description
    
# Lista para armazenar os produtos.
products = [
  Product(1,"Cellphone Charger",19.99,"20w type c usb charger"),
  Product(2,"Glass film ",9.99,"Glass film protector for cellphones"),
  Product(3,"Case",15.99,"Silicon transparent case for cellphone ")
  ]
# Funções de listar,cadastrar,atualizar e deletar produtos.

def listProducts(products):
  print("\n---------------------\n")
  for product in products:
    print(f"Product ID : {product.id}\nName :  {product.name}\nPrice :  {product.price}\nDescription :  {product.description} "  
          "\n-------------------\n")

def registerProduct(products):
  print("\n---------------------\n")
  print("Please enter with the product info")
  
  id = int(input("Enter product id "))
  name = input("Enter product name ")
  price = float(input("Enter product price "))
  description = input("Enter product description ")
  newProduct = Product(id,name,price,description)
  products.append(newProduct)
  print("Registration was a success")
   
def deleteProductById(id):
  print("\n---------------------\n")
  removed = False
  for product in products:
    if product.id == id:
      products.remove(product)
      print(f"Product {product.name} removed!")
      removed = True
      break
  if not removed:
      print("No matches for this product")

def updateProduct(id):
  print("\n---------------------\n")
  updated = False
  for product in products:
    if product.id == id:
       print("Please enter with the product info")
       product.name = input("Enter new product name ")
       product.price = float(input("Enter new product price "))
       product.description = input("Enter new product description ")
       print("Product update was a success!")
       updated = True
       break
  if not updated:
    print("No matches for this product")


# Execução do aplicativo

op = 0
while op < 1 or op > 4:
  op = int(input("Choose an option\n"
     "1. List All products\n"
     "2. Register a new product\n"
     "3. Update product info\n"
     "4. Delete a Product \n"))
  if op == 1:
    listProducts(products)
    print("Want to go back to the previous menu?")
    op = int(input("1.For Yes\n2.For No\n"))
    if op == 1:
      op = 0
    elif op == 2:
      print("Thank you for using our service\nSee you soon!")
      break
    else: 
      print("invalid option")
      op = 0
    print("---------------------")
  elif op == 2:
    registerProduct(products)
    listProducts(products)
    print("Want to go back to the previous menu?")
    op = int(input("1.For Yes\n2.For No\n"))
    if op == 1:
      op = 0
    elif op == 2:
      print("Thank you for using our service\nSee you soon!")
      break
    else: 
      print("invalid option")
      op = 0
    print("---------------------")
  elif op == 3:
    listProducts(products)
    id = int(input("Enter with id number "))
    updateProduct(id)
    listProducts(products)
    print("Want to go back to the previous menu?")
    op = int(input("1.For Yes\n2.For No\n"))
    if op == 1:
      op = 0
    elif op == 2:
      print("Thank you for using our service\nSee you soon!")
      break
    else: 
      print("invalid option")
      op = 0
    print("---------------------")
  elif op == 4:
    listProducts(products)
    id = int(input("Enter with id number "))
    deleteProductById(id)
    listProducts(products)
    print("Want to go back to the previous menu?")
    op = int(input("1.For Yes\n2.For No\n"))
    if op == 1:
      op = 0
    elif op == 2:
      print("Thank you for using our service\nSee you soon!")
      break
    else: 
      print("invalid option")
      op = 0
    print("---------------------")
  else:
    print("Invalid option try again")
    
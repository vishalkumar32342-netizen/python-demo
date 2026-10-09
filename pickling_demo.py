import pickle

product_id=int(input("Enter product ID:"))
name=input("Enter product name:")
price=float(input("Enter price: "))
quantity=int(input("Enter quantity:"))
total=price*quantity
print("total:",total)


product_data= {
    "product id": product_id,
    "product name": name,
    "product price": price,
    "quantity": quantity,
    "total":total

}

with open("product.dat","wb") as file:
    pickle.dump(product_data,file)

print("\nPickling completed")


with open("product.dat","rb") as file:
    product_data=pickle.load(file)

print("Unpickling completed")
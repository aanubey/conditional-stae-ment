bp=float(input("enter the price of puchase"))
sp=float(input("enter the sales price"))
if sp>bp:
    profit=sp-bp
    print("the profit is",profit)
else:
    loss=sp-bp
    print("the loss is",loss)
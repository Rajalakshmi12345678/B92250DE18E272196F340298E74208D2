def                               linearSearchProduct(productlist, trgetproduct):
  indices = [] 
  for index, product in enumerate(productlist):
    if product == trgetproduct:
       indices.append(index)
  return indices
products=["shoes","boots","loafers","sandals","shoes"]
target = "shoes"
target2 = "apple"
result=linearSearchProduct(products, target)
print(result)
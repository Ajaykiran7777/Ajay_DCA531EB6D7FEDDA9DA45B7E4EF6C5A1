def  linearsearchproduct(productlist,targetproduct):
  indices = []

  for index, product in enumerate(productlist):
    if product == targetproduct:
      indices.append(index)

  return indices


# example
product = ["apple","banana","orange","apple","grapes","apple"]
target="apple"
result = linearsearchproduct(product, target)
print(result)
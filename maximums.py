def max_of_two(x, y):
   if x < y:
        return y 
   elif x > y:
        return x
   elif x== y:
        return x

def max_of_three(x, y, z):
   if z == y == x:
       return x
   elif y <= z < x or z <= y < x:
       return x
   elif x <= y < z or y <= x < z:
       return z
   elif z <= x < y or x <= z < y:
      return y

   

    

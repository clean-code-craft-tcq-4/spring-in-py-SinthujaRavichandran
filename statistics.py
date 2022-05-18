import math

def calculateStats(numbers):
  
  try:
        tot = 0
        for i in numbers:
            tot = tot+i
        return {"avg":float(tot)/len(numbers), "max":max(numbers), "min":min(numbers)}
   except ZeroDivisionError as e:
        return {"avg":math.nan, "max":math.nan, "min":math.nan}
       
  #return None

# 8
regions = ["Львівська", "Житомирська", "Крим", "Луганська", "Донецька", "Рівненська", "Харківська", "Одеська"]

for region in regions:
  first_letter = region[0].upper()
  if first_letter in "ЛЖР":
    direction = "Захід"
  elif first_letter in "КД":
    direction = "Схід"
  elif first_letter in "ХО":
    direction = "Південь"
  else:
    direction = "Невідома"
  print(f"{region}: {direction}")

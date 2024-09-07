employees = {
    "Кирил":{
       "посада": "Розробник",
       "КЕ": 8,
       "проєкти": ["Mail List Clasterisation", "Positions Classification", "Rewiews Schedule"]
   },
    "Андрей":{
       "посада": "Гейм дезайнер",
       "КЕ": 7,
       "проєкти": ["Earth Scanning", "Streets Data Scrapping", "Qgis Drawing"]
   },
    "Илья":{
       "посада": "Главний розробник",
       "КЕ": 8,
       "проєкти": ["Mail List Clasterisation", "Positions Classification", "Rewiews Schedule"]
   }
}
print("Список розробників")
for e in employees:
    print("-",e)
Power = 0
for e in employees:
    if Power < employees[e]["КЕ"]:
        Power = employees[e]["КЕ"]
print("Макс.кофиц.ефективности", Power)

metrics = [
    {"time": "10:00", "cpu": 68, "gpu": 70},
    {"time": "10:05", "cpu": 81, "gpu": 73},
    {"time": "10:10", "cpu": 72, "gpu": 69},
    {"time": "10:15", "cpu": 85, "gpu": 78}
]

result = [f"{item['time']} -> {max(item['cpu'], item['gpu'])}°C" 
          for item in metrics if max(item['cpu'], item['gpu']) > 75]
print(result)






payments = [
    ("Ирина", 32000, "Казань"),
    ("Марк", 58000, "Москва"),
    ("Анна", 65000, "Краснодар"),
    ("Сергей", 28000, "Калининград"),
    ("Ольга", 72000, "Киев")
]

result = [f"Клиент: {name}, сумма: {amount}K₽" if amount >= 60000 
          else f"Клиент: {name}, сумма: {amount}₽" 
          for name, amount, city in payments 
          if city.startswith('К') and amount >= 30000]
print(result)








departments = [
    {"name": "Core", "hours": 28, "remote": True},
    {"name": "Support", "hours": 15, "remote": False},
    {"name": "Dev", "hours": 35, "remote": True},
    {"name": "QA", "hours": 40, "remote": False},
    {"name": "Design", "hours": 18, "remote": True}
]

work_mode = {dept["name"]: "удалённо" if dept["remote"] else "в офисе" 
             for dept in departments if dept["hours"] >= 20}
print(work_mode)




logs = [
    "alex:login",
    "bob:update",
    "claire:logout",
    "david:login",
    "error_record",
    "eva:update",
    "frank:",
    ":action"
]

users = {log.split(':')[0].lower() 
         for log in logs 
         if log.count(':') == 1 and len(log.split(':')) == 2 
         and log.split(':')[0] and log.split(':')[1] 
         and log.split(':')[1] in ['login', 'update']}
print(users)







users = {
    user.lower()
    for log in logs
    if ':' in log
    for user, action in [log.split(':', 1)]
    if user and action in ['login', 'update']
}

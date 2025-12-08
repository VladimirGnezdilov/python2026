stations = [
    ('laser', '2025-12-02 12:00'),
    ('cnc', '2025-12-04 09:45'),
    ('printer', '2025-12-05 15:20'),
]
check_tool = 'cnc'
unused_tool = 'lathe'

diagnostics={}
check_tool = 'cnc'
unused_tool = 'lathe'
diagnostics.update(stations)
for i in diagnostics.keys():
   if i==check_tool:
    print(f"{i}->{diagnostics.value()}")
   else:
    continue
    if i==unused_tool:
     print(f"{i}->не проверялось")
    else:
      continue

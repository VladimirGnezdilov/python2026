starter_tools = ["отвёртка", "молоток", "уровень"]
cart=["шуруповёрт", "набор бит"]
starter_tools.extend(cart)
print(f"Третий предмет:{starter_tools[2]},\nПоследний предмет:{starter_tools[-1]},\nКоличество инструментов:{len(starter_tools)}")
enumerate(starter_tools, start=1)

def summarize_orders(*orders, **kwargs):
    if not orders:
        raise ValueError("Нету заказов")
    currency = kwargs.get("currency", "RUB")
    round_to = kwargs.get("round_to", 2)
  
    if not isinstance(round_to, int) or round_to < 0:
        round_to = 2
    
    total_items = 0
    for order in orders:
        if not isinstance(order, tuple) or len(order) != 2:
            continue
        if not isinstance(order[1], (int, float)):
            continue
        total_items += order[1]
    num_orders = len(orders)
    avg_items = total_items / num_orders if num_orders > 0 else 0
    avg_items = round(avg_items, round_to)
    
    result = {
        "orders": num_orders,
        "total_items": total_items,
        "avg_items": avg_items,
        "currency": currency
    }
    
    return result

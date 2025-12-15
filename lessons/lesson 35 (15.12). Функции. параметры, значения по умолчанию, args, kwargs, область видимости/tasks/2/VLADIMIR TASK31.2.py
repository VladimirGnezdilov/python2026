def add_task(task_list, title, description="", tags=None, is_urgent=False):
    if tags is None:
        tags = []
    task = {
        "title": title,
        "description": description,
        "tags": tags,
        "is_urgent": is_urgent
    }   
    task_list.append(task)  
    return task_list
my_tasks = []
print(add_task(my_tasks, "важный", "very important", tags=["ВАЖНО"], is_urgent=False))

tickets = [('ENT', 5), ('therapy', 9), ('ENT', 4), ('lab', 6)]
finished = ['lab']
visits = {}
def process_clinic_data(tickets, finished):
    for i, values in tickets:
        if i not in visits:
            visits[i] = 0
        visits[i] += values 
    for i in finished:
        visits.pop(i, 0) 
    print(visits)
result = process_clinic_data(tickets, finished)
print(result)

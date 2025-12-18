views = [
    ("intro", 120),
    ("dicts", 300),
    ("sets", 180),
    ("dicts", 150),
]
seconds_by_lesson={}
for lesson, seconds in views:
    if lesson in seconds_by_lesson:
        seconds_by_lesson[lesson] += seconds
    else:
        seconds_by_lesson[lesson] = seconds
for lesson, total_seconds in seconds_by_lesson.items():
    print(f"{lesson} -> {total_seconds}")


sessions = [
    ("user1", 3),
    ("user2", 1),
    ("user1", 2),
]
remove = ["user2", "bot"]
session_count = {}
for user, count in sessions:
    if user in session_count:
        session_count[user] += count
    else:
        session_count[user] = count
for user in remove:
    session_count.pop(user, 0)
print(session_count)

emails_a = {"a@corp.ru", "b@corp.ru", "c@gmail.com"}
emails_b = {"b@corp.ru", "d@corp.ru"}
emails_a.update(emails_b)
print(emails_b&emails_b)
print(emails_b-emails_a)


errors = [
    ("dict", 5),
    ("set", 1),
    ("dict", 2),
]
limit = 5
error_counts={}
for errs,t in errors:
    if errs in error_counts:
        error_counts[errs] += t
    else:
       error_counts[errs] = t
new_errors=[]
for value in error_counts.values():
    if value > limit:
        new_errors.append(value)

print(new_errors,error_counts)

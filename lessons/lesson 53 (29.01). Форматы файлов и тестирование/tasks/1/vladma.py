def calculator(filename):
    math_sum = physics_sum = chemistry_sum = 0
    count = 0
    with open(students.csv, 'r', encoding='utf-8') as file:
      file.readline()
        for line in file:
          data = line.strip().split(',')
            if len(data) >= 4:
              math_sum += int(data[1])
              physics_sum += int(data[2])
              chemistry_sum += int(data[3])
                count += 1
     if count > 0:
      print(f"Math: {math_sum / count}")
      print(f"Physics: {physics_sum / count}")
      print(f"Chemistry: {chemistry_sum / count}")
calculator("students.csv")

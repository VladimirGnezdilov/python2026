
def mean_abs_deviation(*points):
    devegrent=[]
    if not points:
        raise ValueError("Нужно передать хотя бы один балл")
    avg = sum(points) / len(points)
    for point in points:
        devegrent.append(round(abs(avg-point), 1))
    return avg, tuple(devegrent)






print(mean_abs_deviation(3, 5, 7, 9))


existing_scores = [10, 8, 6]
print(mean_abs_deviation(*existing_scores))

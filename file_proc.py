
def read_data(input_file):
    x_points = []
    y_points = []
    with open(input_file) as f:
        for line in f:
            x, y = line.split()
            x_points.append(float(x))
            y_points.append(float(y))

    x_points = np.asarray(x_points)
    y_points = np.asarray(y_points)

    sorted_idx = np.argsort(x_points)

    return x_points[sorted_idx], y_points[sorted_idx]


def write_file(diff, error, conj, file_path):
    with open(file_path, "w+") as f:
        s = str(diff) + " " + str(error) + " " + str(conj) + "\n"
        f.write(s)
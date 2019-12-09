
def format_coords(coords):
    return [(val[0], int(val[1:])) for val in coords.split(",")]

DIRECTIONS = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

def find_points(paths):
    points = {}
    
    x = 0
    y = 0
    steps = 0

    for direction, distance in paths:
        for point in range(distance):
            x_change, y_change = DIRECTIONS[direction]
            x += x_change
            y += y_change
            steps += 1
            points[(x, y)] = steps

    return points


def intersections(points1, points2):
    return set(points1.keys()).intersection(set(points2.keys()))


def manhattan_distances(points):
    return [abs(x) + abs(y) for x, y in points]


def least_steps(intersections, points1, points2):
    return [points1[point] + points2[point] for point in intersections]


with open('/Users/jeorryb/Dropbox/AdventofCode_2019/day3/input.txt') as _file:
    paths1 = format_coords(_file.readline())
    points1 = find_points(paths1)

    paths2 = format_coords(_file.readline())
    points2 = find_points(paths2)

    intersections = intersections(points1, points2)

    # Part 1
    print(min(manhattan_distances(intersections)))

    # Part 2
    print(min(least_steps(intersections, points1, points2)))






# origin = (0, 0)

# def parse_dir(entry, start):
#     direction = entry[0]
#     length = int(entry[1:])
#     if direction == 'U':
#         end = (start[0], start[1] + length)
#     elif direction == 'R':
#         end = (start[0] + length, start[1])
#     elif direction == 'D':
#         end = (start[0], start[1] - length)
#     elif direction == 'L':
#         end = (start[0] - length, start[1])
#     return end

# w1_segments = []
# w2_segments = []
# start1 = origin
# start2 = origin

# for x in wire1:
#     end = parse_dir(x, start1)
#     line_seg = [start1, end]
#     w1_segments.append(line_seg)
#     start1 = end

# for x in wire2:
#     end = parse_dir(x, start2)
#     line_seg = [start2, end]
#     w2_segments.append(line_seg)
#     start2 = end

# def line_inter(seg1, seg2):
#     xdiff = (seg1[0][0] - seg1[1][0], seg2[0][0] - seg2[1][0])
#     ydiff = (seg1[0][1] - seg1[1][1], seg2[0][1] - seg2[1][1])

#     def det(a, b):
#         return a[0] * b[1] - a[1] * b[0]

#     div = det(xdiff, ydiff)
#     if div == 0:
#         return False
#     else:
#         d = (det(*seg1), det(*seg2))
#         x = det(d, xdiff) / div
#         y = det(d, ydiff) / div
#         return x, y

# intersects = []

# for i in w1_segments:
#     for j in w2_segments:
#         if line_inter(i, j):
#             x, y = line_inter(i, j)
#             intersects.append(((x, y), (i, j)))

# min_dist = min([abs(x[0][0]) + abs(x[0][1]) for x in intersects])
# print(min_dist)





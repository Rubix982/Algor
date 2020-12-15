INF = 100000
r = [0] + [-1*INF]*5


def max(x, y):
    if x > y:
        return x
    return y


def top_down_rod_cutting(c, n):
    global r
    if(r[n] >= 0):
        return r[n]

    maximum_revenue = -1*INF

    for i in range(1, n+1):
        maximum_revenue = max(
            maximum_revenue, c[i] + top_down_rod_cutting(c, n-i))

    r[n] = maximum_revenue
    return r[n]

# Driver code
# if __name__ == '__main__':
#     # list starting from 1, element at index 0 is fake
#     c = [0, 10, 24, 30, 40, 45]
#     print(top_down_rod_cutting(c, 5))

# See this link for more details https://www.codesdope.com/course/algorithms-rod-cutting/

from playLA.Vector import Vector


if __name__ == '__main__':

    vec = Vector([3, 2])
    print(vec[1])
    print(vec)
    print(len(vec))
    print("vec[0]={} vec[1]={}".format(vec[0], vec[1]))

    vec2 = Vector([5, 3])
    print("vec + vec2 = {}".format(vec + vec2))
    print("vec - vec2 = {}".format(vec2 - vec))
    print("3 * vec2 = {}".format(3 * vec2))
    print("-vec: {}, +vec: {}".format(-vec, +vec))
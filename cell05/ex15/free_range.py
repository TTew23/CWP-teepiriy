import sys


def main():
    if len(sys.argv) != 3:
        print("none")
    else:
        start, end = int(sys.argv[1]), int(sys.argv[2])
        values = list(range(start, end + 1))
        print(values)


if __name__ == "__main__":
    main()

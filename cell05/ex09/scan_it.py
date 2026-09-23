import sys


def main():
    if len(sys.argv) != 3:
        print("none")
        return
    keyword, string = sys.argv[1], sys.argv[2]
    count = string.count(keyword)
    if count == 0:
        print("none")
    else:
        print(count)


if __name__ == "__main__":
    main()

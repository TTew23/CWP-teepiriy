import sys


def main():
    if len(sys.argv) != 2:
        print("none")
        return
    zs = "".join(char for char in sys.argv[1] if char == "z")
    if not zs:
        print("none")
    else:
        print(zs)


if __name__ == "__main__":
    main()

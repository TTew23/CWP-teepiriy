# test   "c:/Users/Teepiya/OneDrive/Desktop/source code/work.vibe coding/gitpython/CWP-teepiriy/cell05/ex07/downcase_it.py" "this" "is"
import sys


def main():
    if len(sys.argv) == 2:
        print(sys.argv[1].lower())
    else:
        print("none")


if __name__ == "__main__":
    main()

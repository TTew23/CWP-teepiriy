#powershell test : py parameters.py "this" "is" "crazy" "there's" "everywhere!"#
import sys


def main():
    print(f"Number of parameters: {len(sys.argv) - 1}.")


if __name__ == "__main__":
    main()

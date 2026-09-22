def main():
    table = 0
    while table <= 10:
        line = f"Table of {table}:"
        multiplier = 0
        while multiplier <= 10:
            line += f" {table * multiplier}"
            multiplier += 1
        print(line)
        table += 1


if __name__ == "__main__":
    main()
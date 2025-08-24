import sys

def compute(n: int) -> int:
    return n * 2

def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else "1"
    try:
        n = int(arg)
    except ValueError:
        print("Invalid number, using 1")
        n = 1
    print(f"worker received n={n}")
    print(f"result: {compute(n)}")

if __name__ == "__main__":
    main()
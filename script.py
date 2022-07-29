from datetime import datetime

if __name__ == "__main__":
    print(f"\nINFO: This script was ran at {datetime.now()}\n")
    with open("../aux.txt", "w") as f:
        f.write(f"This script was ran at {datetime.now()}")

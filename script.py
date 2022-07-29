from datetime import datetime

if __name__ == "__main__":
    with open("aux.txt", "w") as f:
        f.write(f"This script was ran at {datetime.now()}")

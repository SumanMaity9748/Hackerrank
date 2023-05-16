import re

if __name__ == "__main__":
    str = input()
    match = re.search(r'([a-zA-Z0-9])\1+', str)
    
    print(match.group(1) if match else -1)

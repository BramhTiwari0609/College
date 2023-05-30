import re
for _ in range(int(input())):
    uid = input()
    uid = "".join(sorted(uid))
    if (re.search(r"[A-Z]{2}",uid) and 
        re.search(r"\d{3}",uid) and 
        not re.search(r"[^A-Za-z0-9]",uid) and 
        not re.search(r"(\w)\1",uid) and 
        len(uid) == 10):
        print("Valid")
    else:
        print("Invalid")

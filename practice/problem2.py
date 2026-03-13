def mask_string(s):
    n = len(s)
    all_digits = s.isdigit()

    if all_digits and n >= 6:
        s = list(s)
        for i in range(2, n - 4):
            s[i] = "*"
        return "".join(s)

    if all_digits and n < 6:
        return "*" * n

    if "@" in s:
        s = list(s)
        idx = s.index("@")
        for i in range(1, idx):
            s[i] = "*"
        return "".join(s).lower()
        

    return s




input = ["4539148803436467", "123", "JohnDoe@Visa.com", "hello-world"]

for i in input:
    print(mask_string(i))
    
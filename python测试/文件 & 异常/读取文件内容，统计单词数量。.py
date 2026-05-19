import re
from collections import Counter

with open("pile","r",encoding="utf-8") as f:
    total = f.read()
    words = re.findall(r"\b\w+\b",total.lower())
    count = len(words)
    couter_dict = Counter(words).most_common(count)
    print(count)
    print(couter_dict)
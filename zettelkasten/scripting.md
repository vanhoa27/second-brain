---
id: scripting
aliases:
  - Decripting sha256
tags: []
---
## Decripting sha256
- 6 digit sha256 codes are very easy to reverse
- data: january 18, 2024
- **Using this simple python script:**
```python
matrikelnummer = "<your sha256 code>"

for i in range (0, 500000):
    if hashlib.sha256(bytes(str(i), 'utf-8')).hexdigest() == matrikelnummer:
        print(str(i))
```
- to look at how long it takes: 
```bash
time python3 <script>
```



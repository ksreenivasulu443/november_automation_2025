
name = "hello"
[print(f"{i}:{name.count(i)}") for i in name]

count_of = []
for i in name:
    print(f"{i}:{name.count(i)}")
    count_of.append(f"{i}:{name.count(i)}")

print(count_of)
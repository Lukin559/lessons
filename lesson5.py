a = ["stroka", "toje stroka", "ne stroka", " pochti stroka"]
a.reverse()
print(a)
s = "--$--"
result = []
for i in a:
    result.append(i)
    result.append(s)

index = len(result) - 1
result.pop(index)
print(result)

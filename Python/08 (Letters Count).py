text = "hippo runs to us!"
text_dict = {}
for i in list(text):
    tane = text.count(i)
    text_dict[i] = tane
print(text_dict)

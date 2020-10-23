
def reverse_func(s):
    return s == s[::-1]
s = input("Enter a word:  ")

answer = reverse_func(s)

if answer:
    print("You get a point")
else:
    print("You don't get a point")



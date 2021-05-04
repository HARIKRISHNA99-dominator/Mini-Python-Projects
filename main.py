phone = input("phone: ")
digits = {
    "1" : "one",
    "2" : "two",
    "3" : "three"

}
for num in phone:
    print(digits.get(num,"!"))

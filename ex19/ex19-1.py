def ten_ways(num1, num2):
    print(f"What is {num1} + {num2} equal to?")
    print("It is", num1 + num2, "\n")


def pass_value():
    ten_ways(1, 2)

one = 1
two = 2

txt = open("test.txt")

ten_ways(1, 2)
ten_ways(one, two)
ten_ways(1 + 1, 2 + 2)
ten_ways(one + 1, two + 2)
ten_ways(int(input("Number One: ")), int(input("Number Two: ")))
ten_ways(txt.readline(), txt.readline())
pass_value()

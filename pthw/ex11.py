print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

print "First number?",
num1 = int(raw_input())
print "%r!\nSecond number?" % num1,
num2 = int(raw_input())
print "%r!\nResult: %r" % (num2, num1 + num2)
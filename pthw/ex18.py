# this one is like running a script with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# aparently *args is pretty pointless, we can just do this..

def print_two_again(arg1,arg2):
    print "arg1: %r, arg2: %r" % (arg1,arg2)

# this just take one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this takes no arguments
def print_none():
    print "I got nothin'."

print_two("Zed", "Shaw")
print_two_again("Zedd","Shaww")
print_one("First!")
print_none()

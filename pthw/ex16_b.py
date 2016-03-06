from sys import argv

script, filename = argv

print "We're going to read the file: %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename)

txt = target.read()
print "Here's the file: \n", txt
target.close()

print "We're going to truncate the file: %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")
target = open(filename, 'w')
#target.truncate()

print "Now I'm going to ask you for three lines."

line1, line2, line3 = raw_input("line 1: "), raw_input("line 2: "), raw_input("line 3: ")

print "I'm going to write to the file."

target.write("%s\n%s\n%s" % (line1, line2, line3))

print "And finally, we close it."
target.close()


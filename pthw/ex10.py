tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print "\\	Backslash (\)"
print "\'	Single-quote (')"
print "\"	Double-quote (\")"
print "\a	ASCII bell (BEL)"
print "\b	ASCII backspace (BS)"
print "\f	ASCII formfeed (FF)"
print "\n	ASCII linefeed (LF)"
#print "\N{1}	Character named name in the Unicode database (Unicode only)"
print "\r	Carriage Return (CR)"
print "\t	Horizontal Tab (TAB)"
#print "\u0000	Character with 16-bit hex value xxxx (Unicode only)"
#print '\12121212	Character with 32-bit hex value xxxxxxxx (Unicode only)'
#print "\v	ASCII vertical tab (VT)"
#print "\o0	Character with octal value ooo"
# print "\x00"
c = 0

while c < 10:
    for i in ["/","-","|","\\","|"]:
        print '%s' % i,
        c +=1
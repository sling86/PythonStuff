from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

indata = open(from_file).read()

print ("The input for the file is %d bytes long\n"
       "Does the output file exist? %r\n"
       "CTRL-C to abort.") % (len(indata), exists(to_file))
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()

import sqlite3
# import sys
import re
import time
import getpass

conn = sqlite3.connect('../SRC.sql')
c = conn.cursor()

# f = open(sys.argv[0])
f = open('../Source_festival.txt', 'r')
f2 = open('../logs/Build-festival.log', 'w')

f2.write('Build BY: %s\n' % getpass.getuser())
f2.write('Build time: %s\n' % time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
f2.write('Convert from: %s\n' % 'Source_festival.txt')
f2.write('Convert into: %s\n' % 'Festival')
f2.write('Flied: %s\n' % 'Festival name, Date')
f2.write(('-'*20) + '\n')

# f2.write('Convert from: %s' % sys.argv[0])
# f2.write('Convert into: %s' % sys.argv[1])
# f2.write('Flied: %s' % sys.argv[2])

c.execute("DELETE FROM Festival")
# c.execute("DELETE FROM %s" % sys.argv[1])

for line in f.readlines():
    line_BEAT = line.split(' ')
    line_BEAT[1] = line_BEAT[1].replace('(','')
    line_BEAT[1] = line_BEAT[1].replace(')','')
    # Command = "INSERT INTO %s (%s) VALUES ('%s', '%s')" % (sys.argv[1], sys.argv[2], line_BEAT[0], line_BEAT[1])
    Command = "INSERT INTO %s (%s) VALUES ('%s', '%s')" % ('Festival', "'Festival name','Date'", line_BEAT[0], line_BEAT[1])
    f2.write(Command + '\n')
    c.execute(Command)
    pass

f2.write(('-'*20) + '\n')
f.close()
f2.close()
conn.commit()
conn.close()
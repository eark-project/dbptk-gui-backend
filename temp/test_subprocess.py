from subprocess import call, Popen, PIPE
import new

command = ['java', '-jar', '/home/andreas/eark/db-preservation-toolkit/dbptk-core/target/dbptk-app-2.0.0-rc3.2.5.jar', '-i', 'mysql', '-ih', 'localhost',
           '-idb', 'sakila', '-iu', 'andreas', '-ip', 'hemmeligt', '-e', 'siard-dk', '-ef', '/tmp/AVID.MAG.1000.1']


command = ['sleep', '5']
command = ['ls','-l']

p = Popen(command, stdout = PIPE, stderr= PIPE)

raise

print 'Hurra'

term = None
while term == None:
    term = p.poll()
    if term == None:
        print 'Not done'
    else:
        print 'Done'
        
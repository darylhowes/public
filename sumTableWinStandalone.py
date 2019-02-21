#!python3

import os, numpy

#os.chdir('data')
#os.getcwd()

for dirs, subs, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith('dat'):
            data = numpy.genfromtxt(file, delimiter='')
                       
            col1 = data[:,1]
            col2 = data[:,2]
            col3 = data[:,3]

            max_col1 = numpy.max(col1)
            max_col2 = numpy.max(col2)
            max_col3 = numpy.max(col3)

            avg = numpy.average((max_col1, max_col2, max_col3))
            print ("\n" + file)
            print ("Max1: " + str(max_col1) + " Max2: " + str(max_col2) + " Max3: " + str(max_col3))
            print ("Average: " + str(numpy.average((max_col1, max_col2, max_col3))))



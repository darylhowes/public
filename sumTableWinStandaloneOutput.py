#! python3

import os, numpy

#os.chdir('data')
#os.getcwd()
outfile=open('AVG-results.txt','w')

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
            outfile.write('%s, %10.4f,  Max1, %10.4f, Max2, %10.4f, Max3, %10.4f\n' % (file,avg,max_col1,max_col2,max_col3))
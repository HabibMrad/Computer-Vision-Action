
# coding:utf-8

import kMeans

from  numpy import *

datMat=mat(kMeans.loadDataSet('testSet.txt'))
print datMat[1:5,:]


myCentroids,clustAssing=kMeans.kMeans(datMat,4)
print myCentroids
print ' '
print clustAssing

datMat3=mat(kMeans.loadDataSet('testSet2.txt'))
centList,myNewAssments=kMeans.biKmeans(datMat3,3)
print centList,myNewAssments
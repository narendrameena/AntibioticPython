#author narumeena 
#description annotating all arraexpress probes with locun and genes 


## try http:// if https:// URLs are not supported
source("https://bioconductor.org/biocLite.R")
biocLite("ArrayExpress")

library(ArrayExpress)
AEset = ArrayExpress("E-GEOD-6836")
library("affy")

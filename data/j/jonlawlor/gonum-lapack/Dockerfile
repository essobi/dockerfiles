FROM jonlawlor/gonum-blas:1.3.3  
MAINTAINTER Jonathan J Lawlor <jonathan.lawlor@gmail.com>  
# note: this uses OpenBLAS, and Ubuntu linux  
# gonum's lapack  
RUN go get github.com/gonum/lapack  
RUN cd /gopath/src/github.com/gonum/lapack/clapack/ && perl genLapack.pl
-L/opt/OpenBLAS/lib -lopenblas  


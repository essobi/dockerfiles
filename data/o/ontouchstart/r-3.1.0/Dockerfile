FROM debian:sid  
MAINTAINER Sam Liu <ontouchstart@gmail.com>  
  
RUN apt-get update -qq -y  
RUN apt-get install g++ make gfortran libsuitesparse-dev libncurses5-dev
libopenblas-dev liblapack-dev libarpack2-dev libfftw3-dev libgmp-dev
libpcre3-dev libreadline-dev libdouble-conversion-dev curl -y  
  
RUN curl -O http://cran.r-project.org/src/base/R-3/R-3.1.0.tar.gz  
RUN tar -xzvf R-3.1.0.tar.gz  
RUN cd R-3.1.0 && ./configure --with-x=no && make && make install  


FROM ubuntu:latest  
MAINTAINER Sam Liu <ontouchstart@gmail.com>  
# Based on
https://github.com/JuliaLang/julia/blob/master/contrib/vagrant/Vagrantfile  
RUN apt-get update -qq -y  
RUN apt-get install python-software-properties -y  
RUN add-apt-repository ppa:staticfloat/julia-deps -y  
RUN apt-get update -qq -y  
RUN apt-get install g++ git make patchelf gfortran llvm-3.3 libsuitesparse-dev
libncurses5-dev libopenblas-dev liblapack-dev libarpack2-dev libfftw3-dev
libgmp-dev libpcre3-dev libunwind7-dev libreadline-dev libdouble-conversion-
dev libopenlibm-dev librmath-dev libmpfr-dev wget curl -y  
  
ENV LANG C.UTF-8  
RUN git clone https://github.com/JuliaLang/julia.git  
RUN cd julia && git checkout v0.2.1 && make LLVM_CONFIG=llvm-config-3.3
USE_BLAS64=0 USE_SYSTEM_LLVM=1 USE_SYSTEM_ZLIB=1 USE_SYSTEM_SUITESPARSE=1
USE_SYSTEM_ARPACK=1 USE_SYSTEM_BLAS=1 USE_SYSTEM_FFTW=1 USE_SYSTEM_LAPACK=1
USE_SYSTEM_GMP=1 USE_SYSTEM_MPFR=1 USE_SYSTEM_PCRE=1 USE_SYSTEM_LIBUNWIND=1
USE_SYSTEM_READLINE=1 USE_SYSTEM_GRISU=1 USE_SYSTEM_OPENLIBM=1
USE_SYSTEM_RMATH=1 JULIA_CPU_TARGET=core2  
ENTRYPOINT ["/julia/julia"]  


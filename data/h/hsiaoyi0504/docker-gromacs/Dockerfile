FROM ubuntu:14.04  
MAINTAINER Yi Hsiao <hsiaoyi0504@gmail.com>  
ENV GROMACS_VERSION 5.1.2  
RUN apt-get update && apt-get install -y \  
build-essential \  
wget \  
cmake \  
&& wget ftp://ftp.gromacs.org/pub/gromacs/gromacs-${GROMACS_VERSION}.tar.gz  
RUN tar zxfv gromacs-${GROMACS_VERSION}.tar.gz  
WORKDIR "./gromacs-${GROMACS_VERSION}/"  
RUN mkdir build  
WORKDIR "./build"  
RUN cmake .. -DGMX_BUILD_OWN_FFTW=ON -DREGRESSIONTEST_DOWNLOAD=ON  
RUN make  
RUN make check  
RUN make install  
WORKDIR "/"  
RUN ["/bin/bash","-c","source /usr/local/gromacs/bin/GMXRC"]  
CMD ["gmx","-version"]  
CMD echo "Welcome to Gromacs 5.1.2"  


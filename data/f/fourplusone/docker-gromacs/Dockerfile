FROM debian:jessie  
RUN apt-get update && apt-get install -y wget  
  
RUN wget ftp://ftp.gromacs.org/pub/gromacs/gromacs-5.0.4.tar.gz  
  
RUN echo "c177ae5fd6d71e2bec7369bc66cd082e gromacs-5.0.4.tar.gz" > MD5SUM  
RUN md5sum -c MD5SUM  
RUN tar -xf gromacs-5.0.4.tar.gz  
  
RUN apt-get update && apt-get install -y build-essential cmake file
libxml2-dev libboost-dev  
  
WORKDIR gromacs-5.0.4  
RUN mkdir build  
WORKDIR build  
RUN cmake .. -DGMX_BUILD_OWN_FFTW=ON -DREGRESSIONTEST_DOWNLOAD=ON  
RUN make -j `nproc`  
  
# Don't run make check, since mdrun won't work on dockers build servers  
# RUN make check  
RUN make install  
  
WORKDIR /root  
RUN echo source /usr/local/gromacs/bin/GMXRC >> .profile  
  
CMD /bin/bash -l


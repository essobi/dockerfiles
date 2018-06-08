FROM ubuntu:16.04  
RUN apt-get update  
RUN apt-get install -y build-essential debhelper autotools-dev autoconf
automake make cmake nano gcc-4.9  
RUN apt-get install -y unzip wget net-tools git libtool flex bison gperf gawk
m4 libssl-dev libreadline-dev libreadline-dev openssl python-pip  
  
RUN wget http://glaros.dtc.umn.edu/gkhome/fetch/sw/metis/metis-5.1.0.tar.gz  
RUN tar -xvf metis-5.1.0.tar.gz  
  
RUN cd /metis-5.1.0 && make config cc=gcc-4.9 && make && make install  
  
RUN mkdir /data  
WORKDIR /data  
  
CMD ["tail", "-f", "/dev/null"]  
  


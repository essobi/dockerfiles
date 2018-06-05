FROM ubuntu:xenial  
MAINTAINER Daniel P. Foose <dpfoose@gmail.com>  
RUN mkdir -p /usr/dependencies  
COPY . /usr/dependencies  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get -y update  
RUN apt-get -y --no-install-recommends install apt-utils git wget unzip
liblapack-dev build-essential cmake \  
libhdf5-10 vim nano libhdf5-cpp-11 libhdf5-dev libxml2-dev zlib1g zlib1g-dev
libsz2 libboost-all-dev \  
openssh-server libopenblas-dev  
RUN mkdir /var/run/sshd  
  
RUN echo '/usr/lib/libopenblas.so /usr/lib/libblas.so' > /etc/ld.so.preload  
  
RUN cd /usr/dependencies && \  
wget --no-check-certificate https://github.com/BiRG/bioinf-
docker/releases/download/1/armadillo-7.800.1.tar.xz && \  
tar xvf armadillo-7.800.1.tar.xz && \  
mkdir armadillo-7.800.1/build && cd armadillo-7.800.1/build && \  
cmake .. && \  
make && make install  
  
# compile mlpack  
RUN cd /usr/dependencies && \  
wget http://mlpack.org/files/mlpack-2.1.1.tar.gz &&\  
tar xvf mlpack-2.1.1.tar.gz && \  
mkdir mlpack-2.1.1/build && cd mlpack-2.1.1/build &&\  
cmake .. -DBUILD_TESTS:BOOL=OFF -DBUILD_CLI_EXECUTABLES:BOOL=OFF && \  
make && make install  
  
# install the library part of Vespucci  
RUN cd /usr/dependencies && \  
wget --no-check-certificate
https://github.com/VespucciProject/Vespucci/archive/master.zip && \  
unzip master.zip && \  
rm master.zip && \  
cd Vespucci-master && \  
mkdir build && cd build && \  
cmake .. -DBUILD_GUI=OFF && \  
make && make install  
  
# install Anaconda  
RUN cd /usr/dependencies && \  
wget --no-check-certificate
https://repo.continuum.io/archive/Anaconda3-4.3.1-Linux-x86_64.sh  
RUN bash /usr/dependencies/Anaconda3-4.3.1-Linux-x86_64.sh -b -p /opt/anaconda  
RUN chmod +x /usr/dependencies/install_python_packages.sh &&
./usr/dependencies/install_python_packages.sh  
  
#Julia  
RUN apt-get -y install julia  
  
#clean up  
RUN rm -rf /usr/dependencies  


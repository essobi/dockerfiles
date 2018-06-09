FROM docker.repository.cloudera.com/cdsw/engine:4  
RUN echo "cdsw ALL=(ALL:ALL) NOPASSWD: ALL" >> /etc/sudoers  
RUN apt-get install -y libatlas-base-dev python-dev gfortran pkg-config
libfreetype6-dev  
RUN wget https://downloads.sourceforge.net/project/ta-lib/ta-lib/0.4.0/ta-
lib-0.4.0-src.tar.gz  
RUN tar -zxvf ta-lib-0.4.0-src.tar.gz  
  
RUN cd ta-lib && \  
./configure --prefix=/usr && \  
make && \  
make install  


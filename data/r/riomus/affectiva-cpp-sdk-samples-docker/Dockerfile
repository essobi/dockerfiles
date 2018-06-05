FROM ubuntu:14.04  
MAINTAINER Roman Bartusiak <riomus@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -yqq update && apt-get install -y --force-yes \  
build-essential libopencv-dev libboost1.55-all-dev cmake git curl vim strace
gdb libssl-dev wget&& \  
apt-get autoremove -y && apt-get clean  
  
## Build OpenCV  
RUN cd /tmp && wget https://download.affectiva.com/linux/affdex-cpp-
sdk-3.1.1-2802-linux-64bit.tar.gz && \  
mkdir /opt/affdex-sdk && tar -xzvf affdex-cpp-
sdk-3.1.1-2802-linux-64bit.tar.gz -C /opt/affdex-sdk  
  
ENV AFFDEX_DATA_DIR=/opt/affdex-sdk/data  
ENV LD_LIBRARY_PATH=/opt/affdex-sdk/lib:${LD_LIBRARY_PATH}  
ENV SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt  
  
  
##Affectiva example  
RUN git clone https://github.com/Affectiva/cpp-sdk-samples.git  
RUN cd cpp-sdk-samples && cmake -DOpenCV_DIR=/usr/ -DBOOST_ROOT=/usr/
-DAFFDEX_DIR=/opt/affdex-sdk .  
RUN cd cpp-sdk-samples && make  
  
WORKDIR cpp-sdk-samples  
  
ENTRYPOINT bash  


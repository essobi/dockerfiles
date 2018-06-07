FROM tutum/ubuntu:trusty  
  
MAINTAINER Michael Sevilla <mikesevilla3@gmail.com>  
  
# install deps  
RUN echo "===> Installing swift stuff..."  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
apt-get install -y \  
git \  
build-essential \  
libcurl4-openssl-dev \  
libxml2-dev \  
libssl-dev \  
libfuse-dev \  
libjson-c-dev && \  
DEBIAN_FRONTEND=noninteractive apt-get remove -y python-pip && \  
DEBIAN_FRONTEND=noninteractive apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN echo "===> Getting the code..." && \  
git clone https://github.com/redbo/cloudfuse.git && \  
cd cloudfuse && \  
./configure && make && make install  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod 750 /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  


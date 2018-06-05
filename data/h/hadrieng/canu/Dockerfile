FROM hadrieng/docker_base  
  
MAINTAINER Hadrien Gourlé <gourlehadrien@gmail.com>  
  
# install java-1.8  
RUN echo 'deb http://ftp.de.debian.org/debian jessie-backports main' \  
>> /etc/apt/sources.list && \  
apt-get update --fix-missing && \  
apt install -y -t jessie-backports \  
openjdk-8-jre-headless \  
ca-certificates-java \  
openjdk-8-jdk && \  
/usr/sbin/update-java-alternatives -s java-1.8.0-openjdk-amd64  
  
# install canu  
RUN git clone https://github.com/marbl/canu.git && \  
cd canu/src && \  
make  
  
ENV PATH /canu/Linux-amd64/bin/:$PATH  


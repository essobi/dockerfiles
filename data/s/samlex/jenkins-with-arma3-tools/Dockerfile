### Versions of external tools  
ARG DEPBO_VERSION=0.6.77  
ARG SQFLINT_VERSION=0.3.1  
### Build stage to download DePBO tools  
FROM buildpack-deps:stretch-curl as PBO  
  
ARG DEPBO_VERSION  
  
## Download and unpack tools  
RUN curl -L https://armaservices.maverick-
applications.com/Products/MikerosDosTools/DownloadFree.aspx?download=depbo-
tools-${DEPBO_VERSION}-linux-64bit.tgz -o /root/depbo.tgz && \  
tar xf /root/depbo.tgz -C /root && \  
mv /root/depbo-tools-${DEPBO_VERSION} /root/depbo-tools && \  
chmod +x /root/depbo-tools/bin/*  
  
### Actual Jenkins image  
FROM jenkins/jenkins:2.107.3  
MAINTAINER samlex <samlex@gmx.com>  
LABEL maintainer="samlex <samlex@gmx.com>"  
  
ARG SQFLINT_VERSION  
  
USER root  
  
## Download SQFLint and DePBO tools dependencies  
RUN apt-get update && \  
apt-get -y --no-install-recommends install python3-pip liblzo2-2 libvorbis0a
libvorbisfile3 libvorbisenc2 libogg0 && \  
pip3 install --no-cache-dir sqflint==${SQFLINT_VERSION} && \  
apt-get -y purge python3-pip && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
## Copy DePBO tools from build stage  
COPY \--from=PBO /root/depbo-tools/bin/* /usr/bin/  
COPY \--from=PBO /root/depbo-tools/lib/* /usr/lib/  
  
## Copy custom scripts  
COPY bin/*.bash /usr/bin/  
  
USER jenkins  
  
## Install Warnings plugin and copy across custom parser  
RUN /usr/local/bin/install-plugins.sh warnings  
COPY config/*.xml /usr/share/jenkins/ref/  


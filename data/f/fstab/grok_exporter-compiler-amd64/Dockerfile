FROM centos:6  
MAINTAINER Fabian Stäber, fabian@fstab.de  
  
#------------------------------------------------------------------------------  
# Why centos:6  
#------------------------------------------------------------------------------  
# When compiled on current Linux versions, grok_exporter requires GLIBC_2.14,  
# see output of 'objdump -p grok_exporter'. The reason is a call to memcpy,  
# see output of 'objdump -T grok_exporter | grep GLIBC_2.14'.  
# Centos 6 does not provide GLIBC_2.14. In order to make grok_exporter work on  
# old Linux distributions, we compile it on Centos 6 to make sure it doesn't  
# accidentally require a newer GLIBC version.  
#------------------------------------------------------------------------------  
# Edit the LAST_UPDATE variable to force re-run of 'yum update' when building  
# the Docker image  
ENV LAST_UPDATE=2018-05-31  
RUN yum clean all && \  
yum update -y  
  
WORKDIR /root  
  
#------------------------------------------------------------------------------  
# Basic tools  
#------------------------------------------------------------------------------  
RUN yum install -y \  
curl \  
git \  
wget \  
vim  
  
#------------------------------------------------------------------------------  
# Go development  
#------------------------------------------------------------------------------  
# Install golang manually, so we get the latest version.  
RUN cd /usr/local && \  
curl -sLO https://dl.google.com/go/go1.10.2.linux-amd64.tar.gz && \  
tar xfz go1.10.2.linux-amd64.tar.gz && \  
rm go1.10.2.linux-amd64.tar.gz && \  
cd /root && \  
mkdir -p go/bin go/pkg  
  
ENV GOROOT="/usr/local/go" \  
GOPATH="/root/go"  
ENV PATH="${GOROOT}/bin:${PATH}"  
ENV PATH="${GOPATH}/bin:${PATH}"  
#------------------------------------------------------------------------------  
# Create a statically linked Oniguruma library for Windows amd64  
#------------------------------------------------------------------------------  
# Install compiler and cross-compile Oniguruma for mingw  
# This will create /usr/x86_64-w64-mingw32/lib/libonig.a  
RUN yum install -y epel-release && \  
yum install -y gcc mingw64-gcc && \  
cd /tmp && \  
curl -sLO
https://github.com/kkos/oniguruma/releases/download/v5.9.6/onig-5.9.6.tar.gz
&& \  
tar xfz onig-5.9.6.tar.gz && \  
rm onig-5.9.6.tar.gz && \  
cd /tmp/onig-5.9.6 && \  
CC=x86_64-w64-mingw32-gcc ./configure --host x86_64-w64-mingw32
--prefix=/usr/x86_64-w64-mingw32 && \  
CC=x86_64-w64-mingw32-gcc make && \  
CC=x86_64-w64-mingw32-gcc make install && \  
cd /root && \  
rm -r /tmp/onig-5.9.6  
  
#------------------------------------------------------------------------------  
# Create a statically linked Oniguruma library for Linux amd64  
#------------------------------------------------------------------------------  
# This will create /usr/local/lib/libonig.a  
RUN cd /tmp && \  
curl -sLO
https://github.com/kkos/oniguruma/releases/download/v5.9.6/onig-5.9.6.tar.gz
&& \  
tar xfz onig-5.9.6.tar.gz && \  
rm onig-5.9.6.tar.gz && \  
cd /tmp/onig-5.9.6 && \  
./configure && \  
make && \  
make install && \  
cd /root && \  
rm -r /tmp/onig-5.9.6  
  
#------------------------------------------------------------------------------  
# Create compile scripts  
#------------------------------------------------------------------------------  
COPY check-if-gopath-available.sh compile-linux.sh compile-windows-amd64.sh
/root/  
  
CMD /root/check-if-gopath-available.sh && echo "Type 'ls' to see the available
compile scripts." && exec /bin/bash  


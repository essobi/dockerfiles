# installing Virtuoso  
#  
# VERSION 0.1  
# Pull base image.  
FROM dockerfile/ubuntu  
  
# :)  
MAINTAINER Tazro Inutano Ohta, inutano@gmail.com  
  
# Install packages.  
RUN apt-get update && \  
apt-get install -y automake gperf libtool flex bison libssl-dev && \  
rm -rf /var/lib/apt/lists/*  
# Install virtuoso  
ENV VIRTUOSO_VERSION develop/7  
RUN \  
cd /tmp && \  
git clone https://github.com/openlink/virtuoso-opensource.git && \  
cd virtuoso-opensource && \  
git checkout $VIRTUOSO_VERSION && \  
./autogen.sh && \  
export CFLAGS="-O2 -m64" && \  
./configure && \  
make && \  
make install && \  
rm -fr /tmp/virtuoso-opensource  
  
# Define working directory.  
WORKDIR /data  
  
# Start Virtuoso  
WORKDIR /usr/local/virtuoso-opensource/var/lib/virtuoso/  
RUN \  
chown -R `whoami` db  
  
# Define default command.  
WORKDIR /usr/local/virtuoso-opensource/var/lib/virtuoso/db  
CMD ["/usr/local/virtuoso-opensource/bin/virtuoso-t","+foreground"]  
  
# Expose ports.  
# - 8890: HTTP  
EXPOSE 8890  


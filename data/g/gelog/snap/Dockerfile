  
# Builds from an official Docker image  
FROM ubuntu:14.04.1  
# Installing Make, G++, and wget  
# (wget is required to download the snap package)  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y make g++ wget && \  
rm -rf /var/lib/apt/lists/*  
  
# Environment variables  
ENV ZLIB_VERSION 1.2.8  
ENV SNAP_VERSION 1.0beta.15  
ENV SNAP_HOME /usr/local/snap  
  
  
# Installing ZLIB  
RUN wget http://zlib.net/zlib-$ZLIB_VERSION.tar.gz && \  
tar -xzf /zlib-$ZLIB_VERSION.tar.gz -C /usr/local/ && \  
rm /zlib-$ZLIB_VERSION.tar.gz && \  
ln -s /usr/local/zlib-$ZLIB_VERSION /usr/local/zlib && \  
cd /usr/local/zlib && \  
./configure && \  
make  
# Docker's RUN command prepends 'sh -c' to the RUN instruction, which caues
the error  
#  
# /bin/sh: 1: : not found  
#  
# This forces us to do the 'make install' in a separate RUN instruction  
# Using the brackets does not prepend 'sh -c'  
#  
RUN ["make", "-C", "/usr/local/zlib", "install"]  
  
# Installing Snap  
RUN wget http://snap.cs.berkeley.edu/downloads/snap-$SNAP_VERSION-linux.tar.gz
&& \  
tar -xzf /snap-$SNAP_VERSION-linux.tar.gz -C /usr/local/ && \  
rm /snap-$SNAP_VERSION-linux.tar.gz && \  
ln -s /usr/local/snap-$SNAP_VERSION-linux /usr/local/snap && \  
ln -s /usr/local/snap/snap /usr/bin/snap  
  
# Define the default command  
ENTRYPOINT ["snap"]  
  


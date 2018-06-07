#####################  
# Bench Dockerfile #  
#####################  
  
# Set the base image  
FROM ubuntu:16.04  
  
# File Author / Maintainer  
MAINTAINER Toon Lamberigts and Tomas Vercautter, Jerry Park <jaehwa@gmail.com>  
  
# Install dependencies  
RUN apt-get update && apt-get install -y make gcc g++ libtool perl libpopt0
libpopt-dev m4 wget autoconf php-cli php-xml unzip build-essential mesa-utils
apt-file apt-utils libaio-dev libpcre3-dev expat libexpat1-dev python
python3-pip  
  
# Download & extract Phoronix package  
RUN wget http://phoronix-test-suite.com/releases/phoronix-test-
suite-7.6.0.tar.gz -O phoronix-test-suite.tar.gz && \  
tar xzf phoronix-test-suite.tar.gz && \  
rm -f phoronix-test-suite.tar.gz && \  
cd phoronix-test-suite && ./install-sh  
  
# Install predefined tests  
## Disk  
RUN phoronix-test-suite install pts/iozone && \  
phoronix-test-suite install pts/dbench && \  
#RUN phoronix-test-suite install pts/fs-mark  
phoronix-test-suite install pts/tiobench && \  
phoronix-test-suite install pts/aio-stress && \  
## CPU  
phoronix-test-suite install pts/c-ray && \  
## Memory  
phoronix-test-suite install pts/stream && \  
## Network  
#RUN phoronix-test-suite install pts/netperf  
#RUN phoronix-test-suite install pts/iperf  
## Services  
phoronix-test-suite install pts/apache && \  
phoronix-test-suite install pts/redis  
#RUN phoronix-test-suite install pts/tensorflow  
  
# Copy custom scripts  
COPY scripts/ .  
  
# Begin benchmark script  
CMD ./run.sh  


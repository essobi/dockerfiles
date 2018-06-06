FROM ubuntu  
  
MAINTAINER Jeltje van Baren, jeltje.van.baren@gmail.com  
  
# Created this after FINALLY figuring out how to install vcftools.  
RUN apt-get update && apt-get install -y \  
git \  
make \  
automake \  
g++ \  
zlib1g-dev \  
pkgconf  
  
WORKDIR /opt  
  
RUN git clone https://github.com/vcftools/vcftools.git &&\  
cd vcftools &&\  
./autogen.sh &&\  
./configure &&\  
make &&\  
make install  
  
RUN mkdir /data  
WORKDIR /data  
  
# And clean up  
#RUN apt-get clean && rm -rf /var/lib/apt/lists/* && rm -rf /opt/vcftools  


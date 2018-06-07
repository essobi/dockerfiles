FROM insecurity/debian-32bit:latest  
MAINTAINER Vecten Sebastien <jtof_fap@insecurity.fr>  
  
# Set variables  
ENV GOLANG_DL_PATH /usr/local  
ENV GOLANG_INST_PATH $GOLANG_DL_PATH/go  
ENV GOLANG_VERSION 1.6.3  
ENV GOLANG_URL
https://bitbucket.org/jtof_fap/golang-32bit-x87/raw/master/go$GOLANG_VERSION-x87.tgz  
  
# 32Bit-x87 compatibility variables  
ENV GOARCH 386  
ENV GOOS linux  
ENV GO386 387  
ENV GOARM 5  
# Install build dependencies  
RUN LC_ALL=C DEBIAN_FRONTEND=noninteractive \  
&& apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates \  
g++ \  
gcc \  
libc6-dev \  
make \  
curl \  
  
# Get Golang x87 compiled version \  
&& cd $GOLANG_DL_PATH \  
&& curl -fSsl $GOLANG_URL -o go$GOLANG_VERSION-x87.tgz \  
&& tar -xzvf go$GOLANG_VERSION-x87.tgz \  
&& rm go$GOLANG_VERSION-x87.tgz \  
  
# Clean-up \  
&& apt-get autoclean \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV GOROOT $GOLANG_INST_PATH/bin  
ENV PATH $GOROOT:$PATH  
  
WORKDIR $GOLANG_INST_PATH  
  
COPY go-wrapper /usr/local/bin/  
  


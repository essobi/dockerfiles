FROM alpine:3.4  
MAINTAINER Nabil Servais "nabil@eml.cc"  
RUN apk update && \  
apk add --no-cache build-base git perl zlib-dev && \  
git clone https://github.com/rbsec/sslscan.git && \  
cd sslscan && \  
make static && \  
make install && \  
cd / && \  
rm -rf sslscan && \  
apk del build-base git perl zlib-dev  
  
ENTRYPOINT ["/usr/bin/sslscan"]  


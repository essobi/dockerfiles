FROM alpine:3.6  
MAINTAINER Klaus Umbach <klaus+docker@uxix.de>  
  
RUN apk add --no-cache build-base git perl zlib-dev libc6-compat && \  
git clone -b 1.11.8-rbsec https://github.com/rbsec/sslscan.git && \  
cd sslscan && \  
make static && make install && \  
cd / && rm -rf sslscan && \  
apk del build-base git perl zlib-dev libc6-compat  
  
USER nobody  
ENTRYPOINT ["/usr/bin/sslscan"]  


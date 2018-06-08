FROM alpine:3.4  
MAINTAINER Frank Monnerjahn <themonnie@gmail.com>  
  
ENV PEN_VERSION="0.33.2"  
RUN apk update update && \  
apk add --no-cache g++ make && \  
cd /tmp/ && wget -O - "http://siag.nu/pub/pen/pen-$PEN_VERSION.tar.gz" | tar
zx && \  
cd "/tmp/pen-$PEN_VERSION" && \  
./configure && \  
make -j && \  
make install && \  
apk --purge del g++ make wget && \  
rm -rf /tmp/*  
  
ENTRYPOINT ["/usr/local/bin/pen", "-f"]  


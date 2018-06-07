FROM azul/zulu-openjdk-alpine:8  
MAINTAINER "thanhbv" <thanhbv@sandinh.net>  
  
WORKDIR /opt/helix  
  
ARG HELIX_VERSION=0.6.8  
RUN addgroup -S -g 500 helix && \  
adduser -S -D -G helix -u 500 -h /opt/helix -s /bin/sh helix && \  
wget -O helix-core.tar --progress=bar:force:noscroll
http://www.apache.org/dist/helix/$HELIX_VERSION/binaries/helix-
core-${HELIX_VERSION}-pkg.tar && \  
tar xf helix-core.tar --strip-components=1 && \  
rm -r helix-core.tar bin/*.bat  
  
ENV PATH=$PATH:/opt/helix/bin  
  
USER helix  


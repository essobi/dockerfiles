FROM rawmind/rancher-base:0.0.2-1  
MAINTAINER Raul Sanchez <rawmind@gmail.com>  
  
#Set environment  
ENV VAMP_VERSION=0.8.4 \  
VAMP_HOME=/opt/vamp \  
GOROOT=/usr/lib/go \  
GOPATH=/opt/src \  
GOBIN=/gopath/bin  
ENV VAMP_RELEASE=vamp-gateway-agent_${VAMP_VERSION}_linux_amd64.zip  
  
# Install compile and install vamp-gateawy-agent  
RUN apk add --update git && \  
mkdir -p /opt/src; cd /opt/src && \  
git clone -b ${VAMP_VERSION} https://github.com/magneticio/vamp-gateway-
agent.git && \  
tar xzf vamp-gateway-agent/1.6.3/alpine/3.3/vamp.tar.gz -C /opt && \  
rm -rf /opt/src/vamp-gateway-agent && \  
apk del git  
  
# Install haproxy  
RUN apk --update add musl-dev linux-headers curl gcc pcre-dev make zlib-dev &&
\  
mkdir /usr/src && \  
curl -fL http://www.haproxy.org/download/1.6/src/haproxy-1.6.3.tar.gz | tar
xzf - -C /usr/src && \  
cd /usr/src/haproxy-1.6.3 && \  
make TARGET=linux2628 USE_PCRE=1 USE_ZLIB=1 && \  
make install-bin && \  
cd .. && \  
rm -rf /usr/src/haproxy-1.6.3 && \  
apk del musl-dev linux-headers curl gcc pcre-dev make zlib-dev && \  
apk add musl pcre zlib && \  
rm /var/cache/apk/*  
  
# Add start.sh  
ADD start.sh /usr/bin/start.sh  
RUN chmod +x /usr/bin/*.sh  
  
WORKDIR /opt/vamp  
  
ENTRYPOINT /usr/bin/start.sh  


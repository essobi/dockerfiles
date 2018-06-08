# Use alpine tag 3.4, as base image  
FROM alpine:3.4  
# Set maintainer info  
MAINTAINER Rob Timmer <rob@robtimmer.com>  
  
# Environment variables  
ENV GOROOT=/usr/lib/go \  
GOPATH=/go \  
PATH=$PATH:$GOROOT/bin:$GOPATH/bin \  
XMLSTARLET_VERSION=1.6.1-r1  
  
# Add start script  
ADD start.sh /  
  
# Setup Syncthing  
RUN \  
# Set right permissions to start script  
chmod +x /start.sh && \  
  
# Install dependencies  
apk add \--no-cache libxml2 libxslt && \  
apk add --no-cache --virtual .build-dependencies curl jq git go ca-
certificates && \  
  
# Download, compile and install Syncthing  
VERSION=`curl -s
https://api.github.com/repos/syncthing/syncthing/releases/latest | jq -r
'.tag_name'` && \  
mkdir -p /go/src/github.com/syncthing && \  
cd /go/src/github.com/syncthing && \  
git clone https://github.com/syncthing/syncthing.git && \  
cd syncthing && \  
git checkout $VERSION && \  
go run build.go && \  
mkdir -p /go/bin && \  
mv bin/syncthing /go/bin/syncthing && \  
  
# Cleanup  
rm -rf /go/pkg && \  
rm -rf /go/src && \  
apk del .build-dependencies  
  
# Define volumes by path  
VOLUME ["/data/config"]  
  
# Expose required ports  
EXPOSE 8384 22000 21027/udp  
  
# Set the command to the start script  
CMD ["/start.sh"]  


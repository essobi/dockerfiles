# https://hub.docker.com/_/golang  
FROM golang:1.10-alpine  
  
MAINTAINER Instrumentisto Team <developer@instrumentisto.com>  
  
  
RUN apk add \--update \--no-cache \  
ca-certificates \  
# https://github.com/Masterminds/glide#supported-version-control-systems  
git mercurial subversion bzr \  
openssh \  
&& update-ca-certificates \  
\  
# Install build dependencies  
&& apk add \--no-cache --virtual .build-deps \  
curl make \  
\  
# Download and unpack Glide sources  
&& curl -L -o /tmp/glide.tar.gz \  
https://github.com/Masterminds/glide/archive/v0.13.1.tar.gz \  
&& tar -xzf /tmp/glide.tar.gz -C /tmp \  
&& mkdir -p $GOPATH/src/github.com/Masterminds \  
&& mv /tmp/glide-* $GOPATH/src/github.com/Masterminds/glide \  
&& cd $GOPATH/src/github.com/Masterminds/glide \  
\  
# Build and install Glide executable  
&& make install \  
\  
# Install Glide license  
&& mkdir -p /usr/local/share/doc/glide \  
&& cp LICENSE /usr/local/share/doc/glide/ \  
\  
# Cleanup unnecessary files  
&& apk del .build-deps \  
&& rm -rf /var/cache/apk/* \  
$GOPATH/src/* \  
/tmp/*  
  
  
ENTRYPOINT ["/usr/local/bin/glide"]  


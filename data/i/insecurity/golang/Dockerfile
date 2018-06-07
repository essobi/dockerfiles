FROM insecurity/debian:jessie  
MAINTAINER Vecten Sebastien <jtof_fap@insecurity.fr>  
  
# Set variables  
ENV GOLANG_VERSION 1.7  
ENV GOOS linux  
ENV GOARCH amd64  
ENV GOLANG_DOWNLOAD_URL
https://golang.org/dl/go$GOLANG_VERSION.$GOOS-$GOARCH.tar.gz  
ENV GOLANG_DOWNLOAD_SHA256_URL
https://storage.googleapis.com/golang/go$GOLANG_VERSION.$GOOS-$GOARCH.tar.gz.sha256  
ENV GO_WRAPPER_DOWNLOAD_URL https://raw.githubusercontent.com/docker-
library/golang/9f666dc2f4f51df564613f787d28b3a2353243e0/1.7/wheezy/go-wrapper  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
  
# Install build dependencies (gcc for cgo)  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
g++ \  
gcc \  
libc6-dev \  
make \  
curl \  
  
# Get and install Golang binaries \  
&& curl -fsSL "$GOLANG_DOWNLOAD_URL" -o golang.tar.gz \  
&& curl -fsSL "$GOLANG_DOWNLOAD_SHA256_URL" -o golang.tar.gz.sha256 \  
&& SUM=$(cat golang.tar.gz.sha256) && echo "$SUM golang.tar.gz" | sha256sum -c
- \  
&& tar -C /usr/local -xzf golang.tar.gz \  
&& rm golang.tar.gz && rm golang.tar.gz.sha256 \  
  
# APT Clean-up \  
&& apt-get autoclean \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
  
# Create dir and copy go-wrapper \  
&& mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH" \  
&& curl -fsSL "$GO_WRAPPER_DOWNLOAD_URL" -o /usr/local/bin/go-wrapper  
  
# Let's go !  
WORKDIR $GOPATH  
  


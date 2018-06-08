# My googledrive box  
FROM v4tech/base:latest  
MAINTAINER Stewart V. Wright <stewart@vifortech.com>  
  
## This code "borrowed" from https://github.com/adam-
may/dev_machines/blob/master/go/Dockerfile  
# Which version?  
ENV go_version=go1.6.3  
ENV GOPATH /gocode  
ENV PATH
$GOPATH/bin:/usr/local/go/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
  
# go tarball and GOPTH and gcc  
RUN wget -qO- https://golang.org/dl/$go_version.linux-amd64.tar.gz | \  
tar -C /usr/local -xzf - && \  
mkdir -p $GOPATH/bin && \  
mkdir -p $GOPATH/pkg && \  
mkdir -p $GOPATH/src && \  
apt-get update && \  
apt-get install -y gcc && \  
rm -rf /var/lib/opt/lists/*  
  
WORKDIR $GOPATH/src  
  
# Install drive  
RUN go get github.com/odeke-em/drive/drive-gen && drive-gen  
  


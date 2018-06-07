FROM node:0.10-slim  
  
RUN apt-get update -y \  
&& apt-get install --no-install-recommends -y -q \  
curl git ca-certificates mercurial zip \  
&& rm -rf /var/lib/apt/lists/*  
  
  
#################################################################  
# Golang  
################################################################  
ENV GOLANG_VERSION 1.4.2  
RUN curl -sSL https://storage.googleapis.com/golang/go$GOLANG_VERSION.linux-
amd64.tar.gz \  
| tar -C /usr/local -xz  
ENV PATH $PATH:/usr/local/go/bin  
RUN mkdir -p /go/src /go/bin && chmod -R 777 /go  
ENV GOPATH /go  
ENV PATH /go/bin:$PATH  
  
WORKDIR $GOPATH  


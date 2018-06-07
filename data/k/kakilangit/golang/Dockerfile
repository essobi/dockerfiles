FROM debian:jessie  
MAINTAINER kakilangit <theguywhodrinkscoffeeandcodes@gmail.com>  
  
# gcc for cgo  
RUN apt-get update && apt-get install -y --no-install-recommends ca-
certificates \  
wget \  
g++ \  
gcc \  
libc6-dev \  
make \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV GOLANG_VERSION 1.8.3  
ENV GOLANG_DOWNLOAD_URL
https://storage.googleapis.com/golang/go$GOLANG_VERSION.linux-amd64.tar.gz  
  
RUN wget -c "$GOLANG_DOWNLOAD_URL" -O golang.tar.gz \  
&& tar -C /usr/local -xzf golang.tar.gz \  
&& rm golang.tar.gz  
  
ENV GOPATH /gopath  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
  
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"  
  
RUN go version  


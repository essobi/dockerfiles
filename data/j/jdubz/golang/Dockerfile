FROM debian:jessie  
MAINTAINER Josh Williams <t3hpr1m3@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV GO_VERSION 1.5.1  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
git-core \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -sSL \  
"https://storage.googleapis.com/golang/go${GO_VERSION}.linux-amd64.tar.gz" \  
-o /tmp/go${GO_VERSION}.linux-amd64.tar.gz \  
&& tar -C /usr/local -xzf /tmp/go${GO_VERSION}.linux-amd64.tar.gz \  
&& rm /tmp/go${GO_VERSION}.linux-amd64.tar.gz \  
&& apt-get purge -y --auto-remove  
  
COPY go-wrapper /usr/local/bin/go-wrapper  
  
ENTRYPOINT ["/usr/local/bin/go-wrapper"]  


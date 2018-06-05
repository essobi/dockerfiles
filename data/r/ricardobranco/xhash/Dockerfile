FROM debian:9  
  
# Need for speed  
VOLUME /tmp  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install --no-install-recommends -y ca-certificates \  
gcc \  
git \  
libc6-dev \  
libssl-dev \  
wget \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& wget -qO- https://storage.googleapis.com/golang/go1.9.4.linux-amd64.tar.gz
| tar zxf - -C /tmp/ \  
&& PATH=$PATH:/tmp/go/bin GOROOT=/tmp/go GOPATH=/tmp/ go get
github.com/ricardobranco777/xhash \  
&& cd /tmp/src/github.com/ricardobranco777/xhash/ \  
&& PATH=$PATH:/tmp/go/bin GOROOT=/tmp/go GOPATH=/tmp/ go build \  
&& mv xhash /usr/local/bin/ \  
&& apt-get remove -y gcc git libc6-dev wget \  
&& apt-get autoremove -y  
  
ENTRYPOINT ["/usr/local/bin/xhash"]  


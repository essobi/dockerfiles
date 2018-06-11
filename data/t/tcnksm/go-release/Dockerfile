FROM debian:wheezy  
  
RUN apt-get update -y && apt-get install --no-install-recommends -y -q \  
curl \  
zip \  
build-essential \  
ca-certificates \  
git mercurial bzr \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV GOVERSION 1.5beta2  
RUN mkdir /goroot && mkdir /gopath  
RUN curl https://storage.googleapis.com/golang/go${GOVERSION}.linux-
amd64.tar.gz \  
| tar xvzf - -C /goroot --strip-components=1  
  
ENV GOPATH /gopath  
ENV GOROOT /goroot  
ENV PATH $GOROOT/bin:$GOPATH/bin:$PATH  
  
RUN go get -v github.com/mitchellh/gox  
RUN go get -v github.com/tcnksm/ghr  
  
ADD usr/local/bin/go-release.sh /usr/local/bin/go-release.sh  
  
ENTRYPOINT ["/usr/local/bin/go-release.sh"]  


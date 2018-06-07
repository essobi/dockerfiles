FROM jetbrains/teamcity-minimal-agent  
MAINTAINER Jakob Borg <jakob@nym.se>  
  
ENV GO_VERSION 1.10.2  
ENV MIN_GO_VERSION 1.8.7  
  
# Install required packages  
  
RUN apt-get update && apt-get install -y \--no-install-recommends \  
build-essential zip git mercurial graphviz \  
ca-certificates curl fakeroot rubygems ruby-dev rpm \  
snapcraft docker.io ansible openssh-client \  
libffi-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN gem install --no-ri \--no-rdoc fpm  
  
# Install Go  
  
RUN curl -sSL https://golang.org/dl/go${MIN_GO_VERSION}.linux-amd64.tar.gz \  
| tar -C /usr/local -xz && mv /usr/local/go /usr/local/oldgo  
  
RUN curl -sSL https://golang.org/dl/go${GO_VERSION}.linux-amd64.tar.gz \  
| tar -C /usr/local -xz  
  
# Use Go  
  
ENV PATH /usr/local/go/bin:$PATH  
ENV GOPATH /usr/local  
  
# Fetch required utilities, from build.go setup()  
  
RUN go get github.com/alecthomas/gometalinter \  
&& go get github.com/AlekSi/gocov-xml \  
&& go get github.com/axw/gocov/gocov \  
&& go get github.com/FiloSottile/gvt \  
&& go get github.com/golang/lint/golint \  
&& go get github.com/gordonklaus/ineffassign \  
&& go get github.com/mdempsky/unconvert \  
&& go get github.com/mitchellh/go-wordwrap \  
&& go get github.com/opennota/check/cmd/... \  
&& go get github.com/tsenart/deadcode \  
&& go get golang.org/x/net/html \  
&& go get golang.org/x/tools/cmd/cover \  
&& go get honnef.co/go/tools/...  
  
# Extra  
  
RUN go get golang.org/x/tools/cmd/cover \  
&& go get golang.org/x/net/html \  
&& go get github.com/AlekSi/gocov-xml \  
&& go get github.com/tebeka/go2xunit  
  
# GB, for some build setups  
  
RUN go get github.com/constabulary/gb/...  
  
# Hugo, for website builds  
  
RUN curl -sSL
https://github.com/gohugoio/hugo/releases/download/v0.33/hugo_0.33_Linux-64bit.tar.gz
\  
| tar -C /usr/local/bin -xz  
  
# Teamcity build translator  
  
RUN go get github.com/2tvenom/go-test-teamcity  
  
# Install Node JS & Elm  
  
ENV PATH /usr/local/node/bin:$PATH  
  
RUN curl -sSL https://nodejs.org/dist/v6.11.3/node-v6.11.3-linux-x64.tar.xz \  
| tar -C /usr/local -Jx \  
&& ln -s /usr/local/node-v6.11.3-linux-x64 /usr/local/node \  
&& npm install -g elm  


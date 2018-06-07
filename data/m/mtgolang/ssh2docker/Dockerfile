FROM debian:jessie  
MAINTAINER aerth@isupon.us  
  
## Install Go 1.6 (using Go 1.4.3)  
ENV GOLANG_VERSION 1.6  
ENV GOLANG_SRC_URL https://golang.org/dl/go$GOLANG_VERSION.src.tar.gz  
ENV GOLANG_SRC_SHA256
a96cce8ce43a9bf9b2a4c7d470bc7ee0cb00410da815980681c8353218dcf146  
ENV GOLANG_BOOTSTRAP_VERSION 1.4.3  
ENV GOLANG_BOOTSTRAP_URL
https://golang.org/dl/go$GOLANG_BOOTSTRAP_VERSION.src.tar.gz  
ENV GOLANG_BOOTSTRAP_SHA1 486db10dc571a55c8d795365070f66d343458c48  
  
## Install git, curl openssl  
RUN set -ex \  
&& apt-get update && apt-get install -y git curl openssl  
  
## Install wget, gcc, make, build-essential  
RUN apt-get install -y wget gcc make build-essential  
  
## Build Go  
RUN mkdir -p /usr/local/bootstrap \  
&& wget -q "$GOLANG_BOOTSTRAP_URL" -O golang.tar.gz \  
&& echo "$GOLANG_BOOTSTRAP_SHA1 golang.tar.gz" | sha1sum -c - \  
&& tar -C /usr/local/bootstrap -xzf golang.tar.gz \  
&& rm golang.tar.gz \  
&& cd /usr/local/bootstrap/go/src \  
&& ./make.bash \  
&& export GOROOT_BOOTSTRAP=/usr/local/bootstrap/go \  
\  
&& wget -q "$GOLANG_SRC_URL" -O golang.tar.gz \  
&& echo "$GOLANG_SRC_SHA256 golang.tar.gz" | sha256sum -c - \  
&& tar -C /usr/local -xzf golang.tar.gz \  
&& rm golang.tar.gz \  
&& cd /usr/local/go/src \  
&& ./make.bash \  
\  
&& rm -rf /usr/local/bootstrap /usr/local/go/pkg/bootstrap  
  
## Set GOPATH and GOBIN  
ENV PATH $PATH:/home/gopher/go/bin:/usr/local/go/bin:/opt/bin  
ENV GOPATH /tmp/mtgolang  
ENV GOBIN /opt/bin/  
  
## Build ssh2docker library  
RUN go get -v -u github.com/mtgolang/ssh2docker  
  
## Build ssh2docker command  
RUN go get -v -u github.com/mtgolang/ssh2docker/cmd/ssh2docker  
  
## Install Docker  
RUN curl -fsSL https://get.docker.com/ | sh  
  
## Start Docker  
#RUN service docker start  
## Serve 2222  
EXPOSE 2222  
## Copy optionals  
ADD ./opt /opt/  
  
## Run with banner  
ENTRYPOINT ["/opt/bin/ssh2docker", "--banner", "Welcome to Mt Golang. You can
run `help` command for information."]  


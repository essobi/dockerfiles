FROM alpine:3.5  
  
RUN apk add --no-cache ca-certificates  
  
ENV GOLANG_VERSION 1.7.5  
ENV GOLANG_SRC_URL https://golang.org/dl/go$GOLANG_VERSION.src.tar.gz  
ENV GOLANG_SRC_SHA256
4e834513a2079f8cbbd357502cccaac9507fd00a1efe672375798858ff291815  
  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
  
WORKDIR $GOPATH  
  
# https://golang.org/issue/14851  
COPY no-pic.patch /  
# https://golang.org/issue/17847  
COPY 17847.patch /  
  
RUN set -ex \  
&& apk add --no-cache --virtual .build-deps \  
bash \  
gcc \  
musl-dev \  
openssl \  
go \  
build-base \  
git \  
\  
&& export GOROOT_BOOTSTRAP="$(go env GOROOT)" \  
\  
&& wget -q "$GOLANG_SRC_URL" -O golang.tar.gz \  
&& echo "$GOLANG_SRC_SHA256 golang.tar.gz" | sha256sum -c - \  
&& tar -C /usr/local -xzf golang.tar.gz \  
&& rm golang.tar.gz \  
&& cd /usr/local/go/src \  
&& patch -p2 -i /no-pic.patch \  
&& patch -p2 -i /17847.patch \  
&& ./make.bash \  
\  
&& go get bitbucket.org/liamstask/goose/cmd/goose \  
&& cp -pr /go/bin/goose /usr/bin \  
\  
&& rm -rf *.patch \  
&& apk del .build-deps \  
&& rm -rf $GOPATH \  
&& mkdir $GOPATH \  
&& rm -rf /usr/local/go \  
&& rm -rf /var/cache/apk/*  
  
WORKDIR $GOPATH  


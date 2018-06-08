FROM alpine:3.5  
  
RUN apk add --no-cache ca-certificates  
  
ENV GOLANG_VERSION 1.8  
ENV GOLANG_SRC_URL https://golang.org/dl/go$GOLANG_VERSION.src.tar.gz  
ENV GOLANG_SRC_SHA256
406865f587b44be7092f206d73fc1de252600b79b3cacc587b74b5ef5c623596  
  
# https://golang.org/issue/14851  
COPY no-pic.patch /  
  
RUN set -ex \  
&& apk add --no-cache --virtual .build-deps \  
bash \  
gcc \  
musl-dev \  
openssl \  
go \  
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
&& ./make.bash \  
\  
&& rm -rf /*.patch \  
&& export GOPATH=/go \  
&& export PATH=$GOPATH/bin:/usr/local/go/bin:$PATH \  
&& mkdir -p $GOPATH/src/github.com/yaproxy/ && cd
$GOPATH/src/github.com/yaproxy/ \  
&& git clone https://github.com/yaproxy/yap.git && cd yap \  
&& export CGO_ENABLED=0 && go get ./... \  
&& go build -o /usr/local/bin/yap cli/main.go \  
&& cp yap.toml / \  
&& cd / && rm -rf /go /usr/local/go \  
&& apk del .build-deps  
  
EXPOSE 443 8088  
CMD ["/usr/local/bin/yap", "/yap.toml"]  


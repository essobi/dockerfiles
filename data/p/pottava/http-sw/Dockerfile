FROM alpine:3.6  
  
RUN apk --no-cache add \--virtual build-dependencies bash gcc musl-dev openssl
go git \  
  
# Install go 1.9  
&& GOLANG_VERSION=1.9 \  
&& GOLANG_SRC_URL=https://golang.org/dl/go$GOLANG_VERSION.src.tar.gz \  
&&
GOLANG_SRC_SHA256=a4ab229028ed167ba1986825751463605264e44868362ca8e7accc8be057e993
\  
&& export GOROOT_BOOTSTRAP="$(go env GOROOT)" \  
&& wget -q "$GOLANG_SRC_URL" -O golang.tar.gz \  
&& echo "$GOLANG_SRC_SHA256 golang.tar.gz" | sha256sum -c \- \  
&& tar -C /usr/local -xzf golang.tar.gz \  
&& wget -q https://raw.githubusercontent.com/docker-
library/golang/master/1.9/alpine3.6/no-pic.patch \  
&& cd /usr/local/go/src \  
&& patch -p2 -i /no-pic.patch \  
&& ./make.bash \  
&& export GOPATH=/go \  
&& mkdir -p /go/src /go/bin \  
&& chmod -R 777 /go \  
  
# Compile the app  
&& go get github.com/pottava/http-something-wrong \  
&& mv /go/bin/http-something-wrong /app \  
  
# Clean up  
&& apk del --purge -r build-dependencies \  
&& rm -rf /usr/local/go /usr/lib/go /go /golang.tar.gz /*.patch  
  
EXPOSE 80  
  
CMD ["/app"]  


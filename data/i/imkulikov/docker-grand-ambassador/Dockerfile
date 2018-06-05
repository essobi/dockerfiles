FROM alpine:3.4  
ENV GOLANG_VERSION 1.7.3  
ENV GOLANG_SRC_URL https://golang.org/dl/go$GOLANG_VERSION.src.tar.gz  
ENV GOLANG_SRC_SHA256
79430a0027a09b0b3ad57e214c4c1acfdd7af290961dd08d322818895af1ef44  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
  
ADD ./grand-ambassador /go/src/github.com/cpuguy83/docker-grand-ambassador  
COPY ./golang/no-pic.patch /  
COPY ./golang/go-wrapper /usr/local/bin/  
  
WORKDIR $GOPATH  
  
RUN apk --update add --no-cache \  
ca-certificates \  
git \  
# === Golang Build: ===  
&& \  
set -ex \  
&& apk add \--no-cache --virtual .build-deps \  
bash \  
gcc \  
musl-dev \  
openssl \  
go \  
&& export GOROOT_BOOTSTRAP="$(go env GOROOT)" \  
&& wget -q "$GOLANG_SRC_URL" -O golang.tar.gz \  
&& echo "$GOLANG_SRC_SHA256 golang.tar.gz" | sha256sum -c - \  
&& tar -C /usr/local -xzf golang.tar.gz \  
&& rm golang.tar.gz \  
&& cd /usr/local/go/src \  
&& patch -p2 -i /no-pic.patch \  
&& ./make.bash \  
&& rm -rf /*.patch \  
&& apk del .build-deps \  
&& mkdir -p "$GOPATH/src" "$GOPATH/bin" \  
&& chmod -R 777 "$GOPATH" \  
# =========================  
# === Build ambassador: ===  
&& cd /go/src/github.com/cpuguy83/docker-grand-ambassador \  
&& go get \  
&& go build \  
&& cp docker-grand-ambassador /usr/bin/grand-ambassador \  
&& apk del git \  
&& rm -rf /usr/local/go \  
&& rm -rf /var/cache/apk/*  
# =========================  
ENTRYPOINT ["/usr/bin/grand-ambassador"]  


FROM golang:1.9.2-alpine3.6 as builder  
  
ARG VIPS_VERSION=8.5.9  
ARG IMAGINARY_VERSION=1.0.10  
ENV VIPS_DIR=/vips  
ENV PKG_CONFIG_PATH=${VIPS_DIR}/lib/pkgconfig:$PKG_CONFIG_PATH  
  
RUN apk update && apk add --no-cache openssl ca-certificates && mkdir -p
${GOPATH}/src && \  
wget -O-
https://github.com/jcupitt/libvips/releases/download/v${VIPS_VERSION}/vips-${VIPS_VERSION}.tar.gz
| tar xzC /tmp && \  
wget -O-
https://github.com/h2non/imaginary/archive/v${IMAGINARY_VERSION}.tar.gz | tar
xzC ${GOPATH}/src && \  
echo "@testing http://dl-3.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
apk update && apk upgrade && apk add --no-cache \  
build-base git vips-dev@testing gobject-introspection-dev  
  
RUN cd /tmp/vips-${VIPS_VERSION} && \  
./configure \  
\--disable-static \  
\--disable-dependency-tracking \  
\--without-python \  
\--prefix=${VIPS_DIR} && \  
make && \  
make install && \  
cd ${GOPATH}/src/imaginary-${IMAGINARY_VERSION} && \  
go get -u github.com/golang/dep/cmd/dep && \  
dep ensure && \  
go build -o $GOPATH/bin/imaginary  
  
FROM alpine:3.6  
RUN apk update \  
apk upgrade && \  
echo "@testing http://dl-3.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
apk add --no-cache \  
openssl ca-certificates gobject-introspection vips@testing && \  
rm -rf /var/cache/apk/*  
  
COPY \--from=builder /vips/lib/ /usr/local/lib  
COPY \--from=builder /go/bin/imaginary /usr/bin/imaginary  
  
ENV PORT 9000  
EXPOSE 9000  
ENTRYPOINT ["/usr/bin/imaginary"]  


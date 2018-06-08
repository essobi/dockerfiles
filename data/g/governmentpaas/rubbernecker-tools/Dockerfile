FROM alpine:3.7  
  
RUN apk add \--update --no-cache \  
bash \  
gcc \  
musl-dev \  
openssl \  
git \  
make \  
go=1.9.4-r0 \  
nodejs=8.9.3-r1  
  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
RUN mkdir -p "$GOPATH/bin" "$GOPATH/src" && chmod -R 777 "$GOPATH"  
RUN go get -u github.com/golang/dep/cmd/dep  
  
WORKDIR "$GOPATH/src"  


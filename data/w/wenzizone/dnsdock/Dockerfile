FROM alpine  
  
ENV GOLANG_VERSION 1.6.2-r4  
ENV GOPATH /go  
ENV CGO_ENABLED 0  
ENV PATH ${PATH}:/go/bin  
ENV CGO_ENABLED=0  
RUN apk update \  
&& apk upgrade \  
&& apk add go>${GOLANG_VERSION} go-tools>${GOLANG_VERSION} git  
  
ADD . /go/src/github.com/tonistiigi/dnsdock  
WORKDIR /go/src/github.com/tonistiigi/dnsdock  
  
RUN go get -v github.com/tools/godep \  
&& godep restore  
WORKDIR /go/src/github.com/tonistiigi/dnsdock/src  
RUN go build -o /tmp/output/dnsdock -ldflags "-X main.version=$(if
version=$(git describe --contains HEAD 2>/dev/null); then echo $version; else
echo "dev"; fi)" \  
&& cp /tmp/output/dnsdock /go/bin/dnsdock  
  
ENTRYPOINT ["/go/bin/dnsdock"]  


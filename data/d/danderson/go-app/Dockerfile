FROM alpine:edge  
MAINTAINER David Anderson <dave@natulte.net>  
  
ONBUILD COPY . /tmp/go/src/program  
ONBUILD RUN \  
export GOPATH=/tmp/go &&\  
echo "http://dl-4.alpinelinux.org/alpine/edge/community"
>>/etc/apk/repositories &&\  
apk -U add ca-certificates git go &&\  
apk upgrade &&\  
cd /tmp/go/src/program &&\  
go get . &&\  
go build . &&\  
cp program /program &&\  
cd / &&\  
rm -rf /tmp/go &&\  
apk del ca-certificates git go &&\  
rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["/program"]  


FROM alpine:edge  
  
ENV GOPATH=/go GOBIN=/usr/bin  
  
RUN \  
echo "http://dl-4.alpinelinux.org/alpine/edge/community"
>>/etc/apk/repositories &&\  
apk -U add go git gcc libc-dev libltdl libtool libgcc &&\  
apk upgrade &&\  
mkdir -p /go/src &&\  
go get -d github.com/cloudflare/cfssl/... &&\  
go install github.com/cloudflare/cfssl/cmd/cfssl &&\  
go install github.com/cloudflare/cfssl/cmd/cfssljson &&\  
go install github.com/cloudflare/cfssl/cmd/mkbundle &&\  
go install github.com/cloudflare/cfssl/cmd/multirootca &&\  
apk del go git gcc libc-dev libtool libgcc &&\  
rm -rf /var/cache/apk/*  


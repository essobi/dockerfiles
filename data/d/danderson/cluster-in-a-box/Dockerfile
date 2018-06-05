FROM alpine:edge  
  
ENV GOPATH=/go GOBIN=/usr/bin  
  
RUN \  
echo "@testing http://dl-4.alpinelinux.org/alpine/edge/testing"
>>/etc/apk/repositories &&\  
echo "http://dl-4.alpinelinux.org/alpine/edge/community"
>>/etc/apk/repositories &&\  
apk -U add go git gcc libc-dev libltdl libtool libgcc openssl vault@testing
wget &&\  
mkdir -p /go/src &&\  
go get -d github.com/cloudflare/cfssl/... &&\  
go install github.com/cloudflare/cfssl/cmd/cfssl &&\  
go install github.com/cloudflare/cfssl/cmd/cfssljson &&\  
go install github.com/cloudflare/cfssl/cmd/mkbundle &&\  
go install github.com/cloudflare/cfssl/cmd/multirootca &&\  
wget -O /etcd.tgz
https://github.com/coreos/etcd/releases/download/v2.2.0/etcd-v2.2.0-linux-
amd64.tar.gz &&\  
mkdir /etcd &&\  
(cd /etcd && tar zxvf /etcd.tgz) &&\  
cp /etcd/*/etcd /usr/bin &&\  
cp /etcd/*/etcdctl /usr/bin &&\  
apk del go git gcc libc-dev libtool libgcc openssl wget &&\  
rm -rf /var/cache/apk/* /etcd.tgz /etcd  


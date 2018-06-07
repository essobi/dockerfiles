FROM centos:7.4.1708 as builder  
  
# Replcae OAUTH2_PROXY_VERSION=master with OAUTH2_PROXY_VERSION=tags/v2.3 as
soon as release v2.3 will become available.  
# Using master to have Go dep dependency manager available.  
ENV \  
GOPATH=/root \  
OAUTH2_PROXY_VERSION=master \  
PATH="${PATH}:/usr/local/go/bin:/root/bin"  
RUN \  
yum install -y git wget tar 'ca-certificates*' && \  
wget https://storage.googleapis.com/golang/go1.9.linux-amd64.tar.gz && \  
tar xzf go1.9.linux-amd64.tar.gz -C /usr/local && \  
rm go1.9.linux-amd64.tar.gz && \  
go get -u github.com/golang/dep/cmd/dep  
  
# Workaround for: https://github.com/bitly/oauth2_proxy/issues/573  
#RUN go get -d github.com/bitly/oauth2_proxy  
# RUN cd /root/src/github.com/bitly/oauth2_proxy && \  
# git checkout ${OAUTH2_PROXY_VERSION}  
RUN \  
yum install -y unzip && \  
mkdir -p /root/src/github.com/bitly/ && \  
cd /root/src/github.com/bitly/ && \  
curl -Lo -
https://github.com/bitly/oauth2_proxy/archive/${OAUTH2_PROXY_VERSION}.zip>${OAUTH2_PROXY_VERSION}.zip
&& \  
unzip ${OAUTH2_PROXY_VERSION}.zip && \  
mv oauth2_proxy-${OAUTH2_PROXY_VERSION} oauth2_proxy  
WORKDIR /root/src/github.com/bitly/oauth2_proxy  
RUN \  
sed -E 's/gopkg.in\/fsnotify.v1/gopkg.in\/fsnotify\/fsnotify.v1/' -i
Gopkg.toml && \  
sed -E 's/gopkg.in\/fsnotify.v1/gopkg.in\/fsnotify\/fsnotify.v1/' -i
Gopkg.lock && \  
sed -E 's/gopkg.in\/fsnotify.v1/gopkg.in\/fsnotify\/fsnotify.v1/' -i
watcher.go  
# Enf of workaround  
RUN \  
dep ensure && \  
sed -E 's/127.0.0.1:4180/0.0.0.0:4180/' -i main.go && \  
CGO_ENABLED=0 GOOS=linux go build -ldflags '-s -w -extldflags "-static"' -o
/target/oauth2_proxy .  
  
FROM scratch  
COPY \--from=builder /target/oauth2_proxy /  
COPY \--from=builder /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem
/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem  
EXPOSE 4180  
WORKDIR /  
ENTRYPOINT [ "/oauth2_proxy" ]  


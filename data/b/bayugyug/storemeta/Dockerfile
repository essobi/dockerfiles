#FROM golang  
FROM buildpack-deps:wheezy-scm  
  
#auth  
MAINTAINER bayugyug<bayugyug@gmail.com>  
  
ENV GOLANG_VERSION 1.7.1  
ENV GOLANG_DOWNLOAD_URL https://golang.org/dl/go$GOLANG_VERSION.linux-
amd64.tar.gz  
ENV GOLANG_DOWNLOAD_SHA256
43ad621c9b014cde8db17393dc108378d37bc853aa351a6c74bf6432c1bbd182  
ENV GOPATH=/go  
ENV GOSRC=$GOPATH/src  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
  
# gcc for cgo  
RUN apt-get update && \  
apt-get install -y --no-install-recommends make git && \  
rm -rf /var/lib/apt/lists/* && \  
curl -fsSL "$GOLANG_DOWNLOAD_URL" -o golang.tar.gz && \  
echo "$GOLANG_DOWNLOAD_SHA256 golang.tar.gz" | sha256sum -c - && \  
tar -C /usr/local -xzf golang.tar.gz && \  
rm golang.tar.gz && \  
mkdir -p "$GOPATH/src" "$GOPATH/bin" "$GOSRC/github.com/bayugyug" && chmod -R
777 "$GOPATH" && \  
cd $GOSRC/github.com/bayugyug && \  
git clone https://github.com/bayugyug/storemeta.git && \  
cd $GOSRC/github.com/bayugyug/storemeta && \  
go get -v && \  
go build -tags netgo -installsuffix netgo -installsuffix cgo -v -ldflags "-s
-w -X main.pBuildTime=`date +%Y%m%d.%H%M%S`" . && \  
cd $GOSRC && \  
go install github.com/bayugyug/storemeta && \  
cd $GOSRC/github.com/bayugyug/storemeta && \  
cp -f Docker/cleanup.sh $GOPATH/bin/ && \  
cp -f Docker/wheezy/go-wrapper /usr/local/bin/ && \  
chmod +x $GOPATH/bin/* && \  
$GOPATH/bin/cleanup.sh  
  
#main entry  
ENTRYPOINT [ "storemeta" ]  


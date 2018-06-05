#start  
#FROM golang  
FROM golang:alpine  
  
#auth  
MAINTAINER bayugyug<bayugyug@gmail.com>  
  
#envt  
ENV GOPATH /go  
ENV GOSRC $GOPATH/src  
ENV GOBIN $GOPATH/bin  
ENV PATH $PATH:$GOPATH/bin:/usr/local/go/bin  
  
#prepare  
RUN apk add \--no-cache ca-certificates && \  
set -ex \  
&& apk add \--no-cache --virtual .build-deps \  
bash \  
git \  
gcc \  
musl-dev \  
openssl \  
go && \  
apk add \--update ca-certificates # Certificates for SSL  
  
#prepare  
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && \  
chmod -R 777 "$GOPATH" && \  
mkdir -p $GOSRC/github.com/bayugyug && \  
cd $GOSRC/github.com/bayugyug && \  
git clone https://github.com/bayugyug/mongers-uagents.git && \  
cd $GOSRC/github.com/bayugyug/mongers-uagents && \  
go get -v && CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -v
-ldflags "-s -w -X main.pBuildTime=`date +%Y%m%d.%H%M%S`" . && \  
cp -f mongers-uagents $GOBIN/ && \  
chmod +x $GOBIN/* && \  
apk del .build-deps go git gcc musl-dev && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/ && \  
rm -rf /var/{cache,log} && \  
rm -fr /go/pkg /go/src && \  
ls -ltrha $GOBIN/* && \  
du -sh /go/* /*  
  
#main entry  
ENTRYPOINT [ "/go/bin/mongers-uagents" ]  


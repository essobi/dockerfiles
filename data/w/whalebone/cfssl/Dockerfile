FROM gliderlabs/alpine:3.4  
MAINTAINER Petr Vitek "rattus.PV@gmail.com"  
  
# Try hard to get a minimal image to reduce footprint  
RUN apk --no-cache add go git gcc libc-dev libltdl libtool libgcc && \  
export GOPATH=/go && \  
go get -u github.com/cloudflare/cfssl/cmd/... && \  
go get -u bitbucket.org/liamstask/goose/cmd/goose && \  
apk del go git gcc libc-dev libtool libgcc && \  
mv /go/bin/* /bin/ && \  
rm -rf /go/src/golang.org && \  
rm -rf /go/src/github.com/GeertJohan && \  
rm -rf /go/src/github.com/daaku && \  
rm -rf /go/src/github.com/dgryski && \  
rm -rf /go/src/github.com/kardianos && \  
rm -rf /go/src/github.com/miekg  
  
WORKDIR /etc/cfssl  
EXPOSE 8888  
  
COPY cfssl-wrap.sh /opt/cfssl-wrap.sh  
COPY cfssl-config.json /etc/cfssl/cfssl-config.json  
COPY sqlitedb.json /etc/cfssl/cfssl-db-config.json  
  
ENTRYPOINT ["/bin/sh", "/opt/cfssl-wrap.sh" ]  


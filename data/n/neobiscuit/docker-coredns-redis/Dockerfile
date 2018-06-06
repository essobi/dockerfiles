FROM golang:alpine  
MAINTAINER Amrit Panesar <me@amrit.be> @Neo-Desktop  
  
RUN apk --no-cache add bash bind-tools ca-certificates openssl git && \  
update-ca-certificates && \  
rm -rf /var/cache/apk/*  
  
RUN go get -d -v github.com/coredns/coredns && \  
go get -d -v github.com/mholt/caddy/onevent && \  
go get -d -v github.com/Neo-Desktop/redis  
  
RUN cd /go/src/github.com/coredns/coredns && \  
echo "redis:github.com/Neo-Desktop/redis" | tee -a plugin.cfg && \  
go generate && \  
go install -v ./ && \  
rm -rf /go/src/*  
  
COPY ./init.sh /init.sh  
  
ENTRYPOINT /init.sh  
  
VOLUME [ "/data" ]  
  
CMD coredns -conf /data/Corefile  


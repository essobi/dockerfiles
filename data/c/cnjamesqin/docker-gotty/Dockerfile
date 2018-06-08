FROM docker:dind  
  
EXPOSE 8080  
ENV REGISTRY_MIRROR https://registry.docker-cn.com  
ENV INSECURE_REGISTRIE docker-registry.oa.com  
ENV DIND_MODE yes  
  
ADD ./etc/daemon.json /etc/docker/daemon.json  
ADD ./gotty-entrypoint.sh /usr/local/bin/gotty-entrypoint.sh  
  
RUN apk add --update go git musl-dev && \  
GOPATH=/go go get github.com/yudai/gotty && \  
cd /go/src/github.com/yudai/gotty && \  
GOPATH=/go CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o
/usr/local/bin/gotty && \  
apk del go git musl-dev && \  
cd / && \  
rm -rf /go /var/cache/apk/*  
  
ENTRYPOINT ["/usr/local/bin/gotty-entrypoint.sh"]  


FROM haproxy:1.7-alpine  
  
ENV GOPATH /go  
ENV PATH $PATH:/go/bin  
  
COPY ./ /go/src/github.com/appcelerator/docker-haproxy  
RUN echo "@edge http://nl.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories && \  
echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
echo "@community http://nl.alpinelinux.org/alpine/v3.5/community" >>
/etc/apk/repositories  
RUN apk update && apk upgrade && \  
apk -v --virtual build-deps add git make bash go musl-dev && \  
apk -v add curl && \  
go version && \  
cd $GOPATH/src/github.com/appcelerator/docker-haproxy && \  
go get -u github.com/Masterminds/glide/... && \  
glide install && \  
rm -rf vendor/github.com/appcelerator/amp/vendor && \  
rm -rf vendor/github.com/docker/docker/vendor/golang.org/x/net/trace && \  
make install && \  
echo amp-haproxy built && \  
rm /go/bin/glide && \  
apk del build-deps && \  
cd / && rm -rf /go/src /go/pkg /var/cache/apk/* /root/.cache /root/.glide && \  
chmod +x $GOPATH/bin/*  
  
COPY haproxy.cfg.tpt /usr/local/etc/haproxy/haproxy.cfg.tpt  
  
HEALTHCHECK \--interval=5s --timeout=10s --retries=12 CMD curl
http://127.0.0.1/healthcheck  
  
CMD ["/go/bin/docker-haproxy"]  


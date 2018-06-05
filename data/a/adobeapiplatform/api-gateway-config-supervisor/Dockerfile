# api-gateway-config-supervisor  
#  
# VERSION 1.9.3.1  
#  
# From https://hub.docker.com/_/alpine/  
#  
FROM alpine:latest  
  
ENV GOPATH /usr/lib/go/bin  
ENV GOBIN /usr/lib/go/bin  
ENV PATH $PATH:/usr/lib/go/bin  
  
  
RUN mkdir -p /tmp/go  
ADD . /tmp/go  
RUN echo "http://dl-4.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories \  
&& apk update \  
&& apk add make git go \  
  
&& echo " building local project ... " \  
&& cd /tmp/go \  
&& make setup \  
&& mkdir -p /tmp/go/Godeps/_workspace \  
&& ln -s /tmp/go/vendor /tmp/go/Godeps/_workspace/src \  
&& mkdir -p /tmp/go-src/src/github.com/adobe-apiplatform \  
&& ln -s /tmp/go /tmp/go-src/src/github.com/adobe-apiplatform/api-gateway-
config-supervisor \  
&& GOPATH=/tmp/go/vendor:/tmp/go-src CGO_ENABLED=0 GOOS=linux
/usr/lib/go/bin/godep go test \  
&& GOPATH=/tmp/go/vendor:/tmp/go-src CGO_ENABLED=0 GOOS=linux
/usr/lib/go/bin/godep go build -ldflags "-s" -a -installsuffix cgo -o api-
gateway-config-supervisor ./ \  
&& cp /tmp/go/api-gateway-config-supervisor /usr/lib/go/bin \  
  
&& echo "installing rclone sync ... " \  
&& go get github.com/ncw/rclone \  
  
&& echo " cleaning up ... " \  
&& rm -rf /usr/lib/go/bin/src \  
&& rm -rf /tmp/go \  
&& rm -rf /tmp/api-gateway-config-supervisor* \  
&& rm -rf /tmp/go-src \  
&& rm -rf /usr/lib/go/bin/pkg/ \  
&& rm -rf /usr/lib/go/bin/godep \  
&& apk del make git go \  
&& rm -rf /var/cache/apk/*  
  
RUN echo " installing aws-cli ..." \  
&& apk update \  
&& apk add python \  
&& apk add py-pip \  
&& pip install --upgrade pip \  
&& pip install awscli  
  
ENTRYPOINT ["api-gateway-config-supervisor"]


FROM golang:alpine  
  
# Install dependencies  
RUN apk --no-cache --update --repository
http://dl-3.alpinelinux.org/alpine/edge/testing/ add \  
bash \  
git \  
confd  
  
ADD . /go/src/github.com/ThatsNinja/dockerhub-webhook-listener  
ADD ./etc /etc/confd  
  
# Build  
WORKDIR /go/src/github.com/ThatsNinja/dockerhub-webhook-listener/hub-listener  
RUN go get gopkg.in/gcfg.v1  
RUN go build  
  
ENTRYPOINT ["/go/src/github.com/ThatsNinja/dockerhub-webhook-
listener/bin/docker-entrypoint.sh"]  
CMD /go/src/github.com/ThatsNinja/dockerhub-webhook-listener/hub-listener/hub-
listener --config-file=/tmp/config.ini --listen=$listen_addr  


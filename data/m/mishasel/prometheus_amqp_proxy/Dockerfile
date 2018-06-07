FROM golang:alpine  
MAINTAINER Misha Seltzer  
  
COPY proxy/proxy.go /go/src/github.com/mishas/prometheus_amqp_proxy/proxy/  
COPY proxy/rpc/*.go /go/src/github.com/mishas/prometheus_amqp_proxy/proxy/rpc/  
  
RUN apk add --update git \  
&& go get -v -d github.com/streadway/amqp \  
&& go install -v github.com/mishas/prometheus_amqp_proxy/proxy/rpc \  
&& go install -v github.com/mishas/prometheus_amqp_proxy/proxy \  
&& apk del --purge git && rm -rf /var/cache/apk/*  
  
EXPOSE 8200  
  
ENTRYPOINT ["bin/proxy"]  
  


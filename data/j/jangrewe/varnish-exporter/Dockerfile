FROM blang/golang-alpine  
MAINTAINER Jan Grewe <jan@faked.org>  
  
RUN go get github.com/jonnenauha/prometheus_varnish_exporter  
ENTRYPOINT /go/bin/prometheus_varnish_exporter  
EXPOSE 9131  


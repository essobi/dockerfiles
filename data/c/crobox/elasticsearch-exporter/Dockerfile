FROM golang:alpine  
  
ADD . /go/src/elasticsearch_exporter  
  
RUN export GO15VENDOREXPERIMENT=1  
RUN apk add --update git \  
&& go get elasticsearch_exporter \  
&& rm -rf /var/cache/apk/*  
  
EXPOSE 9108  
CMD elasticsearch_exporter --es.uri=http://${ELASTICSEARCH_ADDRESS}
\--es.all=true \--web.listen-address=:9108 --web.telemetry-path=/metrics  


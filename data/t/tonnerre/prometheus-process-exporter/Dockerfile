FROM golang:alpine  
MAINTAINER Tonnerre LOMBARD <tonnerre@ancient-solutions.com>  
  
# Install golang dependencies.  
RUN apk --update add git  
RUN go get -d github.com/mitchellh/go-ps  
RUN go get -d github.com/prometheus/client_golang/prometheus  
RUN go get github.com/tonnerre/prometheus-process-exporter  
RUN apk --update del git  
RUN rm -rf /var/cache/apk/*  
  
EXPOSE 8080  
CMD ["/go/bin/prometheus-process-exporter", "--port=8080"]  


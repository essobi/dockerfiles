FROM golang:1.8.3-alpine3.6  
MAINTAINER Valeriano Manassero https://github.com/valeriano-manassero  
  
ENV LOGSTASH_HOST logstash  
ENV LOGSTASH_PORT 9563  
ENV CRON_SECONDS 3600  
RUN mkdir -p /opt/project  
WORKDIR /opt/project  
COPY app/ /opt/project/  
RUN go build ip-maat.go  
  
CMD ["./ip-maat"]


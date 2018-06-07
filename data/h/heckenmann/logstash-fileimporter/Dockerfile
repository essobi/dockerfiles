FROM golang:1.9.2-stretch  
  
RUN mkdir -p /opt/lfi  
WORKDIR /opt/lfi  
COPY logstash-fileimporter.go .  
RUN go build  
  
CMD ./lfi  


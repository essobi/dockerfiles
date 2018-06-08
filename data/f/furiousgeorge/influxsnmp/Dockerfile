FROM golang:alpine  
MAINTAINER furiousgeorge <furiousgeorgecode@gmail.com>  
  
#Required by influxsnmp  
RUN apk --update add git net-snmp-tools  
  
#install influxsnmp  
RUN go get github.com/paulstuart/influxsnmp  
RUN go install github.com/paulstuart/influxsnmp  
RUN mkdir $GOPATH/etc  
CMD ["/go/bin/influxsnmp", "-config", "/config/config.gcfg"]  


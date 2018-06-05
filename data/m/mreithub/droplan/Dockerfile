FROM golang:alpine  
  
RUN apk update && apk add iptables ca-certificates git  
RUN update-ca-certificates  
  
RUN git clone https://github.com/tam7t/droplan.git /go/src/tam7t/droplan/  
RUN go build tam7t/droplan  
  
ENV DO_KEY ""  
ENV DO_TAG ""  
COPY run-droplan.sh /run-droplan.sh  
  
CMD ["/run-droplan.sh"]  
  


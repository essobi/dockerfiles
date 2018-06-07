FROM golang:1.9 as builder  
WORKDIR /go/bin  
RUN go get -d -v github.com/lumenbox/stellar-go/services/federation  
WORKDIR /go/src/github.com/lumenbox/stellar-go/services/federation  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o federation .  
  
WORKDIR /tmp/  
ARG CONFD_VERSION=0.15.0  
ADD
https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-
amd64 /tmp/confd  
COPY confd /etc/confd  
COPY localhost* wait-for-it.sh /  
RUN chmod 755 /go/src/github.com/lumenbox/stellar-
go/services/federation/federation && \  
chmod 755 /tmp/confd && \  
chmod 755 /etc/confd/confd-wrapper.sh && \  
chmod 755 /wait-for-it.sh  
  
FROM alpine:latest  
RUN apk --no-cache add ca-certificates bash  
WORKDIR /root/  
COPY \--from=builder /go/src/github.com/lumenbox/stellar-
go/services/federation/federation /tmp/confd /localhost* /wait-for-it.sh /  
COPY \--from=builder /etc/confd /etc/confd  
EXPOSE 8000  
CMD ["/etc/confd/confd-wrapper.sh"]  
  


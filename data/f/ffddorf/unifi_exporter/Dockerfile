FROM golang as builder  
ENV CGO_ENABLED=0  
ENV GOOS=linux  
RUN go get github.com/mdlayher/unifi_exporter/cmd/unifi_exporter  
  
FROM alpine as cert  
RUN apk --update add ca-certificates  
  
FROM scratch  
COPY \--from=builder /go/bin/unifi_exporter /go/bin/unifi_exporter  
COPY \--from=cert /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-
certificates.crt  
EXPOSE 9130  
CMD ["/go/bin/unifi_exporter"]  


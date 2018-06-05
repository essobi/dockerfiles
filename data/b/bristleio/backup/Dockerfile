FROM alpine:latest as cert  
RUN apk --no-cache --update upgrade && apk --no-cache add ca-certificates  
  
FROM golang:latest as builder  
  
WORKDIR /go/src/app  
COPY app/ .  
  
RUN echo "listing:" && ls  
RUN go get -d -v ./...  
RUN go build -v -o copy .  
RUN echo "listing:" && ls  
  
FROM scratch  
COPY \--from=cert /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-
certificates.crt  
COPY \--from=builder /go/src/app/copy /  
  
CMD ["/copy"]  


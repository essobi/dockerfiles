FROM golang:1.9 as builder  
WORKDIR /go/src/github.com/proofpoint/kubernetes-ldap/  
  
COPY . .  
RUN go get ./...  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o bin/kubernetes-
ldap .  
  
FROM alpine:3.6  
RUN mkdir /opt  
RUN apk add --no-cache ca-certificates  
WORKDIR /opt/  
COPY \--from=builder /go/src/github.com/proofpoint/kubernetes-
ldap/bin/kubernetes-ldap .  
ENTRYPOINT ["./kubernetes-ldap"]  


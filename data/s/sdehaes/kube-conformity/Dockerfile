# builder image  
FROM golang:1.9-alpine as builder  
  
RUN apk -U add git  
WORKDIR /go/src/github.com/stijndehaes/kube-conformity  
COPY . .  
RUN go test -v ./...  
RUN go build -o /bin/kube-conformity -v \  
-ldflags "-X main.version=$(git describe --tags --always --dirty) -w -s"  
  
# final image  
FROM alpine:3.6  
MAINTAINER Stijn De Haes <stijndehaes@gmail.com>  
  
RUN addgroup -S kube-conformity && adduser -S -g kube-conformity kube-
conformity  
RUN apk add --update openssl ca-certificates  
COPY mailtemplate.html /etc/kube-conformity/mailtemplate.html  
COPY config.yaml /etc/kube-conformity/config.yaml  
COPY \--from=builder /bin/kube-conformity /etc/kube-conformity/kube-conformity  
WORKDIR /etc/kube-conformity  
  
USER kube-conformity  
ENTRYPOINT ["./kube-conformity"]  


# Build Operator  
FROM golang:alpine  
RUN apk update && apk add ca-certificates  
RUN apk add make git  
RUN mkdir -p $GOPATH/src/github.com/srleyva/aws-operator  
WORKDIR /go/src/github.com/srleyva/aws-operator  
ADD ./ ./  
RUN make && cp aws-operator /aws-operator  
  
# Inject Binary into container  
FROM scratch  
COPY \--from=0 /etc/ssl/certs /etc/ssl/certs  
COPY \--from=0 /aws-operator /bin/aws-operator  
ENTRYPOINT ["aws-operator"]  


FROM golang:latest as go  
  
WORKDIR /go/src/github.com/base2services/aws-env  
  
COPY . .  
  
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags "-X main.version=$(git describe
--tags)" -v -o /bin/awsenv .  
  
FROM scratch  
  
COPY \--from=go /bin/awsenv /awsenv  
  
COPY \--from=go /etc/ssl/certs /etc/ssl/certs  
  
VOLUME /ssm  
  
ENTRYPOINT ["/awsenv"]  


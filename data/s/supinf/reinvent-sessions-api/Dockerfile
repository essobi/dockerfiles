# Dockerfile  
FROM golang:1.5.0  
MAINTAINER SUPINF Inc.  
  
RUN go get github.com/supinf/reinvent-sessions-api  
  
ENV AWS_REGION us-west-2  
ENV AWS_ACCESS_KEY_ID abcdefg  
ENV AWS_SECRET_ACCESS_KEY 1234567890  
EXPOSE 80  
ENTRYPOINT ["/go/bin/reinvent-sessions-api"]  


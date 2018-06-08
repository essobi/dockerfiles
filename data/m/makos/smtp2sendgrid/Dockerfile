FROM golang:alpine  
  
RUN apk update && apk upgrade && \  
apk add \--no-cache git ca-certificates  
  
WORKDIR /go/src/github.com/akosmarton/smtp-to-sendgrid  
COPY . .  
  
RUN go get -d -v ./...  
RUN go install -v ./...  
  
CMD ["smtp-to-sendgrid"]  


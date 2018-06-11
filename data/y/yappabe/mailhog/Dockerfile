FROM golang:1.4  
RUN apt-get update  
RUN apt-get install -y ca-certificates  
RUN go get github.com/mailhog/MailHog  
  
EXPOSE 1025 8025  
ENTRYPOINT ["/go/bin/MailHog"]  


# Base docker image  
FROM golang:1.4  
MAINTAINER Benoît Benedetti <benoit.benedetti@gmail.com>  
  
ENV REFRESHED_AT 2014-12-30  
RUN go get github.com/mailhog/MailHog  
  
EXPOSE 1025 8025  
ENTRYPOINT ["/go/bin/MailHog"]  


FROM alpine:latest  
MAINTAINER Mike Patton <mpatton125@gmail.com>  
  
RUN apk add \--no-cache git libexif-dev go tor build-base && \  
export GOPATH=/usr/local && \  
go get github.com/s-rah/onionscan  
  
# Make workdir and set permissions  
RUN mkdir /home/onionscan && \  
chown -R tor /home/onionscan  
  
WORKDIR /home/onionscan  
USER tor  
CMD [ "/usr/bin/tor" ]  


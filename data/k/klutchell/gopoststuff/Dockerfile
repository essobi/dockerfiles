FROM golang:alpine  
MAINTAINER Kyle Harding <kylemharding@gmail.com>  
  
RUN apk update && \  
apk add git  
  
RUN go get github.com/ERR1R/GoPostStuff && \  
go install github.com/ERR1R/GoPostStuff  
  
COPY ./run.sh /root/  
  
RUN chmod +x /root/run.sh  
  
VOLUME /config /uploads  
  
ENTRYPOINT ["/root/run.sh"]  


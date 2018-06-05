FROM alpine:edge  
# Originally created by Steve Williams <mrsixw@gmail.com>  
MAINTAINER Olof Johansson <olof@ethup.se>  
  
RUN apk update && apk upgrade && \  
apk add --update bash rsync jq openssh  
  
COPY ./assets/* /opt/resource/  


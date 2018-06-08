FROM alpine:3.4  
MAINTAINER Maxim Zalysin <zalysin.m@gmail.com>  
  
LABEL pro.magnaz.minidlna.version="{\"container\": 1.0, \"alpine\": 3.4
\"minidlna\": 1.1.5}"  
  
RUN apk --no-cache add minidlna  
  
EXPOSE 1900/udp 8200  
ENTRYPOINT ["minidlnad", "-d"]


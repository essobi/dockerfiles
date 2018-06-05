FROM alpine:3.4  
MAINTAINER Maxim Zalysin <zalysin.m@gmail.com>  
  
LABEL pro.magnaz.docker.transmission.version="{\"container\": 1.1, \"alpine\":
3.4, \"transmission\": 2.92}"  
  
RUN apk add --no-cache transmission-daemon  
  
ENV TRANSMISSION_HOME /var/transmission  
  
EXPOSE 9091 51413 51413/udp  
  
VOLUME ["/var/transmission"]  
  
ENTRYPOINT ["transmission-daemon", "--foreground"]


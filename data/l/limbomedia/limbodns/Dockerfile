FROM alpine:3.4  
MAINTAINER Limbomedia <admin@limbomedia.net>  
  
RUN apk add --update openjdk8-jre-base && rm -rf /var/cache/apk/*  
  
ADD http://limbomedia.net/res/files/limbodns-3.0-jar-with-dependencies.jar /  
RUN mkdir data  
  
VOLUME /data  
  
EXPOSE 7777  
EXPOSE 53/tcp  
EXPOSE 53/udp  
  
ENTRYPOINT java -Ddir=/data -jar /limbodns-3.0-jar-with-dependencies.jar  


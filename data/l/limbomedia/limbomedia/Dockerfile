FROM alpine:3.4  
MAINTAINER Limbomedia <admin@limbomedia.net>  
  
RUN apk add --update openjdk8-jre-base ffmpeg imagemagick bash && rm -rf
/var/cache/apk/*  
  
ADD http://files.limbomedia.net/limbomedia-2.10-bin.zip /  
RUN unzip limbomedia-2.10-bin.zip && rm limbomedia-2.10-bin.zip && mkdir data  
  
VOLUME /data  
  
EXPOSE 8000  
EXPOSE 8001  
ENTRYPOINT java -Dlm.dir.data=/data -Dlm.upnp.enabled=false -jar
/limbomedia-2.10/limbomedia.jar  


FROM alpine  
MAINTAINER Thiago Ramos Fanfoni <thiagofanfoni@gmail.com>  
  
RUN \  
apk update \  
&& apk add transmission-daemon \  
&& rm -rf /var/cache/apk/* \  
  
EXPOSE 9091  
COPY ./transmission.sh /usr/local/bin  
WORKDIR /transmission  
VOLUME /transmission  
CMD [ "transmission.sh" ]  


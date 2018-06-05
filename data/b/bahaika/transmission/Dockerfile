FROM alpine:3.2  
MAINTAINER Jérémy SEBAN  
  
RUN apk add --update transmission-cli transmission-daemon  
RUN rm -rf /var/cache/apk/*  
RUN mkdir /etc/transmission  
COPY ./entrypoint.sh /entrypoint.sh  
COPY ./defaults.json /etc/transmission_defaults.json  
RUN chmod +x /entrypoint.sh  
  
VOLUME ["/etc/transmission"]  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 9091 20683  
CMD ["/usr/bin/transmission-daemon", "-g", "/etc/transmission", "--
foreground"]  


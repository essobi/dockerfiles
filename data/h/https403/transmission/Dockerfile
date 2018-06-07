FROM alpine:3.5  
MAINTAINER Hartman Tam <hartmantam@gmail.com>  
  
COPY settings.json /var/lib/transmission-daemon/info/settings.json  
  
RUN apk add --no-cache stunnel  
  
VOLUME ["/downloads", "/incomplete", "/config"]  
  
ADD ./settings.json /var/lib/transmission-daemon/info/settings.json  
  
ADD ./start.sh /start.sh  
RUN chmod u+x /start.sh  
  
EXPOSE 9091 45555  
ENV USERNAME="transmission" \  
PASSWORD="password"  
CMD ["/start.sh"]  


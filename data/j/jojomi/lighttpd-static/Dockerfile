FROM alpine:latest  
MAINTAINER Johannes Mitlmeier <dev.jojomi@yahoo.com>  
  
RUN apk add --update \  
lighttpd \  
&& rm -rf /var/cache/apk/*  
  
ADD lighttpd.conf /etc/lighttpd/lighttpd.conf  
RUN adduser www-data -G www-data -H -s /bin/false -D  
  
EXPOSE 80  
VOLUME /var/www  
  
ENTRYPOINT ["lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]  


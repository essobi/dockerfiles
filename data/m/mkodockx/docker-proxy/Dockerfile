FROM alpine:latest  
MAINTAINER Markus Kosmal <code@m-ko.de>  
  
RUN mkdir -p /run/apache2 && \  
apk add --update-cache apache2 apache2-proxy apache2-utils  
  
ADD proxy.conf /etc/apache2/conf.d/proxy.conf  
ADD htpasswd.sample /etc/apache2/htpasswd  
  
EXPOSE 80  
ENTRYPOINT ["/usr/sbin/apachectl","-D","FOREGROUND"]


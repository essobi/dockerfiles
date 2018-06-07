FROM alpine:3.1  
MAINTAINER David Ichim <david.ichim@eaudeweb.ro>  
  
RUN apk --update add apache2 && \  
apk del build-base && \  
rm -rf /tmp/src && \  
rm -rf /var/cache/apk/*  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/apache2/access.log  
RUN ln -sf /dev/stderr /var/log/apache2/error.log  
  
VOLUME ["/var/log/apache2"]  
  
WORKDIR /etc/apache2  
  
EXPOSE 80  
CMD ["apachectl", "-D", "FOREGROUND"]  


FROM alpine:3.3  
# referred from https://hub.docker.com/r/sebp/lighttpd/  
MAINTAINER Arul <me@arulraj.net>  
  
RUN apk add --update lighttpd \  
&& rm -rf /var/cache/apk/* \  
&& sed -i.bak "s/server.document-root/#server.document-root/g"
/etc/lighttpd/lighttpd.conf \  
&& echo server.document-root = var.basedir >> /etc/lighttpd/lighttpd.conf \  
&& echo server.port = 8080 >> /etc/lighttpd/lighttpd.conf \  
&& echo server.network-backend = \"writev\" >> /etc/lighttpd/lighttpd.conf  
EXPOSE 8080  
VOLUME /var/www/localhost  
WORKDIR /var/www/localhost  
ENTRYPOINT ["lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]  


FROM alpine:latest  
MAINTAINER J. Elfring <devops@elfrinjo.de>  
  
RUN apk add --update --no-cache lighttpd \  
lighttpd-mod_webdav  
  
COPY ./assets/lighttpd.conf /etc/lighttpd/lighttpd.conf  
COPY ./assets/entrypoint.sh /entrypoint.sh  
  
## Fix permissions  
RUN chmod 755 /entrypoint.sh  
  
## Create a workdir for lighttpd  
## And add a pipe, later used for logging  
RUN mkdir /var/run/lighttpd && \  
mkfifo -m 600 /var/run/lighttpd/logpipe && \  
chown -R lighttpd:lighttpd /var/run/lighttpd  
  
ENV TOKEN="s3cret"  
EXPOSE 80  
VOLUME /var/www/localhost/htdocs  
  
ENTRYPOINT [ "/entrypoint.sh" ]  


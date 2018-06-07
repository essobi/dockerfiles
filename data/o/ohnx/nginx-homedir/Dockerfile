# Base image - alpine linux  
FROM alpine:3.7  
# hi. je suis ohnx.  
MAINTAINER ohnx <me@masonx.ca>  
  
# commands to run:  
# update package repo  
# install nginx, sed  
# make /run/nginx so that the pid can be placed there  
RUN apk update && \  
apk add nginx sed && \  
mkdir /run/nginx  
  
# configuration  
COPY site.conf /etc/nginx/conf.d/  
COPY patch-run.sh /usr/bin  
  
# user sites  
VOLUME /root  
VOLUME /home  
  
# nginx  
EXPOSE 80  
STOPSIGNAL SIGTERM  
  
CMD ["patch-run.sh"]  


FROM alpine  
MAINTAINER littleqz@gmail.com  
LABEL description="A lightweight nginx image based on alpine linux."  
  
ENV TERM xterm  
  
ENV SERVER_NAME _  
ENV SITE_ROOT /var/www/src  
ENV ERROR_LOG_LEVEL error  
  
RUN apk update && apk add nginx py-pip && \  
pip install pip j2cli --upgrade && \  
mkdir -p /etc/nginx/sites-enabled && \  
mkdir -p /etc/nginx/sites-available  
  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
ADD ./nginx.conf /etc/nginx/nginx.conf  
ADD ./docker-entrypoint.sh /docker-entrypoint.sh  
  
RUN chmod +x /docker-entrypoint.sh  
  
RUN deluser nginx &>/dev/null; delgroup nginx &>/dev/null; \  
adduser -u 1000 -Dg nginx -s /sbin/nologin -Hh /var/www/html nginx && \  
adduser nginx users  
  
VOLUME /etc/nginx  
WORKDIR /etc/nginx  
EXPOSE 80 443  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["nginx"]  

